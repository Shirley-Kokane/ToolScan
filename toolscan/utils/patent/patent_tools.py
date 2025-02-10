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
                action_path.append({
                    "Action" : func.__name__,
                    "Action Input" : str(kwargs),
                    "Observation": result,
                    "Subgoal": clean_observation(result) 
                })
                return result
            else:
                action_path.append({
                    "Action" : func.__name__,
                    "Action Input" : str(kwargs),
                    "Observation": result,
                    "Subgoal": "Calling " + func.__name__ + " with " + str(kwargs) + " failed",
                })
                return result
        else:
            return func(*args, **kwargs)
    return wrapper


class patentapi_toolkits:
    def __init__(self):
        pass
    
    @log_path
    def search_patent_type_and_title_and_date(self,patent_date , patent_titles,patent_type,categories,page,count ):
        """
        Retrieve patents with dates, titles, patent type, categories using the PatentsView API.

        Parameters:
        patent_date (str): The date to compare patents against. Format should be 'YYYY-MM-DD'.
        patent_titles (list): A list of terms to search for in patent titles.
        patent_type (str): A string representing which patent type.
        categories (str): Representing what entities to retrieve from the API, [patent_number,patent_date,patent_title,inventor_last_name, patent_abstract]
        page (int): Page number to retrieve the patents from
        count (int): No. of patents to retreive using the PatentsView API

        Returns:
        dict: The response from the PatentsView API containing patents with a date greater than or equal to the specified date.
        """
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_and":[{"_gte": {"patent_date": patent_date}}, {"patent_type": patent_type}, {"_text_any": {"patent_title": patent_titles}}]}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
    
    
    @log_path
    def search_not_patent_type_and_title_and_date(self,patent_date, patent_titles,patent_type,categories,page,count ):
        """
        Retrieve patents with dates, titles and not including patent type using the PatentsView API.

        Parameters:
        patent_date (str): The date to compare patents against. Format should be 'YYYY-MM-DD'.
        patent_titles (list): A list of terms to search for in patent titles.
        patent_type (str): A string representing which patent type.
        categories (str): Representing what entities to retrieve from the API, [patent_number,patent_date,patent_title,inventor_last_name, patent_abstract]
        page (int): Page number to retrieve the patents from
        count (int): No. of patents to retreive using the PatentsView API

        Returns:
        dict: The response from the PatentsView API containing patents with a date greater than or equal to the specified date.
        """
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_and":[{"_gte": {"patent_date": patent_date}}, { "_not": {"patent_type": patent_type}}, {"_text_any": {"patent_title": patent_titles}}]}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
        
    
    
    @log_path
    def search_patent_greater_than_equal_to(self,patent_date, categories, page, count):
        """
        Retrieve patents with a date greater than or equal to the specified date.

        Parameters:
        patent_date (str): The date to compare patents against. Format should be 'YYYY-MM-DD'.

        Returns:
        dict: The response from the PatentsView API containing patents with a date greater than or equal to the specified date.
        """
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_gte": {"patent_date": patent_date}}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
    
    @log_path
    def search_patent_less_than_equal_to(self,patent_date,categories, page, count):
        """
        Retrieve patents with a date less than or equal to the specified date.

        Parameters:
        patent_date (str): The date to compare patents against. Format should be 'YYYY-MM-DD'.

        Returns:
        dict: The response from the PatentsView API containing patents with a date less than or equal to the specified date.
        """
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_lte": {"patent_date": patent_date}}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
        
    @log_path
    def search_patent_less_than_and_greater_than(self,_gt, _lt,categories, page, count):
    
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_and" : [{"_lte": {"patent_date": _lt}}, {"_gte": {"patent_date": _gt}}]}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
    
    @log_path
    def search_patent_less_than_or_greater_than(self,_gt, _lt,categories, page, count):
    
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_or" : [{"_lte": {"patent_date": _gt}}, {"_gte": {"patent_date": _lt}}]}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
        
    @log_path
    def search_patent_lastname_and_less_than_and_greater_than(self,inventor_last_names,_gt, _lt,categories, page, count):
    
        url = "https://api.patentsview.org/patents/query?q="
        query = {"_and" : [{"_lte":{"patent_date": _lt}}, {"_gte": {"patent_date": _gt}}, {"inventor_last_name": inventor_last_names}]}
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}

    @log_path
    def search_patents_lastname_or_title(self,inventor_last_names, patent_titles,categories, page, count):
        """
        Calls the PatentsView API to search for patents based on inventor last names and patent titles.

        Args:
            inventor_last_names (list of str): A list of inventor last names to search for.
            patent_titles (list of str): A list of terms to search for in patent titles.

        Returns:
            dict: A dictionary containing the search results.
        """
        query = {
            "_or": [
                {"inventor_last_name": inventor_last_names},
                {"_text_any": {"patent_title": " ".join(patent_titles)}}
            ]
        }
        url = f"https://api.patentsview.org/patents/query?q="
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
    
    @log_path
    def search_patents_lastname_and_title(self,inventor_last_names, patent_titles,categories, page, count):
        """
        Calls the PatentsView API to search for patents based on inventor last names and patent titles.

        Args:
            inventor_last_names (list of str): A list of inventor last names to search for.
            patent_titles (list of str): A list of terms to search for in patent titles.

        Returns:
            dict: A dictionary containing the search results.
        """
        query = {
            "_and": [
                {"inventor_last_name": inventor_last_names},
                {"_text_any": {"patent_title": " ".join(patent_titles)}}
            ]
        }
        url = f"https://api.patentsview.org/patents/query?q="
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
    
    @log_path
    def search_patents_lastname_and_title_and_date(self,inventor_last_names, patent_titles, patent_date,categories, page, count):
        """
        Calls the PatentsView API to search for patents based on inventor last names and patent titles.

        Args:
            inventor_last_names (list of str): A list of inventor last names to search for.
            patent_titles (list of str): A list of terms to search for in patent titles.

        Returns:
            dict: A dictionary containing the search results.
        """
        query = {
            "_and": [
                {"inventor_last_name": inventor_last_names},
                {"_gt" : {"patent_date": patent_date}},
                {"_text_any": {"patent_title": " ".join(patent_titles)}}
            ]
        }
        url = f"https://api.patentsview.org/patents/query?q="
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}

    @log_path
    def search_patents_lastname_and_date(self,inventor_last_names, patent_date,categories, page, count):
        """
        Calls the PatentsView API to search for patents based on inventor last name and patent date.

        Args:
            last_name (str): The inventor's last name to search for.
            patent_date (str): The patent grant date to search for in the format YYYY-MM-DD.

        Returns:
            dict: A dictionary containing the search results.
        """
        query = {
            "_and": [
                {"inventor_last_name": inventor_last_names},
                {"_gt" : {"patent_date": patent_date}}
            ]
        }
        url = f"https://api.patentsview.org/patents/query?q="
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
        
    
    @log_path
    def search_patents_lastname_and_title_and_greater_than_date(self,inventor_last_names, _gte, patent_titles,categories, page, count):
        """
        Search for patents using the PatentsView API based on inventor last name and patent date.

        Args:
            inventor_last_names (str): The inventor's last name to search for.
            _gt (str): 
            patent_date (str): The patent grant date to search for in the format YYYY-MM-DD.

        Returns:
            dict: A dictionary containing the search results.
        """
        query = {
            "_and": [
                {"inventor_last_name": inventor_last_names},
                {"_gte" : {"patent_date": _gte}},
                {"_text_any": {"patent_title": " ".join(patent_titles)}}
                 
            ]
        }
        
        url = f"https://api.patentsview.org/patents/query?q="
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        
        num_tries = 5
        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
    
    
    @log_path
    def search_patents_lastname_and_title_and_lesser_than_date(self, inventor_last_names, _lt, patent_titles,categories, page, count):
        """
        Search for patents using the PatentsView API based on inventor last name and patent date.

        Args:
            last_name (list): The inventor's last name to search for.
            _lt (str): 
            patent_date (str): The patent grant date to search for in the format YYYY-MM-DD.

        Returns:
            dict: A dictionary containing the search results.
        """
        query = {
            "_and": [
                {"inventor_last_name": inventor_last_names},
                {"_lt" : {"patent_date": _lt}},
                {"_text_any": {"patent_title": " ".join(patent_titles)}}
                 
            ]
        }
        
        url = f"https://api.patentsview.org/patents/query?q="
        misc = "&f="+ json.dumps(categories)  + "&o=" + json.dumps({"matched_subentities_only": "true", "page": page, "per_page": count, "include_subentity_total_counts": "false"})
        mainurl = url + json.dumps(query) + misc
        
        num_tries = 5

        for trial_index in range(num_tries):  
            response = requests.get(mainurl)
            if response.status_code == 200:
                return True, response.json()
        return False, {"error": "Unable to fetch patents for the given query"}
        
    @log_path
    def finish(self, answer):
        
        return True, answer
        
    
    