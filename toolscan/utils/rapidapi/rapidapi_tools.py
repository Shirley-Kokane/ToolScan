import requests
import copy
from copy import deepcopy
from typing import List, Dict, Any, Union
import os
import ast
import re
import json
from dotenv import load_dotenv

load_dotenv()


def clean_observation(result):

    try:
        execution_output_json = ast.literal_eval(result)
        if "response" in execution_output_json:
            response = execution_output_json["response"]
            return response
    except:
        return result


def log_path(func):
    def wrapper(*args, **kwargs):
        if "action_path" in kwargs.keys():
            action_path = kwargs["action_path"]
            kwargs.pop("action_path")
            success, result = func(*args, **kwargs)

            # convert value in kwargs to string
            # for key, value in kwargs.items():
            # kwargs[key] = str(value)

            if success:
                action_path.append(
                    {
                        "Action": func.__name__,
                        "Action Input": str(kwargs),
                        "Observation": result,
                        "Subgoal": clean_observation(result),
                    }
                )
                return result
            else:
                action_path.append(
                    {
                        "Action": func.__name__,
                        "Action Input": str(kwargs),
                        "Observation": result,
                        "Subgoal": "Calling "
                        + func.__name__
                        + " with "
                        + str(kwargs)
                        + " failed",
                    }
                )
                return result
        else:
            return func(*args, **kwargs)

    return wrapper


class rapidapi_toolkits:
    def __init__(self):
        self.category_map = self.open_json(
            "{}/toolscan/utils/rapidapi/category_map.json".format(
                os.environ["PROJECT_PATH"]
            )
        )

    def standardize_toolbench_name(self, string):
        res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9^_]")
        string = res.sub("_", string)
        string = re.sub(r"(_)\1+", "_", string).lower()
        while True:
            if len(string) == 0:
                return string
            if string[0] == "_":
                string = string[1:]
            else:
                break
        while True:
            if len(string) == 0:
                return string
            if string[-1] == "_":
                string = string[:-1]
            else:
                break
        if string[0].isdigit():
            string = "get_" + string
        return string

    def change_toolbench_name(self, name):
        change_list = ["from", "class", "return", "false", "true", "id", "and"]
        if name in change_list:
            name = "is_" + name
        return name

    def open_json(self, filepath):
        reader = open(filepath, "r", encoding="utf-8")
        data = json.load(reader)
        return data

    def execute_toolbench_request(
        self,
        category,
        tool_name,
        api_name,
        payload,
        toolbench_key="",
    ):
        service_url = "http://10.144.33.138:9120/rapidapi"

        try:

            original_toolbench_key = os.environ["TOOLBENCH_KEY"]
        except:
            print("path for oirginal toolbench key not exists")

        # category = tools_dict[tool_name]["category"]
        api_name = self.change_toolbench_name(self.standardize_toolbench_name(api_name))
        # tool_input = str(json.dumps(payload))
        tool_input = {
            self.standardize_toolbench_name(key): value
            for key, value in payload.items()
        }

        to_send_payload = {
            "category": category,
            "tool_name": tool_name,
            "api_name": api_name,
            "tool_input": tool_input,
            "strip": "truncate",
            "toolbench_key": original_toolbench_key,
        }

        # print("     to send payload =", to_send_payload)
        headers = {"toolbench_key": original_toolbench_key}

        num_tries = 5

        # success_call = False
        # output = {"error": "Failed to execute request. Maybe timeout or API is broken?", "response": ""}
        for trial_index in range(num_tries):

            try:
                output = requests.post(
                    "http://8.130.32.149:8080/rapidapi",
                    json=to_send_payload,
                    headers=headers,
                    timeout=15,
                )
                if output.status_code == 200:
                    return True, output.text
            except:
                return False, "BAD_REQUEST"

        return True, output.text

    @log_path
    def get_executetool(self, params):
        ## create a category lookup table
        ## find what action belongs to which category
        action = params["action"]
        action_input = params["action_input"]
        category = self.category_map[action]
        for_idx = action.rfind("_for_")
        api_name = self.standardize_toolbench_name(action[:for_idx])
        tool_name = self.standardize_toolbench_name(action[for_idx + 5 :])

        try:
            return self.execute_toolbench_request(
                category, tool_name, api_name, action_input
            )
        except:

            return False, "BAD_REQUEST"

    @log_path
    def finish(self, answer):
        if type(answer) == list:
            answer = sorted(answer)
        return True, answer
