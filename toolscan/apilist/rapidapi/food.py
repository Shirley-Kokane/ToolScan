RAPID_API = {
    "FASTFOODRESTAURANTSUSATOP50CHAINS_API": {
        "get_all_city_names_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "GET all City names",
            "parameters": {},
        },
        "get_all_state_names_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "GET all State names",
            "parameters": {},
        },
        "get_all_chain_names_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "Get all Chain names",
            "parameters": {},
        },
        "get_all_restaurants_by_chain_city_state_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "Get restaurant Chain by City and State",
            "parameters": {
                "city": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "state": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "restaurantchainname": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 1,
                    "required": True,
                },
            },
        },
        "get_all_restaurants_by_chain_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "Get all restaurants by Chain",
            "parameters": {
                "restaurantchainname": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 1,
                    "required": True,
                },
            },
        },
        "get_all_restaurants_by_chain_state_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "Get all restaurants in the chain in state",
            "parameters": {
                "state": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "restaurantchainname": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 1,
                    "required": True,
                },
            },
        },
        "get_restaurant_logo_by_chain_name_for_fast_food_restaurants_usa_top_50_chains": {
            "description": "Get Restaurant Logo by Chain Name",
            "parameters": {
                "restaurantchainname": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
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
