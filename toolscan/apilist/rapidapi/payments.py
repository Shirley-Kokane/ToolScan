RAPID_API = {
    "ONBOARDINGPROJECT_API": {
        "get_products_for_onboarding_project": {
            "description": " ",
            "parameters": {
                "skip": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                },
            },
        },
        "get_categories_for_onboarding_project": {"description": " ", "parameters": {}},
        "get_product_for_onboarding_project": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "me_for_onboarding_project": {"description": " ", "parameters": {}},
        "get_products_in_category_for_onboarding_project": {
            "description": " ",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "skip": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": True,
                },
            },
        },
        "get_order_for_onboarding_project": {
            "description": " ",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "get_user_orders_for_onboarding_project": {
            "description": " ",
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
