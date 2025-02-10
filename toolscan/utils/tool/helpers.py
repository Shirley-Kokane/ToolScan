import re
import math
import os
from utils.logging.toollogger import SpecLogger


def extract_action_name_and_action_input(text):
    pattern = r"Action:\s*(.*?)\s*with\s*Action Input:\s*(.*?)$"  # r"\s*(.*?)\s*with\s*Action Input:\s*(.*?)$"
    match = re.search(pattern, text)
    if not match:
        pattern = r"\s*(.*?)\s*with\s*Action Input:\s*(.*?)$"
        match = re.search(pattern, text)

    if match:
        action = match.group(1)
        action_input = match.group(2)
        return action, action_input
    else:
        return None, None


def parse_action(string):
    pattern = r"Action:\s*(.*?)\s*with\s*Action Input:\s*(.*?)$"
    match = re.match(pattern, string)

    if match:
        action_type = match.group(1)
        params = match.group(2)

        if "}" != params[-1]:
            params += '"}'
        try:
            params = eval(params)
        except:

            raise Exception("Incorrect Format Error")
        return action_type, params

    else:
        return None


def check_credentials():
    if "MOVIE_KEY" not in os.environ:
        raise Exception("Please set MOVIE_KEY in `.env` .")

    PROJECT_PATH = os.getenv("PROJECT_PATH")


def contains_network_error(observation):
    network_errors = [
        "ConnectionError",
        "HTTPError",
        "HTTPSError",
        "TimeoutError",
        "SSLError",
        "ProxyError",
        "TooManyRedirects",
        "RequestException",
    ]

    for error in network_errors:
        if error in observation:
            return True

    return False


def save_log(logger_name, task_name, output_dir):
    """Creates a log file and logging object for the corresponding task Name"""
    log_dir = os.path.join(output_dir, "trajectory")
    os.makedirs(log_dir, exist_ok=True)
    log_file_name = f"{task_name}.log"
    log_file_path = os.path.join(log_dir, log_file_name)
    logger = SpecLogger(logger_name, filepath=log_file_path)
    return logger
