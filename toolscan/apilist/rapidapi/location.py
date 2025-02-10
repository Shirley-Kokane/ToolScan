RAPID_API = {
    "UGANDAAPI_API": {
        "directions_between_2_locations_for_uganda_api": {
            "description": "This endpoint returns information about the route between two locations in terms of distance, duration, and steps.\n\nBelow Example: **Directions from a location in Nansana to Kampala**",
            "parameters": {
                "end_lat": {
                    "type": "NUMBER",
                    "description": "Latitude of the ending point (required)",
                    "default": "0.32493795000000003",
                    "required": True,
                },
                "start_lat": {
                    "type": "NUMBER",
                    "description": "Latitude of the starting point (required)",
                    "default": "0.365816",
                    "required": True,
                },
                "end_lon": {
                    "type": "NUMBER",
                    "description": "Longitude of the ending point (required)",
                    "default": "32.57523607707668",
                    "required": True,
                },
                "start_lon": {
                    "type": "NUMBER",
                    "description": "Longitude of the starting point (required)",
                    "default": "32.529226",
                    "required": True,
                },
                "distance_unit": {
                    "type": "STRING",
                    "description": "Unit of distance measurement, valid options are **km** (default), and **mi**.",
                    "default": "km",
                    "required": False,
                },
            },
        },
        "reverse_geocode_for_uganda_api": {
            "description": "This endpoint allows you to perform reverse geocoding in Uganda by providing query parameters for latitude and longitude. It returns the name of the city where the location is located.",
            "parameters": {
                "lon": {
                    "type": "STRING",
                    "description": "The longitude of the location.",
                    "default": "32.57523607707668",
                    "required": True,
                },
                "lat": {
                    "type": "STRING",
                    "description": "The latitude of the location.",
                    "default": "0.32493795000000003",
                    "required": True,
                },
            },
        },
        "facilities_lookup_for_uganda_api": {
            "description": "This endpoint allows you to get facilities in Uganda like hospital, bank, college, etc. by providing optional query parameters for facility type, region and city. It returns a list of facilities that match the query parameters.",
            "parameters": {
                "region": {
                    "type": "STRING",
                    "description": "The region where the facility is located",
                    "default": "Central",
                    "required": True,
                },
                "type": {
                    "type": "STRING",
                    "description": "The type of amenity facility to search for (default: **hospital**)\nOptions:\n**aerodrome, bar, cafe, fast_food, pub, restaurant, college, driving_school, school, university, bank, atm, pharmacy,** etc..        \n\n[More options->](https://wiki.openstreetmap.org/wiki/Map_features#Amenity)",
                    "default": "hospital",
                    "required": True,
                },
                "limit": {
                    "type": "STRING",
                    "description": "The number of facilities to query.",
                    "default": "10",
                    "required": False,
                },
                "city": {
                    "type": "STRING",
                    "description": "The city where the facility is located",
                    "default": "Kampala",
                    "required": False,
                },
            },
        },
        "geocode_for_uganda_api": {
            "description": "This endpoint allows you to lookup locations in Uganda by providing an address query parameter. It returns the latitude, longitude and city name of the location.",
            "parameters": {
                "address": {
                    "type": "STRING",
                    "description": "Name of address",
                    "default": "Nansana",
                    "required": True,
                }
            },
        },
        "measure_distance_for_uganda_api": {
            "description": "This endpoint calculates the distance between two locations based on their latitude and longitude coordinates, while allowing the user to specify the unit of measurement.\n\nBelow Example: **Distance from Nansana to Kampala**",
            "parameters": {
                "lat1": {
                    "type": "NUMBER",
                    "description": "Latitude of the first location (required)",
                    "default": "0.365816",
                    "required": True,
                },
                "lat2": {
                    "type": "NUMBER",
                    "description": "Latitude of the second location (required)",
                    "default": "0.32493795000000003",
                    "required": True,
                },
                "lon2": {
                    "type": "NUMBER",
                    "description": "Longitude of the second location (required)",
                    "default": "32.57523607707668",
                    "required": True,
                },
                "lon1": {
                    "type": "NUMBER",
                    "description": "Longitude of the first location (required)",
                    "default": "32.529226",
                    "required": True,
                },
                "unit": {
                    "type": "STRING",
                    "description": "Unit of distance measurement, valid options are **km** (default), **mi**, **ft**, and **yd**.\n",
                    "default": "km",
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
