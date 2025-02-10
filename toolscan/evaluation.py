import os
import re
import warnings
import yaml
import json
import argparse
from dotenv import load_dotenv
from tool import EvalTool
from llm import load_llm
from utils.logging.toollogger import ToolLogger
from utils.logging.logger import SummaryLogger


logger = ToolLogger(__name__)
warnings.filterwarnings("ignore")

DATA_TASKS = [""]


def path_constructor(loader, node):
    path_matcher = re.compile(r"\$\{([^}^{]+)\}")
    """ Extract the matched value, expand env variable, and replace the match """
    value = node.value
    match = path_matcher.match(value)
    env_var = match.group()[2:-1]
    return os.environ.get(env_var) + value[match.end() :]


def load_config_details(PROJECT_PATH):
    env_config = {
        "seed": 1234,
        "dataset_dir": os.path.join(PROJECT_PATH, "data/"),
        "result_dir": os.path.join(PROJECT_PATH, "results"),
        "check_actions": "check_valid_actions",
        "init_prompt_path": os.path.join(PROJECT_PATH, "toolscan/prompts"),
    }

    agent_config = {
        "name": "VanillaAgent",
        "memory_size": 100,
        "need_goal": True,
        "init_prompt_path": os.path.join(PROJECT_PATH, "toolscan/prompts"),
    }

    run_config = {
        "max_num_steps": 5,
        "project_name": "eval-test",
        "feedback_flag": True,
        "log_path": os.path.join(PROJECT_PATH, "results/test"),
    }

    return env_config, agent_config, run_config


def load_config(cfg_path, args):
    path_matcher = re.compile(r"\$\{([^}^{]+)\}")
    yaml.add_implicit_resolver("!path", path_matcher)
    yaml.add_constructor("!path", path_constructor)

    with open(cfg_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    llm_config = config["llm"]

    env_config, agent_config, run_config = load_config_details(args.PROJECT_PATH)

    if args.log_path != "":
        run_config["log_path"] = args.log_path
    if args.project_name != "":
        run_config["project_name"] = args.project_name

    return llm_config, agent_config, env_config, run_config


def check_log_paths_are_ready(log_dir, baseline_dir):

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(os.path.join(log_dir, "logs")):
        os.makedirs(os.path.join(log_dir, "logs"))

    if not os.path.exists(baseline_dir):
        os.makedirs(baseline_dir)

    if not os.path.exists(os.path.join(log_dir, "all_results.txt")):
        with open(os.path.join(log_dir, "all_results.txt"), "w") as f:
            f.write("")
            f.close()

    return True


def main(args):
    load_dotenv()  # take environment variables from .env., load openai api key, tool key, project path...

    args.cfg_path = os.path.join(
        args.PROJECT_PATH, "toolscan/configs/main_results_all_tasks.yaml"
    )

    args.log_path = os.path.join(args.PROJECT_PATH, "/results/", args.model)

    llm_config, agent_config, env_config, run_config = load_config(args.cfg_path, args)
    llm_config = llm_config[args.model]

    # ---------------------------------------------- load llm -----------------------------------------------------
    logger.info("Start loading language model")

    llm = load_llm(llm_config["name"], llm_config)

    logger.info("Finished loading language model")

    log_dir = run_config.get("log_path", None)

    baseline_path = run_config.get("baseline_dir", "data/baseline_results_details")

    assert check_log_paths_are_ready(log_dir, baseline_path)

    toolscan = SummaryLogger(log_path=log_dir)

    log_history = dict()
    for line in open(os.path.join(log_dir, "all_results.txt"), "r"):
        logger.info(line)
        if "_summary" not in line:
            log_history[json.loads(line.strip())["task_name"]] = json.loads(
                line.strip()
            )

    logger.info("Tested tasks: " + " ".join(log_history))

    logger.info(f"Start evaluating Queries")

    agent_task_config = agent_config.copy()
    for key in env_config:
        if key in ["check_actions", "check_inventory", "init_prompt_path"]:
            agent_task_config[key] = env_config[key]

    task = EvalTool(
        args.task_data,
        run_config,
        llm_config,
        agent_task_config,
        env_config,
        llm=llm,
        log_path=args.log_path,
    )

    success_rates, errors = task.evaluate()

    success_rate = sum(success_rates) * 1.0 / len(success_rates)

    logger.finish(
        f"Task {args.task_data} | Error Success Rate: {errors['sr']}, Insufficient api accuracy: {errors['iac']}, Repeat call accuracy {errors['rc']}, Incorrect arg value accuracy: {errors['iav']}, Invalid Format errors: {errors['fe']}, Incorrect argument type accuracy: {errors['iat']}, Incorrect arg name accuracy: {errors['ian']},Incorrect function name accuracy: {errors['ifn']}, "
    )

    toolscan.log_run_result(args.task_data, success_rate, errors)

    logger.info("Finish evaluating all tasks")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LAM evaluation")

    parser.add_argument(
        "-p",
        "--PROJECT_PATH",
        type=str,
        default="",
        help="repo start",
    )

    parser.add_argument("-m", "--model", type=str, default="gpt-3.5-turbo-16k")
    parser.add_argument("-d", "--task_data", type=str, default="total")
    parser.add_argument(
        "-c",
        "--cfg_path",
        type=str,
        default="toolscan/configs/main_results_all_tasks.yaml",
    )
    parser.add_argument("-l", "--log_path", type=str, default="")

    args = parser.parse_args()

    main(args)
