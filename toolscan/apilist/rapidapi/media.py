RAPID_API = {
    "SHAZAM_API": {
        "artist_top_tracks_for_shazam": {
            "description": "This endpoint will return the top tracks of the artist",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "5",
                    "required": True,
                },
                "artist_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "40543550",
                    "required": True,
                },
            },
        },
        "top_track_by_city_for_shazam": {
            "description": "This endpoint will give the top song in specific city",
            "parameters": {
                "city_name": {
                    "type": "STRING",
                    "description": "",
                    "default": "Moscow",
                    "required": True,
                },
                "country_code": {
                    "type": "STRING",
                    "description": "",
                    "default": "RU",
                    "required": True,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "2",
                    "required": False,
                },
            },
        },
        "top_track_by_country_for_shazam": {
            "description": "This endpoint will return the top tracks from a specific country",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "2",
                    "required": True,
                },
                "country_code": {
                    "type": "STRING",
                    "description": "",
                    "default": "RU",
                    "required": True,
                },
            },
        },
        "track_recommendations_for_shazam": {
            "description": "This endpoint will return the recommendation or similar songs of the given track.",
            "parameters": {
                "track_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "296831279",
                    "required": True,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "4",
                    "required": True,
                },
            },
        },
        "search_track_for_shazam": {
            "description": "This endpoint will search for the name of any song and return similar songs with the name.",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "5",
                    "required": True,
                },
                "track": {
                    "type": "STRING",
                    "description": "",
                    "default": "Love Yourself",
                    "required": True,
                },
            },
        },
        "track_info_for_shazam": {
            "description": "This endpoint will return info of any track from shazam.com",
            "parameters": {
                "track_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "296831279",
                    "required": True,
                }
            },
        },
        "artist_search_for_shazam": {
            "description": "This endpoint let you search for an artist by their name. You can get a list of artists from its name.",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "5",
                    "required": True,
                },
                "artist": {
                    "type": "STRING",
                    "description": "",
                    "default": "Justin Bieber",
                    "required": True,
                },
            },
        },
        "artist_info_for_shazam": {
            "description": "This endpoint will extract information of any artist from https://www.shazam.com.",
            "parameters": {
                "artist_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "40543550",
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
    "VIMEO_API": {
        "getrelatedchannels_for_vimeo": {
            "description": "",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "Category name",
                    "default": "",
                    "required": True,
                },
                "format": {
                    "type": "STRING",
                    "description": "json or xml or php",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "NUMBER",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getvideofromuser_for_vimeo": {
            "description": "Get all videos credited to a user (both uploaded and appears).",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/xml/php",
                    "default": "",
                    "required": True,
                },
                "user_id": {
                    "type": "STRING",
                    "description": "The ID number or username of the user. A token may be used instead.",
                    "default": "",
                    "required": True,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Method to sort by: newest, oldest, most_played, most_commented, or most_liked.",
                    "default": "",
                    "required": False,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "STRING",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": False,
                },
                "summary_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back more information.",
                    "default": "",
                    "required": False,
                },
                "full_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back the full video information.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getvideosbytag_for_vimeo": {
            "description": "Get a list of videos that have the specified tag.",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/php/xml",
                    "default": "",
                    "required": True,
                },
                "tag": {
                    "type": "STRING",
                    "description": "The tag to get",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "Page number to show",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "STRING",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": False,
                },
                "summary_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back more information.",
                    "default": "",
                    "required": False,
                },
                "full_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back the full video information.",
                    "default": "",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Method to sort by: relevant, newest, oldest, most_played, most_commented, or most_liked.",
                    "default": "most_commented",
                    "required": False,
                },
            },
        },
        "getallchannels_for_vimeo": {
            "description": "Get a list of all public channels.",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/xml/php",
                    "default": "",
                    "required": True,
                },
                "per_page": {
                    "type": "STRING",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": True,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Method to sort by: newest, oldest, alphabetical, most_videos, most_subscribed, or most_recently_updated.",
                    "default": "most_recently_updated",
                    "required": False,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getchannelvideos_for_vimeo": {
            "description": "Get a list of the videos in a channel.",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/xml/php",
                    "default": "",
                    "required": True,
                },
                "channel_id": {
                    "type": "STRING",
                    "description": "The numeric id of the channel or its url name.",
                    "default": "",
                    "required": True,
                },
                "full_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back the full video information",
                    "default": "",
                    "required": True,
                },
                "user_id": {
                    "type": "STRING",
                    "description": "The ID number or username of the user. A token may be used instead.",
                    "default": "",
                    "required": False,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "Number of items to show on each page. Max 50.",
                    "required": False,
                },
                "summary_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back more information.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getrelatedtags_for_vimeo": {
            "description": "Get a list of related tags for a category.",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "The Name of category",
                    "default": "",
                    "required": True,
                },
                "format": {
                    "type": "STRING",
                    "description": "json or xml or php",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "NUMBER",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "searchvideos_for_vimeo": {
            "description": "Search for videos.",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/xml/php",
                    "default": "",
                    "required": True,
                },
                "query": {
                    "type": "STRING",
                    "description": "The search terms",
                    "default": "",
                    "required": True,
                },
                "user_id": {
                    "type": "STRING",
                    "description": "The ID number or username of the user.",
                    "default": "",
                    "required": False,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "NUMBER",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": False,
                },
                "summary_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back more information.",
                    "default": "",
                    "required": False,
                },
                "full_response": {
                    "type": "BOOLEAN",
                    "description": "Set this parameter to get back the full video information.",
                    "default": "",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Method to sort by: relevant, newest, oldest, most_played, most_commented, or most_liked.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getchannelinfo_for_vimeo": {
            "description": "Get the information on a single channel.",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/xml/php",
                    "default": "",
                    "required": True,
                },
                "channel_id": {
                    "type": "STRING",
                    "description": "The numeric id of the channel or its url name.",
                    "default": "",
                    "required": True,
                },
            },
        },
        "getrelatedpeople_for_vimeo": {
            "description": "Get a list of related people for a category.",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "The name of the category.",
                    "default": "",
                    "required": True,
                },
                "format": {
                    "type": "STRING",
                    "description": "json or xml or php",
                    "default": "json",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "NUMBER",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getvideoscomment_for_vimeo": {
            "description": "Get a list of the comments on a video.",
            "parameters": {
                "format": {
                    "type": "STRING",
                    "description": "json/php/xml",
                    "default": "",
                    "required": True,
                },
                "video_id": {
                    "type": "STRING",
                    "description": "The ID of the video.",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "The page number to show.",
                    "default": "",
                    "required": False,
                },
                "per_page": {
                    "type": "NUMBER",
                    "description": "Number of items to show on each page. Max 50.",
                    "default": "",
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
