RAPID_API = {
    "WAZE_API": {
        "autocomplete_for_waze": {
            "description": "Waze/Google autocomplete/type-ahead for places, locations and addresses.",
            "parameters": {
                "q": {
                    "type": "STRING",
                    "description": "Free-text geographic query",
                    "default": "sunn",
                    "required": True,
                },
                "lang": {
                    "type": "STRING",
                    "description": "The language of the results. See https://wazeopedia.waze.com/wiki/USA/Countries_and_Languages for a list of supported languages.",
                    "default": "en",
                    "required": False,
                },
                "coordinates": {
                    "type": "STRING",
                    "description": "Geographic coordinates (latitude, longitude) bias. Highly recommended to use for getting accurate results.",
                    "default": "37.376754, -122.023350",
                    "required": False,
                },
            },
        },
        "driving_directions_for_waze": {
            "description": "Get routes and driving directions from Waze/Google.",
            "parameters": {
                "source_coordinates": {
                    "type": "STRING",
                    "description": "Geographic coordinates (latitude, longitude pair) of the starting point",
                    "default": "32.0852999,34.78176759999999",
                    "required": True,
                },
                "destination_coordinates": {
                    "type": "STRING",
                    "description": "Geographic coordinates (latitude, longitude pair) of the destination",
                    "default": "32.7940463,34.989571",
                    "required": True,
                },
                "return_route_coordinates": {
                    "type": "BOOLEAN",
                    "description": "Whether to return route coordinate pairs (`route_coordinates` field)",
                    "default": "",
                    "required": False,
                },
                "arrival_timestamp": {
                    "type": "NUMBER",
                    "description": "Unix-timestamp (seconds since epoch) of the arrival time (in case not specified directions will be returned for current time) ",
                    "default": "",
                    "required": False,
                },
            },
        },
        "alerts_and_jams_for_waze": {
            "description": "Get real-time alerts and jams from Waze in a geographic rectangular area defined by bottom-left and top-right latitude, longitude pairs.",
            "parameters": {
                "top_right": {
                    "type": "STRING",
                    "description": "Top-right corner of the geographic rectangular area for which to get alerts and traffic jams. Specified as latitude, longitude pair.",
                    "default": "40.772787404902594,-73.76818084716798",
                    "required": True,
                },
                "bottom_left": {
                    "type": "STRING",
                    "description": "Bottom-left corner of the geographic rectangular area for which to get alerts and traffic jams. Specified as latitude, longitude pair.",
                    "default": "40.66615391742187,-74.13732147216798",
                    "required": True,
                },
                "max_alerts": {
                    "type": "NUMBER",
                    "description": "Maximum number of alerts to fetch (to avoid fetching alerts set it to `0`).\nDefault: `20`",
                    "default": "20",
                    "required": False,
                },
                "max_jams": {
                    "type": "NUMBER",
                    "description": "Maximum number of traffic jams to fetch (to avoid fetching traffic jams, set it to `0`).\nDefault: `20`",
                    "default": "20",
                    "required": False,
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
}
