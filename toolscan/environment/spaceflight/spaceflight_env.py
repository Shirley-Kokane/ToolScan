import subprocess
import os
import re
import json
import logging
from environment.base_env import BaseEnvironment
from utils.spaceflight.spaceflight_tools import spacelfightapi_toolkits
from utils.tool.helpers import parse_action

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class SpaceflightEnv(BaseEnvironment):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()
        self.spacelfightapi_toolkits = spacelfightapi_toolkits()

    def step(self, action_type, params, action_path=None):

        if action_path == None:
            action_path = self.action_path

        try:
            if action_type == "search_spaceflight_articles_with_newssite":

                observation = self.spacelfightapi_toolkits.search_spaceflight_articles_with_newssite(
                    search=params.get("search", None),
                    news_site=params["news_site"],
                    news_site_exclude=params.get("news_site_exclude", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif (
                action_type
                == "search_spaceflight_articles_with_newssite_and_published_date_equal"
            ):

                observation = self.spacelfightapi_toolkits.search_spaceflight_articles_with_newssite_and_published_date_equal(
                    search=params.get("search", None),
                    news_site=params["news_site"],
                    news_site_exclude=params.get("news_site_exclude", None),
                    published_at_gte=params.get("published_at_gte", None),
                    published_at_lte=params.get("published_at_lte", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif (
                action_type
                == "search_spaceflight_articles_with_newssite_and_published_date_unequal"
            ):

                observation = self.spacelfightapi_toolkits.search_spaceflight_articles_with_newssite_and_published_date_unequal(
                    search=params.get("search", None),
                    news_site=params["news_site"],
                    news_site_exclude=params.get("news_site_exclude", None),
                    published_at_gt=params.get("published_at_gt", None),
                    published_at_lt=params.get("published_at_lt", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif action_type == "search_spaceflight_blogs_with_title":

                observation = (
                    self.spacelfightapi_toolkits.search_spaceflight_blogs_with_title(
                        title_contains=params.get("title_contains", None),
                        title_contains_all=params.get("title_contains_all", None),
                        title_contains_one=params.get("title_contains_one", None),
                        limit=params.get("limit", 2),
                        offset=params.get("offset", 0),
                        ordering=params.get("ordering", None),
                        action_path=action_path,
                    )
                )

            elif (
                action_type
                == "search_spaceflight_blogs_with_title_and_published_date_equal"
            ):

                observation = self.spacelfightapi_toolkits.search_spaceflight_blogs_with_title_and_published_date_equal(
                    title_contains=params.get("title_contains", None),
                    title_contains_all=params.get("title_contains_all", None),
                    title_contains_one=params.get("title_contains_one", None),
                    published_at_gte=params.get("published_at_gte", None),
                    published_at_lte=params.get("published_at_lte", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif (
                action_type
                == "search_spaceflight_blogs_with_title_and_published_date_unequal"
            ):

                observation = self.spacelfightapi_toolkits.search_spaceflight_blogs_with_title_and_published_date_unequal(
                    title_contains=params.get("title_contains", None),
                    title_contains_all=params.get("title_contains_all", None),
                    title_contains_one=params.get("title_contains_one", None),
                    published_at_gt=params.get("published_at_gt", None),
                    published_at_lt=params.get("published_at_lt", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif action_type == "get_spaceflight_news_info":
                observation = self.spacelfightapi_toolkits.get_spaceflight_news_info(
                    action_path=action_path
                )

            elif action_type == "get_spaceflight_article_by_id":

                observation = (
                    self.spacelfightapi_toolkits.get_spaceflight_article_by_id(
                        article_id=params["article_id"], action_path=action_path
                    )
                )

            elif action_type == "get_spaceflight_blog_by_id":

                observation = self.spacelfightapi_toolkits.get_spaceflight_blog_by_id(
                    blog_id=params["blog_id"], action_path=action_path
                )

            elif action_type == "get_spaceflight_report_by_id":

                observation = self.spacelfightapi_toolkits.get_spaceflight_report_by_id(
                    report_id=params["report_id"], action_path=action_path
                )

            elif (
                action_type
                == "search_spaceflight_reports_with_summary_and_published_date_equal"
            ):

                observation = self.spacelfightapi_toolkits.search_spaceflight_reports_with_summary_and_published_date_equal(
                    summary_contains=params.get("summary_contains", None),
                    summary_contains_all=params.get("summary_contains_all", None),
                    summary_contains_one=params.get("summary_contains_one", None),
                    published_at_gte=params.get("published_at_gte", None),
                    published_at_lte=params.get("published_at_lte", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif (
                action_type
                == "search_spaceflight_reports_with_summary_and_published_date_unequal"
            ):

                observation = self.spacelfightapi_toolkits.search_spaceflight_reports_with_summary_and_published_date_unequal(
                    summary_contains=params.get("summary_contains", None),
                    summary_contains_all=params.get("summary_contains_all", None),
                    summary_contains_one=params.get("summary_contains_one", None),
                    published_at_gt=params.get("published_at_gt", None),
                    published_at_lt=params.get("published_at_lt", None),
                    limit=params.get("limit", 2),
                    offset=params.get("offset", 0),
                    ordering=params.get("ordering", None),
                    action_path=action_path,
                )

            elif action_type == "finish":
                observation = self.spacelfightapi_toolkits.finish(
                    answer=params["answer"], action_path=action_path
                )

        except Exception as e:
            observation = "ERROR | " + type(e).__name__ + "(" + str(e) + ")"
            done = False
            return observation, self.done  # , None

        done = "Finish" in action_type or "finish" in action_type
        self.done = done

        return str(observation), self.done
