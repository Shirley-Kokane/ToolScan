import subprocess
import os
import re
import json
import logging
from environment.base_env import BaseEnvironment
from utils.patent.patent_tools import patentapi_toolkits
from utils.tool.helpers import parse_action

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class PatentapiEnv(BaseEnvironment):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()
        # self.action_path = []
        self.patentapi_toolkits = patentapi_toolkits()
        if not use_dataset:
            self.dataset = None
        else:
            self.dataset = dataset
        self.reset()

    def step(self, action_type, params, action_path=None):
        action_route = None
        if action_path == None:
            action_path = self.action_path

        if "finish" not in action_type and "categories" in params:
            mainl = [
                "patent_abstract",
                "patent_title",
                "patent_number",
                "patent_date",
                "inventor_last_name",
                "patent_abstract",
            ]
            if (
                not set(params["categories"]).issubset(set(mainl))
                or len(params["categories"]) == 0
            ):
                return (
                    "ERROR | Categories not selected from one of the following categories [patent_number,patent_date,patent_title,inventor_last_name, patent_abstract]",
                    False,
                )

        try:

            if action_type == "search_patent_type_and_title_and_date":

                observation = (
                    self.patentapi_toolkits.search_patent_type_and_title_and_date(
                        patent_date=params["patent_date"],
                        patent_titles=params["patent_titles"],
                        patent_type=params["patent_type"],
                        categories=params["categories"],
                        page=params["page"],
                        count=params["count"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_not_patent_type_and_title_and_date":

                observation = (
                    self.patentapi_toolkits.search_not_patent_type_and_title_and_date(
                        patent_date=params["patent_date"],
                        patent_titles=params["patent_titles"],
                        patent_type=params["patent_type"],
                        categories=params["categories"],
                        page=params["page"],
                        count=params["count"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patent_greater_than_equal_to":

                observation = (
                    self.patentapi_toolkits.search_patent_greater_than_equal_to(
                        patent_date=params["patent_date"],
                        categories=params["categories"],
                        page=params["page"],
                        count=params["count"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patent_less_than_equal_to":

                observation = self.patentapi_toolkits.search_patent_less_than_equal_to(
                    patent_date=params["patent_date"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif action_type == "search_patent_less_than_and_greater_than":

                observation = (
                    self.patentapi_toolkits.search_patent_less_than_and_greater_than(
                        _gt=params["_gt"],
                        _lt=params["_lt"],
                        categories=params["categories"],
                        page=params["page"],
                        count=params["count"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patent_less_than_or_greater_than":

                observation = (
                    self.patentapi_toolkits.search_patent_less_than_or_greater_than(
                        _gt=params["_gt"],
                        _lt=params["_lt"],
                        categories=params["categories"],
                        page=params["page"],
                        count=params["count"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patent_lastname_and_less_than_and_greater_than":

                observation = self.patentapi_toolkits.search_patent_lastname_and_less_than_and_greater_than(
                    inventor_last_names=params["inventor_last_names"],
                    _gt=params["_gt"],
                    _lt=params["_lt"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif action_type == "search_patents_lastname_or_title":

                observation = self.patentapi_toolkits.search_patents_lastname_or_title(
                    inventor_last_names=params["inventor_last_names"],
                    patent_titles=params["patent_titles"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif action_type == "search_patents_lastname_and_title":

                observation = self.patentapi_toolkits.search_patents_lastname_and_title(
                    inventor_last_names=params["inventor_last_names"],
                    patent_titles=params["patent_titles"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif action_type == "search_patents_lastname_and_title_and_date":

                observation = (
                    self.patentapi_toolkits.search_patents_lastname_and_title_and_date(
                        inventor_last_names=params["inventor_last_names"],
                        patent_titles=params["patent_titles"],
                        patent_date=params["patent_date"],
                        categories=params["categories"],
                        page=params["page"],
                        count=params["count"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patents_lastname_and_date":

                observation = self.patentapi_toolkits.search_patents_lastname_and_date(
                    inventor_last_names=params["inventor_last_names"],
                    patent_date=params["patent_date"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif (
                action_type == "search_patents_lastname_and_title_and_greater_than_date"
            ):

                observation = self.patentapi_toolkits.search_patents_lastname_and_title_and_greater_than_date(
                    inventor_last_names=params["inventor_last_names"],
                    patent_titles=params["patent_titles"],
                    _gte=params["_gte"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif (
                action_type == "search_patents_lastname_and_title_and_lesser_than_date"
            ):
                observation = self.patentapi_toolkits.search_patents_lastname_and_title_and_lesser_than_date(
                    inventor_last_names=params["inventor_last_names"],
                    patent_titles=params["patent_titles"],
                    _lt=params["_lt"],
                    categories=params["categories"],
                    page=params["page"],
                    count=params["count"],
                    action_path=action_path,
                )

            elif action_type == "finish":
                observation = self.patentapi_toolkits.finish(
                    answer=params["answer"], action_path=action_path
                )

        except Exception as e:
            observation = "ERROR | " + type(e).__name__ + "(" + str(e) + ")"
            done = False
            return observation, self.done  # , None

        done = "Finish" in action_type or "finish" in action_type
        self.done = done

        return str(observation), self.done
