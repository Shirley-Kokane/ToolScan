import subprocess
import os
import re
import json
import logging
from environment.base_env import BaseEnvironment
from utils.mixed.mixed_tools import mixedapi_toolkits
from utils.tool.helpers import parse_action

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class MixedEnv(BaseEnvironment):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()

        self.mixedapi_toolkits = mixedapi_toolkits()

    def step(self, action_type, params, action_path=None):

        if action_path == None:
            action_path = self.action_path

        try:
            if action_type == "validate_single_email":

                observation = self.mixedapi_toolkits.validate_single_email(
                    email=params["email"], action_path=action_path
                )

            elif action_type == "validate_multiple_emails":

                observation = self.mixedapi_toolkits.validate_multiple_emails(
                    emails=params["emails"], action_path=action_path
                )

            elif action_type == "get_random_advice":
                observation = self.mixedapi_toolkits.get_random_advice(
                    action_path=action_path
                )

            elif action_type == "get_advice_on_query":

                observation = self.mixedapi_toolkits.get_advice_on_query(
                    query=params["query"], action_path=action_path
                )

            elif action_type == "search_patent_greater_than_equal_to":

                observation = (
                    self.mixedapi_toolkits.search_patent_greater_than_equal_to(
                        patent_date=params["patent_date"], action_path=action_path
                    )
                )

            elif action_type == "search_patent_less_than_equal_to":

                observation = self.mixedapi_toolkits.search_patent_less_than_equal_to(
                    patent_date=params["patent_date"], action_path=action_path
                )

            elif action_type == "search_patent_less_than_and_greater_than":

                observation = (
                    self.mixedapi_toolkits.search_patent_less_than_and_greater_than(
                        start_date=params["start_date"],
                        end_date=params["end_date"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patent_less_than_or_greater_than":

                observation = (
                    self.mixedapi_toolkits.search_patent_less_than_or_greater_than(
                        start_date=params["start_date"],
                        end_date=params["end_date"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patents_lastname_or_title":

                observation = self.mixedapi_toolkits.search_patents_lastname_or_title(
                    inventor_last_names=params["inventor_last_names"],
                    patent_titles=params["patent_titles"],
                    action_path=action_path,
                )

            elif action_type == "search_patents_lastname_and_title":

                observation = self.mixedapi_toolkits.search_patents_lastname_and_title(
                    inventor_last_names=params["inventor_last_names"],
                    patent_titles=params["patent_titles"],
                    action_path=action_path,
                )

            elif action_type == "search_patent_lastname_and_less_than_and_greater_than":

                observation = self.mixedapi_toolkits.search_patent_lastname_and_less_than_and_greater_than(
                    inventor_last_names=params["inventor_last_names"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )

            elif action_type == "search_patents_lastname_and_title_and_date":

                observation = (
                    self.mixedapi_toolkits.search_patents_lastname_and_title_and_date(
                        inventor_last_names=params["inventor_last_names"],
                        patent_titles=params["patent_titles"],
                        patent_date=params["patent_date"],
                        action_path=action_path,
                    )
                )

            elif action_type == "search_patents_lastname_and_date":

                observation = self.mixedapi_toolkits.search_patents_lastname_and_date(
                    last_name=params["inventor_last_names"],
                    patent_date=params["patent_date"],
                    action_path=action_path,
                )

            elif action_type == "search_spaceflight_news":

                observation = self.mixedapi_toolkits.search_spaceflight_news(
                    news_site=params["news_site"],
                    news_site_exclude=params.get("news_site_exclude", None),
                    limit=params.get("limit", 10),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif action_type == "search_spaceflight_blogs":

                observation = self.mixedapi_toolkits.search_spaceflight_blogs(
                    search=params["search"],
                    title_contains=params.get("title_contains", None),
                    title_contains_all=params.get("title_contains_all", None),
                    title_contains_one=params.get("title_contains_one", None),
                    limit=params.get("limit", 10),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif action_type == "get_spaceflight_news_info":
                observation = self.mixedapi_toolkits.get_spaceflight_news_info(
                    action_path=action_path
                )

            elif action_type == "get_spaceflight_article_by_id":

                observation = self.mixedapi_toolkits.get_spaceflight_article_by_id(
                    article_id=params["article_id"], action_path=action_path
                )

            elif action_type == "get_spaceflight_blog_by_id":

                observation = self.mixedapi_toolkits.get_spaceflight_blog_by_id(
                    blog_id=params["blog_id"], action_path=action_path
                )

            elif action_type == "get_spaceflight_report_by_id":

                observation = self.mixedapi_toolkits.get_spaceflight_report_by_id(
                    report_id=params["report_id"], action_path=action_path
                )

            elif action_type == "search_spaceflight_reports":

                observation = self.mixedapi_toolkits.search_spaceflight_reports(
                    search=params["search"],
                    summary_contains=params.get("summary_contains", None),
                    summary_contains_all=params.get("summary_contains_all", None),
                    summary_contains_one=params.get("summary_contains_one", None),
                    limit=params.get("limit", 10),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif action_type == "finish":
                observation = self.mixedapi_toolkits.finish(
                    answer=params["answer"], action_path=action_path
                )

        except Exception as e:
            observation = "ERROR | " + type(e).__name__ + "(" + str(e) + ")"
            done = False
            return observation, self.done  # , None

        done = "Finish" in action_type or "finish" in action_type
        self.done = done

        return str(observation), self.done
