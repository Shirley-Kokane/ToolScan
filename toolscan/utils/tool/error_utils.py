import os
import json
import numpy as np
import ast
import re
import ast
import pdb


def clean_dict(data):
    for key in data:
        # Check if the value is a list with a single element
        if isinstance(data[key], list) and len(data[key]) == 1:
            # Replace the list with the single element
            data[key] = data[key][0]
    return data


def map_apilist(apilist):
    for apiname in apilist:
        if apiname.lower() != "finish" and apiname.lower() != "check_valid_actions":
            api_params = apilist[apiname]["parameters"]
            for argname in api_params:
                if api_params[argname]["type"] in {
                    "str",
                    "enum",
                    "string",
                    "STR",
                    "ENUM",
                    "STRING",
                }:
                    api_params[argname]["type"] = str
                elif api_params[argname]["type"] in {"number", "num", "NUMBER", "NUM"}:
                    api_params[argname]["type"] = (int, float, complex)
                elif api_params[argname]["type"] in {
                    "boolean",
                    "bool",
                    "BOOLEAN",
                    "BOOL",
                }:
                    api_params[argname]["type"] = bool
    return apilist


class ErrorMetric:
    def __init__(self, apilist, groundtruth, N) -> None:
        self.apilist = map_apilist(apilist)
        self.groundtruth = groundtruth
        self.N = N

        self.errors = {}
        self.invalid_function_name = 0
        self.invalid_argument_name = 0
        self.invalid_argument_type = 0
        self.insufficient_api_calls = 0
        self.incorrect_argument_values = 0
        self.missing_argument = 0
        self.total_interactions = 0
        self.repeat_calls = 0
        self.format_errors = 0

        self.errors["iac"] = 0
        self.errors["iav"] = 0
        self.errors["ifn"] = 0
        self.errors["ian"] = 0
        self.errors["iat"] = 0
        self.errors["fe"] = 0
        self.errors["sr"] = 0
        self.errors["rc"] = 0

    def fn_incorrectargumentvalues(self, groundtruth_sample: dict, modeloutput: dict):

        wav = 0
        for gt_api_name, gt_api_args_list in groundtruth_sample.items():
            if gt_api_name in modeloutput:
                model_args_list = modeloutput[gt_api_name]
                for gt_api_args_sample in gt_api_args_list:
                    gt_api_args_sample_refined = {
                        k: v for k, v in gt_api_args_sample.items() if v != "optional"
                    }
                    if gt_api_args_sample_refined not in model_args_list:
                        wav += 1

        return wav

    def fn_insufficientapicalls(self, groundtruth_sample: dict, modeloutput: dict):
        insufficient_api_count = 0
        model_per_api_count = {}
        gt_per_api_count = {}
        count_gt_apis = 0

        for model_api in modeloutput:
            model_per_api_count[model_api] = len(modeloutput[model_api])
        for gt_api in groundtruth_sample:
            gt_per_api_count[gt_api] = len(groundtruth_sample[gt_api])
            count_gt_apis += len(groundtruth_sample[gt_api])

        for api_name in gt_per_api_count:
            if api_name in model_per_api_count:
                insufficient_api_count += max(
                    gt_per_api_count[api_name] - model_per_api_count[api_name], 0
                )
            else:
                insufficient_api_count += gt_per_api_count[api_name]

        return insufficient_api_count, count_gt_apis

    def fn_invalidargumentname(self, action, action_input):
        count = []

        # for action in model_apis:
        if action in self.apilist:

            for argname in action_input:  # modeloutput[action].keys():
                if argname not in self.apilist[action]["parameters"]:

                    count.append(argname)

        return count

    def fn_missingargumentname(self, action, action_input):
        count = []
        # model_apis = [action]

        if action in self.apilist:
            for argname in self.apilist[action]["parameters"]:
                if (
                    self.apilist[action]["parameters"][argname]["required"]
                    and argname not in action_input
                ):
                    count.append(argname)

        return count

    def fn_invalidargumenttype(self, action, action_input):
        count = []
        # model_apis = [action]
        # for action in model_apis:
        if (
            action in self.apilist
            and action.lower() != "finish"
            and action.lower() != "check_valid_actions"
        ):
            # model_params = action_input
            for argname in action_input:
                if argname in self.apilist[action]["parameters"]:
                    if not isinstance(
                        action_input[argname],
                        self.apilist[action]["parameters"][argname]["type"],
                    ):
                        count.append(argname)

        return count

    def fn_invalidfunctionname(self, action):
        count = []

        # for apiname in model_apis:
        if action not in self.apilist and action.lower() != "finish":
            count.append(action)
        return count

    def fn_countinteractions(self, modeloutput):
        model_apis = [(modeloutput.keys())]
        model_apis = [m for m in model_apis if m.lower() != "finish"]
        return len(model_apis)

    def error_calculate(self, action, action_input):
        min_ifn, min_ian, min_iat = [], [], []

        if len(self.groundtruth) == 0:
            return 0, 0, 0

        min_ifn = self.fn_invalidfunctionname(action)
        min_ian = self.fn_invalidargumentname(action, action_input)
        min_iat = self.fn_invalidargumenttype(action, action_input)
        min_man = self.fn_missingargumentname(action, action_input)

        return min_ifn, min_ian, min_iat, min_man

    def update(self, action, action_input):
        (
            invalid_function_name,
            invalid_argument_name,
            invalid_argument_type,
            missing_argument,
        ) = self.error_calculate(action, action_input)
        self.invalid_function_name += len(invalid_function_name)
        self.invalid_argument_name += min(
            1, max(len(invalid_argument_name), len(missing_argument))
        )
        self.invalid_argument_type += min(1, len(invalid_argument_type))
        self.missing_argument += min(1, len(missing_argument))
        feedback = ""

        if len(invalid_function_name) > 0:
            func_names = list(self.apilist.keys())
            feedback = f"ERROR | Incorrect function name {action} please refer to the list of function calls available {func_names}"
            return feedback
        if len(invalid_argument_name) > 0:
            for argname in invalid_argument_name:
                actionlist = list(self.apilist[action]["parameters"].keys())
                if len(actionlist) > 0:
                    feedback += f"ERROR | Incorrect argument name {argname} for function {action}, Valid arguments are {actionlist}"
                else:
                    feedback += f"ERROR | Incorrect argument name {argname} for function {action}, this function does not require any arguments."
            return feedback
        if len(missing_argument) > 0:

            feedback += f"ERROR | Insufficient required arguments for function {action}, Please add the required argument {missing_argument}"

            return feedback

        if len(invalid_argument_type) > 0:
            for argname in invalid_argument_type:
                actiontype = self.apilist[action]["parameters"][argname]["type"]
                feedback += f"ERROR | Incorrect argument type for {argname} for function {action}, Valid argument type is {actiontype}"
            return feedback

        return None

    def calculate_rem_metric(self, action_route):
        if len(action_route) > 0:
            pergt_scores = []
            count_gt_apis_list = []
            for groundtruth_sample in self.groundtruth:
                min_iav = self.fn_incorrectargumentvalues(
                    groundtruth_sample, action_route
                )
                min_iac, count_gt_apis = self.fn_insufficientapicalls(
                    groundtruth_sample, action_route
                )
                count_gt_apis_list.append(count_gt_apis)
                pergt_scores.append((min_iac, min_iav))

            idx = pergt_scores.index(min(pergt_scores))
            count_gt_apis = count_gt_apis_list[idx]
            # self.N = len(action_route)

            self.errors["iac"] = (count_gt_apis - pergt_scores[idx][0]) / count_gt_apis
            self.errors["iav"] = (self.N - (pergt_scores[idx][1])) / self.N
            self.errors["ifn"] = (self.N - self.invalid_function_name) / self.N
            self.errors["ian"] = (self.N - self.invalid_argument_name) / self.N
            self.errors["iat"] = (self.N - self.invalid_argument_type) / self.N
            self.errors["fe"] = (self.N - self.format_errors) / self.N
            self.errors["rc"] = (self.N - self.repeat_calls) / self.N
            self.errors["sr"] = 0

        self.total_interactions = len(action_route)
