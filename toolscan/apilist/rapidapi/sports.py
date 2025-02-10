RAPID_API = {
    "BETSAPI_API": {
        "bet365_inplay_filter_for_betsapi": {
            "description": "bet365 inplay filter",
            "parameters": {
                "league_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "sport_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": False,
                },
                "skip_esports": {
                    "type": "BOOLEAN",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "bet365_inplay_for_betsapi": {
            "description": "bet365 inplay data",
            "parameters": {},
        },
        "bet365_inplay_event_for_betsapi": {
            "description": "inplay event with all scores/stats/markets",
            "parameters": {
                "FI": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "stats": {
                    "type": "ENUM",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "lineup": {
                    "type": "ENUM",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "bet365_upcoming_events_for_betsapi": {
            "description": "get bet365 fixtures",
            "parameters": {
                "sport_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "day": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "league_id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "bet365_prematch_odds_for_betsapi": {
            "description": "prematch odds",
            "parameters": {
                "FI": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "bet365_result_for_betsapi": {
            "description": "to view bet365 event result",
            "parameters": {
                "event_id": {
                    "type": "NUMBER",
                    "description": "",
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
    "PINNACLEODDS_API": {
        "betting_status_for_pinnacle_odds": {
            "description": "Get a betting status. Checking the Pinnacle server",
            "parameters": {},
        },
        "list_of_special_markets_for_pinnacle_odds": {
            "description": "Get a list of special markets. Always first issue a snapshot call and continue with the delta calls. Calls return changes since the provided `since` value. You must always use the since parameter, after the first call. Please note that prematch and live events are different",
            "parameters": {
                "sport_id": {
                    "type": "NUMBER",
                    "description": "Sport id",
                    "default": 1,
                    "required": True,
                },
                "is_have_odds": {
                    "type": "BOOLEAN",
                    "description": "`1` or `0`. You can only get matches for which there are already open odds, or matches that will be given odds in the future",
                    "default": True,
                    "required": False,
                },
                "league_ids": {
                    "type": "NUMBER",
                    "description": "League id",
                    "default": "",
                    "required": False,
                },
                "event_type": {
                    "type": "STRING",
                    "description": "Status: `prematch`, `live`  Please note that prematch and live events are different",
                    "default": "",
                    "required": False,
                },
                "since": {
                    "type": "NUMBER",
                    "description": "Since UTC time. Calls return changes since the provided `since` value.",
                    "default": "",
                    "required": False,
                },
                "event_ids": {
                    "type": "NUMBER",
                    "description": "Event id",
                    "default": "",
                    "required": False,
                },
            },
        },
        "event_details_for_pinnacle_odds": {
            "description": "Get a event details and history odds. history:[time, value, max bet]. `Period_results - status`: 1 = Event period is settled, 2 = Event period is re-settled, 3 = Event period is cancelled, 4 = Event period is re-settled as cancelled, 5 = Event is deleted",
            "parameters": {
                "event_id": {
                    "type": "NUMBER",
                    "description": "Event id",
                    "default": 1419211461,
                    "required": True,
                }
            },
        },
        "list_of_periods_for_pinnacle_odds": {
            "description": "Get a list of periods",
            "parameters": {
                "sport_id": {
                    "type": "NUMBER",
                    "description": "Sport id",
                    "default": 1,
                    "required": True,
                }
            },
        },
        "list_of_archive_events_for_pinnacle_odds": {
            "description": "Get a list of archive events. Use pagination",
            "parameters": {
                "sport_id": {
                    "type": "NUMBER",
                    "description": "Sport id",
                    "default": 1,
                    "required": True,
                },
                "page_num": {
                    "type": "NUMBER",
                    "description": "Page num",
                    "default": 1,
                    "required": True,
                },
                "league_ids": {
                    "type": "NUMBER",
                    "description": "League id",
                    "default": "",
                    "required": False,
                },
            },
        },
        "list_of_sports_for_pinnacle_odds": {
            "description": "Get a list of sports",
            "parameters": {},
        },
        "list_of_markets_for_pinnacle_odds": {
            "description": "Get a list of markets. Always first issue a snapshot call and continue with the delta calls. Calls return changes since the provided `since` value.  You must always use the `since` parameter, after starting your program cycle. You can make request without a `since` parameter no more than 15 times in 5 minutes. Please note that `prematch` and `live` events are different",
            "parameters": {
                "sport_id": {
                    "type": "NUMBER",
                    "description": "Sport id",
                    "default": 1,
                    "required": True,
                },
                "league_ids": {
                    "type": "NUMBER",
                    "description": "League id",
                    "default": "",
                    "required": False,
                },
                "event_type": {
                    "type": "STRING",
                    "description": "Status: `prematch`, `live`  Please note that prematch and live events are different",
                    "default": "",
                    "required": False,
                },
                "event_ids": {
                    "type": "NUMBER",
                    "description": "Event id",
                    "default": "",
                    "required": False,
                },
                "is_have_odds": {
                    "type": "BOOLEAN",
                    "description": "`1` or `0`. You can only get matches for which there are already open odds, or matches that will be given odds in the future",
                    "default": True,
                    "required": False,
                },
                "since": {
                    "type": "NUMBER",
                    "description": "Since UTC time. Calls return changes since the provided `since` value.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "list_of_leagues_for_pinnacle_odds": {
            "description": "Get a list of leagues",
            "parameters": {
                "sport_id": {
                    "type": "NUMBER",
                    "description": "Sport id",
                    "default": 1,
                    "required": True,
                }
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
