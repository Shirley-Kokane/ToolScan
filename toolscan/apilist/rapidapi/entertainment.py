RAPID_API = {
    "WORLDOFJOKES_API": {
        "get_joke_of_the_day_by_category_for_world_of_jokes": {
            "description": "Get the joke of the day of specific category from a collection of most rated and most popular jokes.",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "Category of joke based on the jokes categories API",
                    "default": "Money",
                    "required": True,
                }
            },
        },
        "get_random_joke_by_category_for_world_of_jokes": {
            "description": "Get the random joke by category from a collection of most rated and most popular jokes.",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "Category of joke based on the jokes categories API",
                    "default": "Political",
                    "required": True,
                }
            },
        },
        "get_random_joke_for_world_of_jokes": {
            "description": "Get the random joke from a collection of most rated and most popular jokes.",
            "parameters": {},
        },
        "get_jokes_for_world_of_jokes": {
            "description": "Access our huge collection of jokes and paginate through them based on your desired limit and sorting criteria.",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 100,
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 1,
                    "required": True,
                },
                "sortby": {
                    "type": "STRING",
                    "description": "Valid format to sort is `field:order`\ne.g. `score:desc` for highest score first sorting\n\nwhere `asc` for sorting in ascending order\n`desc` for sorting in descending order",
                    "default": "score:desc",
                    "required": False,
                },
            },
        },
        "get_categories_of_jokes_for_world_of_jokes": {
            "description": "Get all available categories of our Jokes collection which can be used to filter jokes based on specific category.",
            "parameters": {},
        },
        "get_jokes_by_specific_category_for_world_of_jokes": {
            "description": "Access our huge collection of jokes of specific category and paginate through them based on your desired limit and sorting criteria.",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 100,
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": 1,
                    "required": True,
                },
                "category": {
                    "type": "STRING",
                    "description": "Category of joke based on the jokes categories API",
                    "default": "Women",
                    "required": True,
                },
                "sortby": {
                    "type": "STRING",
                    "description": "Valid format to sort is `field:order`\ne.g. `score:desc` for highest score first sorting\nwhere `asc` for sorting in ascending order\n`desc` for sorting in descending order",
                    "default": "score:desc",
                    "required": False,
                },
            },
        },
        "get_joke_of_the_day_for_world_of_jokes": {
            "description": "Get the joke of the day from a collection of most rated and most popular jokes.",
            "parameters": {},
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
