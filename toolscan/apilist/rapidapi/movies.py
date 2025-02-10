RAPID_API = {
    "MOVIESDATABASE_API": {
        "titles_id_crew_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "Imdb Id of title ex: tt0000002",
                    "default": "",
                    "required": True,
                }
            },
        },
        "titles_series_seriesid_season_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "season": {
                    "type": "STRING",
                    "description": "Season number",
                    "default": "",
                    "required": True,
                },
                "seriesId": {
                    "type": "STRING",
                    "description": "Series Imdb Id",
                    "default": "",
                    "required": True,
                },
            },
        },
        "titles_episode_id_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "Episode Imdb Id",
                    "default": "",
                    "required": True,
                },
                "info": {
                    "type": "STRING",
                    "description": "Info type structure (default: mini-info) -> base_info / mini_info / image / ...",
                    "default": "",
                    "required": False,
                },
            },
        },
        "titles_id_main_actors_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "Imdb Id of title ex: tt0000002",
                    "default": "",
                    "required": True,
                }
            },
        },
        "titles_x_titles_by_ids_for_moviesdatabase": {
            "description": "Titles by ids list",
            "parameters": {
                "idsList": {
                    "type": "STRING",
                    "description": "Imdb id's comma separated -> tt0001702,tt0001856,tt0001856 ...",
                    "default": "",
                    "required": True,
                },
                "list": {
                    "type": "STRING",
                    "description": "Selected list -> most_pop_movies / most_pop_series / top_rated_series_250 / ...",
                    "default": "",
                    "required": False,
                },
                "info": {
                    "type": "STRING",
                    "description": "Info type structure (default: mini-info) -> base_info / mini_info / image / ...",
                    "default": "",
                    "required": False,
                },
            },
        },
        "titles_id_aka_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "Imdb Id of title ex: tt0000002",
                    "default": "",
                    "required": True,
                }
            },
        },
        "titles_random_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "startYear": {
                    "type": "NUMBER",
                    "description": "Year range filter -from- ex: ?startYear=2020",
                    "default": "",
                    "required": False,
                },
                "genre": {
                    "type": "STRING",
                    "description": "Year filter ex: ?genre=Drama",
                    "default": "",
                    "required": False,
                },
                "titleType": {
                    "type": "STRING",
                    "description": "Filter by type of title",
                    "default": "",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Add sorting (incr, decr) -> year.incr /year.decr",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Number of titles per page (default: 10) -> 10 max ",
                    "default": "",
                    "required": False,
                },
                "info": {
                    "type": "STRING",
                    "description": "Info type structure (default: mini-info) -> base_info / mini_info / image / ...",
                    "default": "",
                    "required": False,
                },
                "endYear": {
                    "type": "NUMBER",
                    "description": "Year range filter -to- ex: ?endYear=2020",
                    "default": "",
                    "required": False,
                },
                "year": {
                    "type": "NUMBER",
                    "description": "Year filter ex: ?year=2020",
                    "default": "",
                    "required": False,
                },
                "list": {
                    "type": "STRING",
                    "description": "Selected list -> most_pop_movies / most_pop_series / top_rated_series_250 / ...",
                    "default": "",
                    "required": False,
                },
            },
        },
        "titles_id_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "Imdb Id of title ex: tt0000002",
                    "default": "",
                    "required": True,
                },
                "info": {
                    "type": "STRING",
                    "description": "Info type structure (default: base-info) -> base_info / mini_info / image / ...",
                    "default": "",
                    "required": False,
                },
            },
        },
        "titles_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "genre": {
                    "type": "STRING",
                    "description": "Year filter ex: ?genre=Drama",
                    "default": "",
                    "required": False,
                },
                "startYear": {
                    "type": "NUMBER",
                    "description": "Year range filter -from- ex: ?startYear=2020",
                    "default": "",
                    "required": False,
                },
                "titleType": {
                    "type": "STRING",
                    "description": "Filter by type of title",
                    "default": "",
                    "required": False,
                },
                "list": {
                    "type": "STRING",
                    "description": "Selected list -> most_pop_movies / most_pop_series / top_rated_series_250 / ...",
                    "default": "",
                    "required": False,
                },
                "year": {
                    "type": "NUMBER",
                    "description": "Year filter ex: ?year=2020",
                    "default": "",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Add sorting (incr, decr) -> year.incr /year.decr",
                    "default": "",
                    "required": False,
                },
                "page": {
                    "type": "STRING",
                    "description": "Page number",
                    "default": "",
                    "required": False,
                },
                "info": {
                    "type": "STRING",
                    "description": "Info type structure (default: mini-info) -> base_info / mini_info / image / ...",
                    "default": "",
                    "required": False,
                },
                "endYear": {
                    "type": "NUMBER",
                    "description": "Year range filter -to- ex: ?endYear=2020",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Number of titles per page (default: 10) -> 10 max ",
                    "default": "",
                    "required": False,
                },
            },
        },
        "titles_seasons_seriesid_for_moviesdatabase": {
            "description": " ",
            "parameters": {
                "seriesId": {
                    "type": "STRING",
                    "description": "Series Imdb Id",
                    "default": "",
                    "required": True,
                }
            },
        },
        "finish": {
            "description": "Return an answer and finish the task",
            "parameters": {
                "answer": {
                    "type": ["string", "number", "array"],
                    "description": "The answer to be returned",
                    "required": True,
                }
            },
        },
    },
    "OTTDETAILS_API": {
        "advanced_search_for_ott_details": {
            "description": "This endpoint allows you to search for a movie or tvshow based on various parameters such as release year , imdb rating , genre , language etc.",
            "parameters": {
                "start_year": {
                    "type": "NUMBER",
                    "description": "Enter any year between 1970 to 2020 to get results.",
                    "default": "1970",
                    "required": False,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": False,
                },
                "max_imdb": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "7.8",
                    "required": False,
                },
                "type": {
                    "type": "STRING",
                    "description": "Enter type 'movie' or 'show'",
                    "default": "movie",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Enter values highestrated , lowestrated , latest , oldest to  sort results accodingly .",
                    "default": "latest",
                    "required": False,
                },
                "min_imdb": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "6",
                    "required": False,
                },
                "genre": {
                    "type": "STRING",
                    "description": "use comma seperated values to enter multiple genre eg : action,horror",
                    "default": "action",
                    "required": False,
                },
                "language": {
                    "type": "STRING",
                    "description": "use comma seperated values to enter multiple values , eg : english,german",
                    "default": "english",
                    "required": False,
                },
                "end_year": {
                    "type": "NUMBER",
                    "description": "Enter any year from 1970 to 2020 to  get results.",
                    "default": "2020",
                    "required": False,
                },
            },
        },
        "basic_info_for_ott_details": {
            "description": "Get info on a  cast such as name , profession , birth and death year , bio , poster , best titles  etc.",
            "parameters": {
                "peopleid": {
                    "type": "STRING",
                    "description": "",
                    "default": "nm0000375",
                    "required": True,
                }
            },
        },
        "params_for_ott_details": {
            "description": "Get array of values that can be used as params in Advanced Search .",
            "parameters": {
                "param": {
                    "type": "STRING",
                    "description": "input 'genre' or 'language' to get array of genre or languages that can be used as filter in advanced search .",
                    "default": "genre",
                    "required": True,
                }
            },
        },
        "search_for_ott_details": {
            "description": "This endpoint allows you to search for a movie or tvshow based on the given 'title '.",
            "parameters": {
                "title": {
                    "type": "STRING",
                    "description": "",
                    "default": "Endgame",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "*Maximum number of pages returned is 10 ",
                    "default": "1",
                    "required": False,
                },
            },
        },
        "title_details_for_ott_details": {
            "description": "Get basic information on a movie or tv show such as imdbid , title , genre , runtime , imdbrating , language , synopsis , type , imageurl  , Streaming platforms info etc.",
            "parameters": {
                "imdbid": {
                    "type": "STRING",
                    "description": "",
                    "default": "tt9904802",
                    "required": True,
                }
            },
        },
        "additional_title_details_for_ott_details": {
            "description": "Get  additional details for a movie or tv show like reviews  , quotes , plotsummary , number of votes , trailer url  , cast details etc.",
            "parameters": {
                "imdbid": {
                    "type": "STRING",
                    "description": "",
                    "default": "tt7286456",
                    "required": True,
                }
            },
        },
        "ott_providers_for_ott_details": {
            "description": "Get  information on OTT platforms we suuport .",
            "parameters": {
                "region": {
                    "type": "STRING",
                    "description": "currently only USA and India region is supported enter param 'US' for USA and 'IN' for India.",
                    "default": "IN",
                    "required": True,
                }
            },
        },
        "new_arrivals_for_ott_details": {
            "description": "Get the latest arrivals from different platforms .",
            "parameters": {
                "region": {
                    "type": "STRING",
                    "description": "Use 'IN' for India and 'US' for USA , * currently we support only US and Indian region.",
                    "default": "US",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": False,
                },
            },
        },
    },
    "finish": {
        "description": "Return an answer and finish the task",
        "parameters": {
            "answer": {
                "type": ["string", "number", "array"],
                "description": "The answer to be returned",
                "required": True,
            }
        },
    },
}
