import subprocess
import os
import re
import json
import logging
from environment.base_env import BaseEnvironment
from utils.movie.movie_tools import movie_toolkits
from utils.tool.helpers import parse_action

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class MovieEnv(BaseEnvironment):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()
        self.movie_toolkits = movie_toolkits()

    def step(self, action_type, params, action_path=None):

        if action_path == None:
            action_path = self.action_path

        try:
            if action_type == "get_search_movie":

                observation = self.movie_toolkits.get_search_movie(
                    movie_name=params["movie_name"], action_path=action_path
                )

            elif action_type == "get_movie_details":

                observation = self.movie_toolkits.get_movie_details(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_movie_production_companies":

                observation = self.movie_toolkits.get_movie_production_companies(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_movie_production_countries":

                observation = self.movie_toolkits.get_movie_production_countries(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_movie_keywords":

                observation = self.movie_toolkits.get_movie_keywords(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_search_person":

                observation = self.movie_toolkits.get_search_person(
                    person_name=params["person_name"], action_path=action_path
                )

            elif action_type == "get_person_details":

                observation = self.movie_toolkits.get_person_details(
                    person_id=params["person_id"], action_path=action_path
                )

            elif action_type == "get_movie_cast":

                observation = self.movie_toolkits.get_movie_cast(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_movie_crew":

                observation = self.movie_toolkits.get_movie_crew(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_person_cast":

                observation = self.movie_toolkits.get_person_cast(
                    person_id=params["person_id"], action_path=action_path
                )

            elif action_type == "get_person_crew":

                observation = self.movie_toolkits.get_person_crew(
                    person_id=params["person_id"], action_path=action_path
                )

            elif action_type == "get_person_external_ids":

                observation = self.movie_toolkits.get_person_external_ids(
                    person_id=params["person_id"], action_path=action_path
                )

            elif action_type == "get_movie_alternative_titles":

                observation = self.movie_toolkits.get_movie_alternative_titles(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "get_movie_translation":

                observation = self.movie_toolkits.get_movie_translation(
                    movie_id=params["movie_id"], action_path=action_path
                )

            elif action_type == "finish":
                observation = self.movie_toolkits.finish(
                    answer=params["answer"], action_path=action_path
                )
            elif action_type == "check_valid_actions":
                observation = "You can use following valid actions: {}".format(
                    self.get_action_space(with_input=False)
                )

        except Exception as e:
            observation = "ERROR | " + type(e).__name__ + "(" + str(e) + ")"
            done = False
            return observation, self.done  # , None

        done = "Finish" in action_type or "finish" in action_type
        self.done = done

        return str(observation), self.done
