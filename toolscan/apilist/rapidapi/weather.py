RAPID_API = {
    "FORECAWEATHER_API": {
        "nowcast_for_foreca_weather": {
            "description": "3-hour forecast in 15-minute time steps.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "102643743",
                    "required": True,
                },
                "dataset": {
                    "type": "STRING",
                    "description": "Variable set",
                    "default": "full",
                    "required": False,
                },
                "windunit": {
                    "type": "STRING",
                    "description": "Wind speed unit in response.",
                    "default": "MS",
                    "required": False,
                },
                "tz": {
                    "type": "STRING",
                    "description": "Time zone in response (IANA time zone database names)",
                    "default": "Europe/London",
                    "required": False,
                },
                "tempunit": {
                    "type": "STRING",
                    "description": "Temperature unit in response",
                    "default": "C",
                    "required": False,
                },
                "alt": {
                    "type": "NUMBER",
                    "description": "Altitude (meters)",
                    "default": "0",
                    "required": False,
                },
                "periods": {
                    "type": "NUMBER",
                    "description": "Number of time steps (default 8, maximum 12)",
                    "default": "8",
                    "required": False,
                },
            },
        },
        "three_hourly_for_foreca_weather": {
            "description": "A longer three-hourly forecast up to 14 days.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "102643743",
                    "required": True,
                },
                "history": {
                    "type": "BOOLEAN",
                    "description": "Whether to include 24 hours of past data.",
                    "default": "0",
                    "required": False,
                },
                "tz": {
                    "type": "STRING",
                    "description": "Time zone in response (IANA time zone database names)",
                    "default": "Europe/London",
                    "required": False,
                },
                "dataset": {
                    "type": "STRING",
                    "description": "Variable set",
                    "default": "full",
                    "required": False,
                },
                "tempunit": {
                    "type": "STRING",
                    "description": "Temperature unit in response",
                    "default": "C",
                    "required": False,
                },
                "alt": {
                    "type": "NUMBER",
                    "description": "Altitude (meters)",
                    "default": "0",
                    "required": False,
                },
                "periods": {
                    "type": "NUMBER",
                    "description": "Number of time steps (default 8, maximum 12)",
                    "default": "8",
                    "required": False,
                },
                "windunit": {
                    "type": "STRING",
                    "description": "Wind speed unit in response.",
                    "default": "MS",
                    "required": False,
                },
            },
        },
        "daily_for_foreca_weather": {
            "description": "Daily forecast.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "102643743",
                    "required": True,
                },
                "alt": {
                    "type": "NUMBER",
                    "description": "Altitude (meters)",
                    "default": "0",
                    "required": False,
                },
                "dataset": {
                    "type": "STRING",
                    "description": "Variable set",
                    "default": "full",
                    "required": False,
                },
                "tempunit": {
                    "type": "STRING",
                    "description": "Temperature unit in response",
                    "default": "C",
                    "required": False,
                },
                "windunit": {
                    "type": "STRING",
                    "description": "Wind speed unit in response.",
                    "default": "MS",
                    "required": False,
                },
                "periods": {
                    "type": "NUMBER",
                    "description": "Number of time steps (default 8, maximum 12)",
                    "default": "8",
                    "required": False,
                },
            },
        },
        "location_info_for_foreca_weather": {
            "description": "Metadata for location.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "101275339",
                    "required": True,
                }
            },
        },
        "current_for_foreca_weather": {
            "description": "Current weather estimate for location.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "102643743",
                    "required": True,
                },
                "windunit": {
                    "type": "STRING",
                    "description": "Wind speed unit in response.",
                    "default": "MS",
                    "required": False,
                },
                "alt": {
                    "type": "NUMBER",
                    "description": "Altitude (meters)",
                    "default": "0",
                    "required": False,
                },
                "lang": {
                    "type": "STRING",
                    "description": "Language (ISO 639-1 codes). Options: de, en, es, fr, it, pl, ru, fi, sv, nl, ko, pt, th, tr, zh, zh_TW (Chinese in Taiwan), zh_CN (Chinese in China). (default en)",
                    "default": "en",
                    "required": False,
                },
                "tz": {
                    "type": "STRING",
                    "description": "Time zone in response (IANA time zone database names)",
                    "default": "Europe/London",
                    "required": False,
                },
                "tempunit": {
                    "type": "STRING",
                    "description": "Temperature unit in response",
                    "default": "C",
                    "required": False,
                },
            },
        },
        "latest_observations_for_foreca_weather": {
            "description": "Observations from nearby representative weather stations.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "102643743",
                    "required": True,
                },
                "lang": {
                    "type": "STRING",
                    "description": "",
                    "default": "en",
                    "required": False,
                },
            },
        },
        "location_search_for_foreca_weather": {
            "description": "Search for locations by name.",
            "parameters": {
                "query": {
                    "type": "string",
                    "description": "",
                    "default": "mumbai",
                    "required": True,
                },
                "lang": {
                    "type": "STRING",
                    "description": "",
                    "default": "en",
                    "required": False,
                },
                "country": {
                    "type": "STRING",
                    "description": "",
                    "default": "in",
                    "required": False,
                },
            },
        },
        "hourly_for_foreca_weather": {
            "description": "Hourly forecast.",
            "parameters": {
                "location": {
                    "type": "string",
                    "description": "",
                    "default": "102643743",
                    "required": True,
                },
                "alt": {
                    "type": "NUMBER",
                    "description": "Altitude (meters)",
                    "default": "0",
                    "required": False,
                },
                "history": {
                    "type": "BOOLEAN",
                    "description": "Whether to include 24 hours of past data.",
                    "default": "0",
                    "required": False,
                },
                "dataset": {
                    "type": "STRING",
                    "description": "Variable set",
                    "default": "full",
                    "required": False,
                },
                "tz": {
                    "type": "STRING",
                    "description": "Time zone in response (IANA time zone database names)",
                    "default": "Europe/London",
                    "required": False,
                },
                "periods": {
                    "type": "NUMBER",
                    "description": "Number of time steps (default 8, maximum 12)",
                    "default": "8",
                    "required": False,
                },
                "windunit": {
                    "type": "STRING",
                    "description": "Wind speed unit in response.",
                    "default": "MS",
                    "required": False,
                },
                "tempunit": {
                    "type": "STRING",
                    "description": "Temperature unit in response",
                    "default": "C",
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
