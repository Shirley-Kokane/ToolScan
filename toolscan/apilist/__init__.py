import json



def load_apilist(env_name, category):
    if env_name == "movie":
        from .movie.movie_list import MOVIE_API
        return MOVIE_API
    if env_name == "weather":
        from .weather.weather_list import WEATHER_API
        return WEATHER_API
    if env_name == "mixed":
        from .mixed.mixed_list import MIXED_API
        return MIXED_API
    if env_name == "patent":
        from .patent.patent_list import PATENT_API
        return PATENT_API
    if env_name == "spaceflight":
        from .spaceflight.spaceflight_list import SPACEFLIGHT_API
        return SPACEFLIGHT_API
    if env_name == "rapidapi":
        if category.startswith("Food"): 
            from .rapidapi.food import RAPID_API
            return RAPID_API[category.replace("Food", "").strip("_")]
        
        if category.startswith("Data"): 
            from .rapidapi.data import RAPID_API
            return RAPID_API[category.replace("Data", "").strip("_")]

        if category.startswith("Entertainment"):
            from .rapidapi.entertainment import RAPID_API
            return RAPID_API[category.replace("Entertainment", "").strip("_")]
        
        if category.startswith("Location"):
            from .rapidapi.location import RAPID_API
            return RAPID_API[category.replace("Location", "").strip("_")]
        
        if category.startswith("Media"): 
            from .rapidapi.media import RAPID_API
            return RAPID_API[category.replace("Media", "").strip("_")]

        if category.startswith("Movies"):
            from .rapidapi.movies import RAPID_API
            return RAPID_API[category.replace("Movies", "").strip("_")]

        if category.startswith("Newsmedia"):
            from .rapidapi.newsmedia import RAPID_API
            return RAPID_API[category.replace("Newsmedia", "").strip("_")]
        
        if category.startswith("Payments"):
            from .rapidapi.payments import RAPID_API
            return RAPID_API[category.replace("Payments", "").strip("_")]
        
        if category.startswith("Social"):
            from .rapidapi.social import RAPID_API
            return RAPID_API[category.replace("Social", "").strip("_")]
        
        if category.startswith("Sports"):
            from .rapidapi.sports import RAPID_API
            return RAPID_API[category.replace("Sports", "").strip("_")]
        
        if category.startswith("Tools"):
            from .rapidapi.tools import RAPID_API
            return RAPID_API[category.replace("Tools", "").strip("_")]
        
        if category.startswith("Transportation"):
            from .rapidapi.transportation import RAPID_API
            return RAPID_API[category.replace("Transportation", "").strip("_")]
        
        if category.startswith("Travel"):
            from .rapidapi.travel import RAPID_API
            return RAPID_API[category.replace("Travel", "").strip("_")]
        
        if category.startswith("VideoImages"):
            from .rapidapi.videoimages import RAPID_API
            return RAPID_API[category.replace("VideoImages", "").strip("_")]
        
        if category.startswith("Weather"):
            from .rapidapi.weather import RAPID_API
            return RAPID_API[category.replace("Weather", "").strip("_")]
        
        return "API LIST NOT FOUND"
    
