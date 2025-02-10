from common.registry import registry
import json
import os


def load_environment(name, config):

    if name == "movie":
        from environment.movie.movie_env import MovieEnv

        env_l = MovieEnv()
        env = env_l.from_config(config)

    if name == "weather":
        from environment.weather.weather_env import WeatherEnv

        env_l = WeatherEnv()
        env = env_l.from_config(config)

    if name == "mixed":
        from environment.mixed.mixed_env import MixedEnv

        env_l = MixedEnv()
        env = env_l.from_config(config)

    if name == "rapidapi":
        from environment.rapidapi.rapidapi_env import RapidapiEnv

        env_l = RapidapiEnv()
        env = env_l.from_config(config)

    if name == "patent":
        from environment.patent.patent_env import PatentapiEnv

        env_l = PatentapiEnv()
        env = env_l.from_config(config)

    if name == "spaceflight":
        from environment.spaceflight.spaceflight_env import SpaceflightEnv

        env_l = SpaceflightEnv()
        env = env_l.from_config(config)

    return env
