import gym
import subprocess
import os
import re
import numpy as np


class BaseEnvironment(gym.Env):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()
        self.action_path = []

        if not use_dataset:
            self.dataset = None
        else:
            self.dataset = dataset
        self.reset()

    def get_info(self):
        return self.infos

    def get_obs(self):
        return self.states[-1]

    def get_goal(self):
        return self.goal

    def get_history(self):
        return self.history

    def get_action_space(self):
        """ """
        pass

    def is_done(self):
        return self.done

    def update(self, action, obs, reward, done, infos):
        pass

    def reset(self):
        if self.dataset is not None:
            self.ground_truth = self.dataset["ground_truth"]
        else:
            self.goal = None

        self.init_obs = "New trial starts. Once you have finished the goal, please remember to take 'finish' action to end this goal."

        self.infos = dict()
        self.errors = dict()
        self.errors["invalid_function_name"] = 0
        self.errors["invalid_argument_name"] = 0
        self.errors["invalid_argument_type"] = 0
        self.errors["insufficient_api_calls"] = 0
        self.errors["incorrect_argument_values"] = 0

        self.states = [self.init_obs]  # record a stream of states
        self.history = [
            ("state", self.init_obs)
        ]  # record a stream of s0, a0, r0, s1, a1, r1, ...
        self.steps = 0

        self.infos["states"] = self.states
        self.infos["history"] = self.history
        self.infos["steps"] = self.steps
        self.infos["state"] = self.states[-1]

        self.done = False

    def step(self, action):
        pass

    def save_log(self, log_path):
        pass

    @classmethod
    def from_config(cls, config):
        env = cls(dataset=config.get("dataset"))

        return env
