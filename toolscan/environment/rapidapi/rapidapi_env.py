import json
import ast
import random
from tqdm import tqdm
import os
import pandas as pd
import matplotlib.pyplot as plt
import copy
import time
from environment.base_env import BaseEnvironment
from utils.rapidapi.rapidapi_tools import rapidapi_toolkits
from utils.tool.helpers import parse_action

tools_dict = {}

import requests
import re


# @registry.register_environment("movie")
class RapidapiEnv(BaseEnvironment):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()
        self.action_path = []
        self.rapidapi_toolkits = rapidapi_toolkits()
        if not use_dataset:
            self.dataset = None
        else:
            self.dataset = dataset
        self.reset()

    def step(self, action_type, params, action_path=None):
        if action_path == None:
            action_path = self.action_path

        if action_type == "finish" or action_type == "Finish":
            observation = self.rapidapi_toolkits.finish(
                answer=params["answer"], action_path=action_path
            )

        else:
            param_dict = {}
            param_dict["action"] = action_type
            param_dict["action_input"] = params
            try:
                observation = self.rapidapi_toolkits.get_executetool(
                    params=param_dict, action_path=action_path
                )
            except Exception as e:
                observation = "ERROR | " + type(e).__name__ + "(" + str(e) + ")"
                done = False

        done = "Finish" in action_type or "finish" in action_type
        self.done = done

        return str(observation), self.done
