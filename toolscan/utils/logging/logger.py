import os
import json
import re
import logging
import numpy as np


class SummaryLogger:
    def __init__(self, log_path):

        self.current_run_metrics = []
        self.log_path = os.path.join(log_path, "all_results.txt")
        self.log_dimension_path = os.path.join(log_path, "dimension.txt")

    def check_metric_item_is_logged(self, metric_type, file_name):
        with open(file_name) as f:
            for line in f:
                if metric_type in line:
                    return True
        return False

    def log_run_result(self, task_name, success_rate, errors):
        result = {
            "task_name": task_name,
            "success_rate": success_rate,
            "error_success_rate": errors["sr"],
            "insufficient_api_calls": errors["iac"],
            "repeat_calls": errors["rc"],
            "incorrect_argument_values": errors["iav"],
            "incorrect_argument_type": errors["iat"],
            "invalid_argument_names": errors["ian"],
            "invalid_function_names": errors["ifn"],
            "format_errors": errors["fe"],
        }

        self.current_run_metrics.append(result)

        if not self.check_metric_item_is_logged(task_name, self.log_path):
            with open(self.log_path, "a+") as f:
                f.write(json.dumps(result) + "\n")


class TaskLogger:
    def __init__(self, task_name, log_path, max_num_steps=10):
        self.task_name = task_name

        self.max_num_steps = max_num_steps

        self.log_path = os.path.join(log_path, "logs", f"{task_name}.jsonl")
        self.log_summary_path = os.path.join(log_path, f"{task_name}.txt")

        with open(self.log_path, "w") as f:
            f.write("")
            f.close()

        with open(self.log_summary_path, "w") as f:
            f.write("")
            f.close()

    def extract_variables(self, line):
        pattern = r"\[EXP\] (\d+): \[success_rate\]: (.*), \[progress_rate\]: (.*), \[grounding_acc\]: (.*), \[score_state\]: (.*)"
        match = re.match(pattern, line)
        if match:
            i = int(match.group(1))
            sr_temp = match.group(2)
            if sr_temp == "True":
                sr_temp = 1
            if sr_temp == "False":
                sr_temp = 0
            sr = float(sr_temp)
            score = float(match.group(3))
            grounding_acc = float(match.group(4))
            score_state_str = match.group(5)
            score_state = eval(score_state_str)

            # make score_state index integer, and value float
            score_state = [(int(step), float(score)) for step, score in score_state]
            return_dict = {
                "EXP": i,
                "success_rate": sr,
                "progress_rate": score,
                "grounding_acc": grounding_acc,
                "score_state": score_state,
            }
            return return_dict

    def save_sample_data_to_file_detailed(
        self, id, is_done, errors, env_details, trajectory
    ):

        sample_result = dict()
        sample_result["id"] = id
        sample_result.update(env_details)
        sample_result["is_done"] = is_done
        sample_result["trajectory"] = {}

        for item in trajectory:
            type = list(item.keys())[0]
            step_id = int(item["id"])
            content = item[type]

            step_name = f"Interaction Turn {step_id}"

            if step_name not in sample_result["trajectory"]:
                sample_result["trajectory"][step_name] = dict()
                # sample_result["trajectory"][int(step_id)]["Interaction Turn"] = step_id
            sample_result["trajectory"][step_name][type] = content

        with open(self.log_path, "a+") as f:
            f.write(json.dumps(sample_result, indent=2) + "\n")

    def save_sample_data_to_file_overview(
        self, id, is_done, errors, env_details, trajectory
    ):
        with open(self.log_summary_path, "a+") as f:
            f.write(
                f"[EXP] {id}: [success_rate]: {is_done}, [Error Success Rate] : {errors['sr']},[insufficient api calls]: {errors['iac']},[repeat api calls]: {errors['rc']}, [incorrect argument values]: {errors['iav']}, [invalid argument names]: {errors['ian']},[invalid function names]: {errors['ifn']},[invalid argument type]: {errors['iat']}, [format errors]: {errors['fe']} \n"
            )

    def log_example(
        self,
        id,
        is_done,
        errors,
        env_details,
        trajectory,
        example_prompt=None,
    ):
        self.save_sample_data_to_file_detailed(
            id, is_done, errors, env_details, trajectory
        )  # log to file
        self.save_sample_data_to_file_overview(
            id, is_done, errors, env_details, trajectory
        )
