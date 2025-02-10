import subprocess
import os
import re
import json
import logging
from environment.base_env import BaseEnvironment
from utils.weather.weather_tools import weather_toolkits
from utils.tool.helpers import parse_action, is_same_location

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class WeatherEnv(BaseEnvironment):
    def __init__(self, dataset=None, use_dataset=True):
        super().__init__()

        self.weather_toolkits = weather_toolkits()

    def step(self, action_type, params, action_path=None):

        if action_path == None:
            action_path = self.action_path

        try:
            if action_type == "get_user_current_date":
                observation = self.weather_toolkits.get_user_current_date(
                    action_path=action_path
                )
            elif action_type == "get_user_current_location":
                observation = self.weather_toolkits.get_user_current_location(
                    action_path=action_path
                )
            elif action_type == "get_historical_temp":
                observation = self.weather_toolkits.get_historical_temp(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_historical_rain":
                observation = self.weather_toolkits.get_historical_rain(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_historical_snow":
                observation = self.weather_toolkits.get_historical_snow(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_snow_forecast":
                observation = self.weather_toolkits.get_snow_forecast(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_current_snow":
                observation = self.weather_toolkits.get_current_snow(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    current_date=params["current_date"],
                    action_path=action_path,
                )
            elif action_type == "get_current_temp":
                observation = self.weather_toolkits.get_current_temp(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    current_date=params["current_date"],
                    action_path=action_path,
                )
            elif action_type == "get_latitude_longitude":
                observation = self.weather_toolkits.get_latitude_longitude(
                    name=params["name"], action_path=action_path
                )

            elif action_type == "get_elevation":
                observation = self.weather_toolkits.get_elevation(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    action_path=action_path,
                )
            elif action_type == "get_temp_forecast":
                observation = self.weather_toolkits.get_temp_forecast(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_rain_forecast":
                observation = self.weather_toolkits.get_rain_forecast(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_current_rain":
                observation = self.weather_toolkits.get_current_rain(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    current_date=params["current_date"],
                    action_path=action_path,
                )
            elif action_type == "get_distance":
                observation = self.weather_toolkits.get_distance(
                    latitude1=params["latitude1"],
                    longitude1=params["longitude1"],
                    latitude2=params["latitude2"],
                    longitude2=params["longitude2"],
                    action_path=action_path,
                )
            elif action_type == "get_historical_air_quality_index":
                observation = self.weather_toolkits.get_historical_air_quality_index(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    start_date=params["start_date"],
                    end_date=params["end_date"],
                    action_path=action_path,
                )
            elif action_type == "get_current_air_quality_index":
                observation = self.weather_toolkits.get_current_air_quality_index(
                    latitude=params["latitude"],
                    longitude=params["longitude"],
                    current_date=params["current_date"],
                    action_path=action_path,
                )
            elif action_type == "get_air_quality_level":
                observation = self.weather_toolkits.get_air_quality_level(
                    air_quality_index=params["air_quality_index"],
                    action_path=action_path,
                )
            elif action_type == "convert_zipcode_to_address":
                observation = self.weather_toolkits.convert_zipcode_to_address(
                    zipcode=params["zipcode"], action_path=action_path
                )
            elif action_type == "finish":
                observation = self.weather_toolkits.finish(
                    answer=params["answer"], action_path=action_path
                )
            elif action_type == "check_valid_actions":
                observation = "You can use following valid actions: {}".format(
                    self.get_action_space(with_input=False)
                )
            else:
                observation = "ERROR | Invalid action: {}".format(action_type)
        except Exception as e:
            observation = "ERROR | " + type(e).__name__ + "(" + str(e) + ")"
            done = False
            return observation, self.reward, self.done, None

        done = "Finish" in action_type or "finish" in action_type
        self.done = done

        return str(observation), self.done
