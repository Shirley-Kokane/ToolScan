import json
import os
from agents.vanilla_agent import VanillaAgent
from collections import defaultdict


def parse_json_with_duplicates(json_data):
    def handle_duplicates(pairs):
        result = defaultdict(list)
        for key, value in pairs:
            result[key].append(value)
        return dict(result)

    return json.loads(json_data, object_pairs_hook=handle_duplicates)


class ToolDataset:
    def __init__(self, test_file) -> None:
        super().__init__()
        self._load_data(test_file)

    def _load_data(self, test_file_path):

        data = None

        with open(test_file_path, "rt") as r:
            raw_json = r.read()

        decoder = json.JSONDecoder()
        data = []
        while raw_json:
            item, pos = decoder.raw_decode(raw_json)
            raw_json = raw_json[pos:].strip()
            data.append(item)

        self.goals = [i["goal"] for i in data]

        if "answer" in data[0]["additional_info"]:
            self.ground_truths = [i["additional_info"]["answer"] for i in data]

        if "ground_truth" in data[0]:
            self.ground_truth = [i["ground_truth"] for i in data]

        if "subgoals" in data[0]:
            self.ground_truth_subgoals = [i["subgoals"] for i in data]

        if "init_config" in data[0]["additional_info"]:
            self.init_configs = [i["additional_info"]["init_config"] for i in data]

        if "goal_type" in data[0]["additional_info"]:
            self.goal_types = [i["additional_info"]["goal_type"] for i in data]

        if "tool" in data[0]["additional_info"]:
            self.tools = [i["additional_info"]["tool"] for i in data]

        self.category = []
        for i in data:
            if "category" in i["additional_info"]:
                self.category.append(i["additional_info"]["category"])
            else:
                self.category.append(i["category"])

    def __len__(self):
        return len(self.goals)
