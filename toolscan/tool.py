import os
import time
import numpy as np
import json
from typing import Any, Dict, List, Union

from llm import load_llm
from agents import load_agent
from environment import load_environment
from apilist import load_apilist
from utils.tool.data_utils import ToolDataset
from utils.tool.error_utils import ErrorMetric

from utils.logging.logger import TaskLogger
from utils.logging.toollogger import ToolLogger

from utils.tool.helpers import (
    extract_action_name_and_action_input,
    check_credentials,
    contains_network_error,
)
from prompts import load_prompt_example
from utils.tool.helpers import parse_action
from collections import defaultdict

logger = ToolLogger(__name__)


class EvalTool:
    def __init__(
        self,
        task_name=None,
        run_config=None,
        llm_config=None,
        agent_config=None,
        env_config=None,
        llm=None,
        max_num_steps=10,
        log_path=None,
    ):

        self.run_config = run_config
        self.feedback_flag = run_config["feedback_flag"]
        self.agent_config = agent_config
        self.env_config = env_config
        self.max_num_steps = max_num_steps
        if llm is None:
            llm = load_llm(llm_config["name"], llm_config)

        self.init_prompt_path = agent_config["init_prompt_path"]
        agent_config["init_prompt_path"] = None

        self.agent = load_agent(agent_config["name"], agent_config, llm)

        self.toolscan = TaskLogger(
            task_name, log_path=log_path, max_num_steps=self.max_num_steps
        )

        # check credentials for movie, todo and sheet
        check_credentials()

    def evaluate(self):
        # get dataset
        self.dataset = self.load_dataset(
            self.env_config["dataset_dir"],
            self.env_config["result_dir"],
        )

        dataset_size = len(self.dataset)
        success_rates = []
        num_steps = []
        errors = {k: 0 for k in ["iac", "iav", "ifn", "ian", "iat", "fe", "sr", "rc"]}

        for id in range(dataset_size):
            success, steps, output, errormetric = self.evaluate_env(id)

            if success:
                success_rates.append(1)
            else:
                success_rates.append(0)

            errors = {k: v + errormetric[k] for k, v in errors.items()}

            num_steps.append(steps)

            logger.finish(
                "Example {} | Success: {} , Steps: {}\n".format(id, success, steps)
            )

        errors = {k: v / dataset_size for k, v in errors.items()}

        return success_rates, errors

    def prompt_edit(self, api_list, toolname):
        final_api = ""
        for api_key, api_value in api_list.items():
            result = f"\nName: {api_key} \nDescription: {api_value['description']}\nParameters:"
            for param, param_value in api_value["parameters"].items():
                result += f"\n- {param} (Type: {param_value['type']}, Required: {param_value['required']}): {param_value['description']}"
            if "returns" in api_value:
                result += f"\nReturns: {api_value}\n"
            final_api += result

        # final_api += "\nName: finish(answer)\nDescription: Return an answer and finish the task\nParameters:\n- answer (Type: ['string', 'number', 'array']): The answer to be returned that is limited upto 200 tokens. If the answer exceeds 200 tokens, please summarize it to reach the limit.\n\n"

        self.agent.init_prompt_dict = json.load(
            open("/".join([self.init_prompt_path, f"standard_prompt.json"]), "r")
        )
        self.agent.init_prompt_dict["examples"] = load_prompt_example(toolname)

        self.agent.instruction = (
            self.agent.init_prompt_dict["instruction"]
            + final_api
            + self.agent.init_prompt_dict["final_instruction"]
        )

        self.agent.examples = self.agent.init_prompt_dict["examples"]

    def initialize_dataset_sample(self, id):
        dataset_i = {}

        dataset_i["goal"] = self.dataset.goals[id]
        dataset_i["ground_truth"] = self.dataset.ground_truth[id]

        # dataset.api_list[id]
        dataset_i["tool"] = self.dataset.tools[id]
        dataset_i["api_list"] = load_apilist(
            self.dataset.tools[id], self.dataset.category[id]
        )

        if dataset_i["tool"] == "weather":
            #! Same operation for todo
            dataset_i["current_date"] = self.dataset.init_configs[id]["current_date"]
            dataset_i["current_location"] = self.dataset.init_configs[id][
                "current_location"
            ]

        return dataset_i

    def evaluate_env(self, id):
        dataset = self.dataset
        env_config = self.env_config.copy()

        # dataset_i is passed to env_config, and then passed to initialize env

        env_config["dataset"] = self.initialize_dataset_sample(id)

        self.env = load_environment(env_config["dataset"]["tool"], env_config)
        # pdb.set_trace()
        self.errormetric = ErrorMetric(
            env_config["dataset"]["api_list"], env_config["dataset"]["ground_truth"], 10
        )

        # get task infomation
        goal = self.dataset.goals[id]
        ground_truth = self.dataset.ground_truths[id]
        tool = self.dataset.tools[id]
        goal_type = self.dataset.goal_types[id]
        # difficulty = self.dataset.difficulties[id]

        action_path = []
        action_route = defaultdict(list)
        self.env.action_path = action_path

        self.prompt_edit(
            env_config["dataset"]["api_list"], env_config["dataset"]["tool"]
        )

        if tool == "weather":
            init_obs = "If you want to get the latitude and longitude information of a city, you must call \"get_latitude_longitude\", do not generate it by yourself which maybe wrong. Once you have finished the goal, please remember to take 'finish' action to end this goal."
            self.agent.reset(goal, init_obs)

            self.env.weather_toolkits.current_date = self.dataset.init_configs[id][
                "current_date"
            ]
            self.env.weather_toolkits.current_location = self.dataset.init_configs[id][
                "current_location"
            ]
        else:
            init_obs = "Once you have finished the goal, please remember to take 'finish' action to end this goal."
            self.agent.reset(goal, init_obs)

        logger.goal("Example {} | Goal: {}".format(id, self.agent.goal))

        max_steps = self.run_config["max_num_steps"]

        trajectory = []
        trajectory.append({"Goal": goal, "id": 0})
        trajectory.append({"Observation": init_obs, "id": 0})

        for step_id in range(max_steps):

            try:
                _, message = self.agent.run()
                message = message.strip()

                logger.info("Step {:02} - Message: {}".format(step_id, message))

                trajectory.append({"Action": message, "id": step_id})

                action, action_input = None, None
                try:
                    action, action_input = extract_action_name_and_action_input(message)

                    action_with_action_input = (
                        "Action: " + action + " with Action Input: " + action_input
                    )
                    action, action_input = parse_action(action_with_action_input)

                except Exception as e:
                    observation = (
                        "ERROR | "
                        + type(e).__name__
                        + "("
                        + str(e)
                        + ")"
                        + ' Format error, please response in the format of  "Action: [your action] with Action Input: [your action input]'
                    )
                    done = False
                    self.errormetric.format_errors += 1
                    self.agent.update(action="", state=observation)

                logger.info("Step {:02} - Action: {}".format(step_id, action))
                logger.info(
                    "Step {:02} - Action Input: {}".format(step_id, action_input)
                )

                if action:
                    # pdb.set_trace()
                    if action != "finish":
                        feedback = self.errormetric.update(action, action_input)

                    if self.feedback_flag and feedback != None:
                        observation, done = feedback, False
                        self.agent.update(action="", state=observation)
                    else:
                        # action_with_action_input = "Action: " + action + " with Action Input: " + action_input
                        # pdb.set_trace()
                        observation, done = self.env.step(
                            action_type=action,
                            params=action_input,
                            action_path=action_path,
                        )

                        self.agent.update(
                            action=action + " with Action Input: " + str(action_input),
                            state=observation,
                        )

                        if (
                            action in action_route
                            and action_input in action_route[action]
                        ):
                            self.errormetric.repeat_calls += 1
                        elif action != "finish":
                            action_route[action].append(action_input)

                    logger.info(
                        "Step {:02} - Observation: {}".format(step_id, observation)
                    )
                    trajectory.append({"Observation": observation, "id": step_id})

                else:
                    observation = (
                        "ERROR | "
                        + ' Format error, please response in the format of  "Action: [your action] with Action Input: [your action input]'
                    )
                    done = False
                    self.errormetric.format_errors += 1
                    self.agent.update(action="", state=observation)
                    logger.info(
                        "Step {:02} - Observation: {}".format(step_id, observation)
                    )

                if contains_network_error(observation):
                    raise Exception(observation)

                # Early stop if the agent has finished the task.
                if done:
                    output = observation
                    logger.info("Example {} | Finished with {}".format(id, output))
                    break

            except Exception as e:
                done = False
                output = "Example {} | Error: {}".format(id, str(e))
                logger.info(output)
                # Since there is an Exception, we must break the evaluation of this example.
                break

        if step_id == (max_steps - 1) and not done:
            output = "Example {} | Error: Exceed max steps".format(id)
            logger.info(output)

        self.errormetric.calculate_rem_metric(action_route)
        error_sr = (sum(self.errormetric.errors.values())) / 7

        if done:
            if goal_type == 1:
                success = self.get_todo_score(output, ground_truth)
                self.errormetric.errors["sr"] = success

            else:
                success = True
                self.errormetric.errors["sr"] = error_sr
        else:
            success = False
            self.errormetric.errors["sr"] = success

        logger.info("Example {} | Ground Truth: {}".format(id, str(ground_truth)))

        env_details = {"task_name": tool, "goal": goal}
        try:
            example_prompt = self.agent.get_example_prompt()
        except:
            example_prompt = None

        self.toolscan.log_example(
            id,
            success,
            self.errormetric.errors,
            env_details,
            trajectory,
            example_prompt,
        )

        return (
            success,
            step_id + 1,
            output,
            self.errormetric.errors,
        )

    def get_todo_score(self, output, ground_truth):

        return output == ground_truth

    def load_dataset(self, dataset_dir, result_dir):
        dataset_file = os.path.join(dataset_dir, "test.jsonl")

        dataset = ToolDataset(test_file=dataset_file)

        logger.info("Load dataset with {} examples".format(len(dataset)))
        return dataset

    @classmethod
    def from_config(cls, run_config, llm_config, agent_config, env_config, llm=None):
        # run_config
        run_config["max_num_trials"] = run_config.get("max_num_trials", 4)
        run_config["max_num_steps"] = run_config.get("max_num_steps", 10)
        run_config["env_num_per_task"] = run_config.get("env_num_per_task", 1)
        run_config["grounding"] = run_config.get("grounding", False)

        # llm config
        llm_config["name"] = llm_config.get("name", "gpt")

        # agent config
        agent_config["name"] = agent_config.get("name", "vanilla")
        agent_config["use_parser"] = llm_config.get("use_parser", True)

        # env config
        env_config["seed"] = env_config.get("seed", 1234)

        max_num_steps = run_config.get("max_num_steps", 10)

        log_path = run_config.get("log_path", None)

        return cls(
            run_config=run_config,
            llm_config=llm_config,
            agent_config=agent_config,
            env_config=env_config,
            llm=llm,
            max_num_steps=max_num_steps,
            log_path=log_path,
        )
