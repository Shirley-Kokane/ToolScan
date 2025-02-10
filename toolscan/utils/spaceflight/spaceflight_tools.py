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


class spacelfightapi_toolkits:
    def __init__(self):
        pass

    @log_path
    def search_spaceflight_articles_with_newssite(
        self, search, news_site, limit, news_site_exclude, offset, ordering
    ):
        """
        Calls the Spaceflight News API to search for articles based on various parameters.

        Args:
            news_site (str): Search for documents with a news_site__name present in a list of comma-separated values. Case insensitive.
            limit (int, optional): Number of results to return per page. Defaults to 10.
            news_site_exclude (str, optional): Search for documents with a news_site__name not present in a list of comma-separated values. Case insensitive. Defaults to None.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/articles?news_site={news_site}"

        if search is not None:
            url += f"&search={search}"
        if limit is not None:
            url += f"&limit={limit}"
        if news_site_exclude is not None:
            url += f"&news_site_exclude={news_site_exclude}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch articles for the given parameters"}

    @log_path
    def search_spaceflight_articles_with_newssite_and_published_date_equal(
        self,
        search,
        news_site,
        limit,
        news_site_exclude,
        published_at_gte,
        published_at_lte,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for articles based on various parameters.

        Args:
            news_site (str): Search for documents with a news_site__name present in a list of comma-separated values. Case insensitive.
            limit (int, optional): Number of results to return per page. Defaults to 10.
            news_site_exclude (str, optional): Search for documents with a news_site__name not present in a list of comma-separated values. Case insensitive. Defaults to None.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/articles?news_site={news_site}"

        if search is not None:
            url += f"&search={search}"
        if published_at_gte is not None:
            published_at_gte = published_at_gte.replace(":", "%3A")
            url += f"&published_at_gte={published_at_gte}"
        if published_at_lte is not None:
            published_at_lte = published_at_lte.replace(":", "%3A")
            url += f"&published_at_lte={published_at_lte}"
        if limit is not None:
            url += f"&limit={limit}"
        if news_site_exclude is not None:
            url += f"&news_site_exclude={news_site_exclude}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch articles for the given parameters"}

    @log_path
    def search_spaceflight_articles_with_newssite_and_published_date_unequal(
        self,
        search,
        news_site,
        limit,
        news_site_exclude,
        published_at_gt,
        published_at_lt,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for articles based on various parameters.

        Args:
            news_site (str): Search for documents with a news_site__name present in a list of comma-separated values. Case insensitive.
            limit (int, optional): Number of results to return per page. Defaults to 10.
            news_site_exclude (str, optional): Search for documents with a news_site__name not present in a list of comma-separated values. Case insensitive. Defaults to None.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/articles?news_site={news_site}"

        if search is not None:
            url += f"&search={search}"
        if published_at_gt is not None:
            published_at_gt = published_at_gt.replace(":", "%3A")
            url += f"&published_at_gt={published_at_gt}"
        if published_at_lt is not None:
            published_at_lt = published_at_lt.replace(":", "%3A")
            url += f"&published_at_lt={published_at_lt}"
        if limit is not None:
            url += f"&limit={limit}"
        if news_site_exclude is not None:
            url += f"&news_site_exclude={news_site_exclude}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch articles for the given parameters"}

    @log_path
    def search_spaceflight_blogs_with_title(
        self,
        title_contains,
        title_contains_all,
        title_contains_one,
        limit,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for blogs based on various parameters.

        Args:
            search (str): Search for documents with a specific phrase in the title or summary.
            title_contains (str, optional): Search for all documents with a specific phrase in the title. Defaults to None.
            title_contains_all (str, optional): Search for documents with a title containing all keywords from comma-separated values. Defaults to None.
            title_contains_one (str, optional): Search for documents with a title containing at least one keyword from comma-separated values. Defaults to None.
            limit (int, optional): Number of results to return per page. Defaults to 10.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/blogs?"

        if title_contains is not None:
            url += f"&title_contains={title_contains}"
        if title_contains_all is not None:
            url += f"&title_contains_all={title_contains_all}"
        if title_contains_one is not None:
            url += f"&title_contains_one={title_contains_one}"
        if limit is not None:
            url += f"&limit={limit}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blogs for the given parameters"}

    @log_path
    def search_spaceflight_blogs_with_title_and_published_date_equal(
        self,
        title_contains,
        title_contains_all,
        title_contains_one,
        published_at_gte,
        published_at_lte,
        limit,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for blogs based on various parameters.

        Args:
            search (str): Search for documents with a specific phrase in the title or summary.
            title_contains (str, optional): Search for all documents with a specific phrase in the title. Defaults to None.
            title_contains_all (str, optional): Search for documents with a title containing all keywords from comma-separated values. Defaults to None.
            title_contains_one (str, optional): Search for documents with a title containing at least one keyword from comma-separated values. Defaults to None.
            limit (int, optional): Number of results to return per page. Defaults to 10.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/blogs?"

        if title_contains is not None:
            url += f"&title_contains={title_contains}"
        if published_at_gte is not None:
            published_at_gte = published_at_gte.replace(":", "%3A")
            url += f"&published_at_gte={published_at_gte}"
        if published_at_lte is not None:
            published_at_lte = published_at_lte.replace(":", "%3A")
            url += f"&published_at_lte={published_at_lte}"
        if title_contains_all is not None:
            url += f"&title_contains_all={title_contains_all}"
        if title_contains_one is not None:
            url += f"&title_contains_one={title_contains_one}"
        if limit is not None:
            url += f"&limit={limit}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blogs for the given parameters"}

    @log_path
    def search_spaceflight_blogs_with_title_and_published_date_unequal(
        self,
        title_contains,
        title_contains_all,
        title_contains_one,
        published_at_gt,
        published_at_lt,
        limit,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for blogs based on various parameters.

        Args:
            search (str): Search for documents with a specific phrase in the title or summary.
            title_contains (str, optional): Search for all documents with a specific phrase in the title. Defaults to None.
            title_contains_all (str, optional): Search for documents with a title containing all keywords from comma-separated values. Defaults to None.
            title_contains_one (str, optional): Search for documents with a title containing at least one keyword from comma-separated values. Defaults to None.
            limit (int, optional): Number of results to return per page. Defaults to 10.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/blogs?"

        if title_contains is not None:
            url += f"&title_contains={title_contains}"
        if published_at_gt is not None:
            published_at_gt = published_at_gt.replace(":", "%3A")
            url += f"&published_at_gt={published_at_gt}"
        if published_at_lt is not None:
            published_at_lt = published_at_lt.replace(":", "%3A")
            url += f"&published_at_lt={published_at_lt}"
        if title_contains_all is not None:
            url += f"&title_contains_all={title_contains_all}"
        if title_contains_one is not None:
            url += f"&title_contains_one={title_contains_one}"
        if limit is not None:
            url += f"&limit={limit}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blogs for the given parameters"}

    @log_path
    def get_spaceflight_news_info(self):
        """
        Calls the Spaceflight News API to retrieve information about the API.

        Returns:
            dict: A dictionary containing the information about the API.
        """
        url = "https://api.spaceflightnewsapi.net/v4/info"
        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch information about the API"}

    @log_path
    def get_spaceflight_article_by_id(self, article_id):
        """
        Calls the Spaceflight News API to retrieve an article based on its ID.

        Args:
            article_id (int): The ID of the article to retrieve.

        Returns:
            dict: A dictionary containing the article information.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/articles?id={article_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch article for the given ID"}

    @log_path
    def get_spaceflight_blog_by_id(self, blog_id):
        """
        Calls the Spaceflight News API to retrieve a blog based on its ID.

        Args:
            blog_id (int): The ID of the blog to retrieve.

        Returns:
            dict: A dictionary containing the blog information.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/blogs?id={blog_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blog for the given ID"}

    @log_path
    def search_spaceflight_reports_with_summary_and_published_date_equal(
        self,
        summary_contains,
        summary_contains_all,
        summary_contains_one,
        published_at_gte,
        published_at_lte,
        limit,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for blogs based on various parameters.

        Args:
            search (str): Search for documents with a specific phrase in the summary.
            summary_contains (str, optional): Search for all documents with a specific phrase in the summary. Defaults to None.
            summary_contains_all (str, optional): Search for documents with a summary containing all keywords from comma-separated values. Defaults to None.
            summary_contains_one (str, optional): Search for documents with a summary containing at least one keyword from comma-separated values. Defaults to None.
            published_at_gt (string, optional): Get all documents published after a given ISO8601 timestamp (excluded).
            published_at_lt (string, optional): Get all documents published before a given ISO8601 timestamp (excluded).
            limit (int, optional): Number of results to return per page. Defaults to 10.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/blogs?"

        if summary_contains is not None:
            url += f"&summary_contains={summary_contains}"
        if summary_contains_all is not None:
            url += f"&summary_contains_all={summary_contains_all}"
        if summary_contains_one is not None:
            url += f"&summary_contains_one={summary_contains_one}"
        if published_at_gte is not None:
            url += f"&published_at_gte={published_at_gte}"
        if published_at_lte is not None:
            url += f"&published_at_lte={published_at_lte}"
        if limit is not None:
            url += f"&limit={limit}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blogs for the given parameters"}

    @log_path
    def search_spaceflight_reports_with_summary_and_published_date_unequal(
        self,
        summary_contains,
        summary_contains_all,
        summary_contains_one,
        published_at_gt,
        published_at_lt,
        limit,
        offset,
        ordering,
    ):
        """
        Calls the Spaceflight News API to search for blogs based on various parameters.

        Args:
            search (str): Search for documents with a specific phrase in the summary.
            summary_contains (str, optional): Search for all documents with a specific phrase in the summary. Defaults to None.
            summary_contains_all (str, optional): Search for documents with a summary containing all keywords from comma-separated values. Defaults to None.
            summary_contains_one (str, optional): Search for documents with a summary containing at least one keyword from comma-separated values. Defaults to None.
            published_at_gt (string, optional): Get all documents published after a given ISO8601 timestamp (excluded).
            published_at_lt (string, optional): Get all documents published before a given ISO8601 timestamp (excluded).
            limit (int, optional): Number of results to return per page. Defaults to 10.
            offset (int, optional): The initial index from which to return the results. Defaults to 0.
            ordering (str, optional): Which field to use when ordering the results. Defaults to None.

        Returns:
            dict: A dictionary containing the search results.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/blogs?"

        if summary_contains is not None:
            url += f"&summary_contains={summary_contains}"
        if summary_contains_all is not None:
            url += f"&summary_contains_all={summary_contains_all}"
        if summary_contains_one is not None:
            url += f"&summary_contains_one={summary_contains_one}"
        if published_at_gt is not None:
            url += f"&published_at_gt={published_at_gt}"
        if published_at_lt is not None:
            url += f"&published_at_lt={published_at_lt}"
        if limit is not None:
            url += f"&limit={limit}"
        if offset is not None:
            url += f"&offset={offset}"
        # if ordering is not None:
        #     url += f"&ordering={ordering}"

        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blogs for the given parameters"}

    @log_path
    def get_spaceflight_report_by_id(self, report_id):
        """
        Calls the Spaceflight News API to retrieve a report based on its ID.

        Args:
            report_id (int): The ID of the report to retrieve.

        Returns:
            dict: A dictionary containing the report information.
        """
        url = f"https://api.spaceflightnewsapi.net/v4/reports?id={report_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, {"error": "Unable to fetch blog for the given ID"}

    @log_path
    def finish(self, answer):
        # if type(answer) == list:
        #     answer = sorted(answer)
        return True, answer
