PATENT_API = {
    "search_patent_type_and_title_and_date": {
        "description": "Retrieve patents with dates, titles, patent type, categories using the PatentsView API.",
        "parameters": {
            "patent_date": {
                "type": str,
                "description": "The date to compare patents against. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "patent_type": {
                "type": str,
                "description": "A string representing which patent type",
                "default": "design",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_not_patent_type_and_title_and_date": {
        "description": "Retrieve patents with dates, titles and not including patent type using the PatentsView API.",
        "parameters": {
            "patent_date": {
                "type": str,
                "description": "The date to compare patents against. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "patent_type": {
                "type": str,
                "description": "A string representing which patent type",
                "default": "design",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patent_greater_than_equal_to": {
        "description": "Retrieve patents with a date greater than or equal to the specified date using the PatentsView API.",
        "parameters": {
            "patent_date": {
                "type": str,
                "description": "The date to compare patents against. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patent_less_than_equal_to": {
        "description": "Retrieve patents with a date less than or equal to the specified date using the PatentsView API.",
        "parameters": {
            "patent_date": {
                "type": str,
                "description": "The date to compare patents against. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patent_lastname_and_less_than_and_greater_than": {
        "description": "Retrieve patents invented within less than and greater than dates and lastnames using the PatentsView API.",
        "parameters": {
            "_gt": {
                "type": str,
                "description": "The start patent date of patents to collect from. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "_lt": {
                "type": str,
                "description": "The end patent date of patents to collect from. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-12-09",
                "required": True,
            },
            "inventor_last_names": {
                "type": list,
                "description": "A list of inventor last names to search for.",
                "default": ["Whitney", "Hopper"],
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patent_less_than_and_greater_than": {
        "description": "Retrieve patents invented within less than and greater than dates using the PatentsView API.",
        "parameters": {
            "_gt": {
                "type": str,
                "description": "The start patent date of patents to collect from. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "_lt": {
                "type": str,
                "description": "The end patent date of patents to collect from. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-12-09",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patent_less_than_or_greater_than": {
        "description": "Retrieve patents invented outside the less than and greater than date using the PatentsView API.",
        "parameters": {
            "_gt": {
                "type": str,
                "description": "Collect patents from after this patent date . Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-01-09",
                "required": True,
            },
            "_lt": {
                "type": str,
                "description": "Collect patents from before this patent date. Format should be 'YYYY-MM-DD'.",
                "example_value": "2007-12-09",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patents_lastname_or_title": {
        "description": "Search for patents using the PatentsView API based on inventor last names and patent titles.",
        "parameters": {
            "inventor_last_names": {
                "type": list,
                "description": "A list of inventor last names to search for.",
                "default": ["Whitney", "Hopper"],
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API,Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patents_lastname_and_title": {
        "description": "Search for patents using the PatentsView API based on inventor last names or patent titles.",
        "parameters": {
            "inventor_last_names": {
                "type": list,
                "description": "A list of inventor last names to search for.",
                "default": ["Whitney", "Hopper"],
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API,Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patents_lastname_and_title_and_date": {
        "description": "Search for patents using the PatentsView API based on inventor last names, patent titles and date.",
        "parameters": {
            "inventor_last_names": {
                "type": list,
                "description": "A list of inventor last names to search for.",
                "default": ["Whitney", "Hopper"],
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "patent_date": {
                "type": str,
                "description": "The patent grant date to search for in the format YYYY-MM-DD.",
                "default": "1981-10-06",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API,Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patents_lastname_and_date": {
        "description": "Search for patents using the PatentsView API based on inventor last name and patent date.",
        "parameters": {
            "inventor_last_names": {
                "type": list,
                "description": "The inventor's last name to search for.",
                "default": ["Whitney"],
                "required": True,
            },
            "patent_date": {
                "type": str,
                "description": "The patent grant date to search for in the format YYYY-MM-DD.",
                "default": "1981-10-06",
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API,Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patents_lastname_and_title_and_greater_than_date": {
        "description": "Search for patents using the PatentsView API based on inventor last name and patent date.",
        "parameters": {
            "inventor_last_names": {
                "type": list,
                "description": "The inventor's last name to search for.",
                "default": ["Whitney"],
                "required": True,
            },
            "_gte": {
                "type": str,
                "description": "The patent grant date greater than the provided date to search for in the format YYYY-MM-DD.",
                "default": "1981-10-06",
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API,Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
            },
        },
    },
    "search_patents_lastname_and_title_and_lesser_than_date": {
        "description": "Search for patents using the PatentsView API based on inventor last name and patent date.",
        "parameters": {
            "inventor_last_names": {
                "type": list,
                "description": "The inventor's last name to search for.",
                "default": ["Whitney"],
                "required": True,
            },
            "_lt": {
                "type": str,
                "description": "The patent grant date greater than the provided date date to search for in the format YYYY-MM-DD.",
                "default": "1981-10-06",
                "required": True,
            },
            "patent_titles": {
                "type": list,
                "description": "A list of terms to search for in patent titles.",
                "default": ["COBOL", "cotton gin"],
                "required": True,
            },
            "categories": {
                "type": list,
                "description": "Representing what entities to retrieve from the API, Options available [patent_number,patent_date,patent_title,inventor_last_name]",
                "default": [""],
                "required": True,
            },
            "page": {
                "type": int,
                "description": "Page number to retrieve the patents from",
                "default": 1,
                "required": True,
            },
            "count": {
                "type": int,
                "description": "No. of patents to retreive using the PatentsView API",
                "default": 5,
                "required": True,
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
