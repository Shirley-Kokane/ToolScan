RAPID_API = {
    "FLIGHTFARESEARCH_API": {
        "airport_arrivals_for_flight_fare_search": {
            "description": "An Endpoint to fetch Arrivals on a given date",
            "parameters": {
                "airportCode": {
                    "type": "STRING",
                    "description": "",
                    "default": "LHR",
                    "required": True,
                },
                "carrierCode": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "date": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "flight_search_v2_for_flight_fare_search": {
            "description": "A faster, more agile Endpoint that's used to search flights.",
            "parameters": {
                "date": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "from": {
                    "type": "STRING",
                    "description": "",
                    "default": "LHR",
                    "required": True,
                },
                "adult": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": True,
                },
                "to": {
                    "type": "STRING",
                    "description": "",
                    "default": "DXB",
                    "required": True,
                },
                "currency": {
                    "type": "STRING",
                    "description": "",
                    "default": "USD",
                    "required": False,
                },
                "type": {
                    "type": "STRING",
                    "description": "",
                    "default": "economy",
                    "required": False,
                },
                "child": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "infant": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "airport_departues_for_flight_fare_search": {
            "description": "An endpoint to get Departues in an airport",
            "parameters": {
                "airportCode": {
                    "type": "STRING",
                    "description": "",
                    "default": "LHR",
                    "required": True,
                },
                "carrierCode": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "date": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "airport_search_for_flight_fare_search": {
            "description": "An endpoint to search airports",
            "parameters": {
                "query": {
                    "type": "STRING",
                    "description": "",
                    "default": "LHR",
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
    }
}
