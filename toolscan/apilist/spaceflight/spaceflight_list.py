SPACEFLIGHT_API = {
    "search_spaceflight_articles_with_newssite": {
        "description": "Search for articles using the Spaceflight News API based on various parameters.",
        "parameters": {
            "search": {
                "type": str,
                "description": "Search for documents on a specific topic.",
                "default": "",
                "required": True,
            },
            "news_site": {
                "type": str,
                "description": "Search for documents with a news_site__name present in a list of comma-separated values (nasa, spacenews, Spaceflight Now, SpacePolicyOnline.com, European Spaceflight, ESA, Planetary Society). Case insensitive.",
                "default": "NASA",
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "news_site_exclude": {
                "type": str,
                "description": "Search for documents with a news_site__name not present in a list of comma-separated values (nasa, spacenews, Spaceflight Now, SpacePolicyOnline.com, European Spaceflight, ESA, Planetary Society). Case insensitive.",
                "default": None,
                "required": False,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "search_spaceflight_articles_with_newssite_and_published_date_equal": {
        "description": "Search for articles using the Spaceflight News API based on various parameters.",
        "parameters": {
            "search": {
                "type": str,
                "description": "Search for documents on a specific topic.",
                "default": "",
                "required": True,
            },
            "news_site": {
                "type": str,
                "description": "Search for documents with a news_site__name present in a list of comma-separated values (nasa, spacenews, Spaceflight Now, SpacePolicyOnline.com, European Spaceflight, ESA, Planetary Society). Case insensitive.",
                "default": "NASA",
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "news_site_exclude": {
                "type": str,
                "description": "Search for documents with a news_site_name not present in a list of comma-separated values (nasa, spacenews, Spaceflight Now, SpacePolicyOnline.com, European Spaceflight, ESA, Planetary Society). Case insensitive.",
                "default": None,
                "required": False,
            },
            "published_at_gte": {
                "type": str,
                "description": " Get all documents published after a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "published_at_lte": {
                "type": str,
                "description": " Get all documents published before a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "search_spaceflight_articles_with_newssite_and_published_date_unequal": {
        "description": "Search for articles using the Spaceflight News API based on various parameters.",
        "parameters": {
            "search": {
                "type": str,
                "description": "Search for documents on a specific topic.",
                "default": "",
                "required": True,
            },
            "news_site": {
                "type": str,
                "description": "Search for documents with a news_site__name present in a list of comma-separated values (nasa, spacenews, Spaceflight Now, SpacePolicyOnline.com, European Spaceflight, ESA, Planetary Society). Case insensitive.",
                "default": "NASA",
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "news_site_exclude": {
                "type": str,
                "description": "Search for documents with a news_site__name not present in a list of comma-separated values (nasa, spacenews, Spaceflight Now, SpacePolicyOnline.com, European Spaceflight, ESA, Planetary Society). Case insensitive.",
                "default": None,
                "required": False,
            },
            "published_at_gt": {
                "type": str,
                "description": " Get all documents published after a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "published_at_lt": {
                "type": str,
                "description": " Get all documents published before a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "search_spaceflight_blogs_with_title": {
        "description": "Search for blogs using the Spaceflight News API based on various parameters.",
        "parameters": {
            "title_contains": {
                "type": str,
                "description": "Search for all documents with a specific phrase in the title.",
                "default": None,
                "required": True,
            },
            "title_contains_all": {
                "type": str,
                "description": "Search for documents with a title containing all keywords from comma-separated values.",
                "default": None,
                "required": False,
            },
            "title_contains_one": {
                "type": str,
                "description": "Search for documents with a title containing at least one keyword from comma-separated values.",
                "default": None,
                "required": False,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 10,
                "required": False,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "search_spaceflight_blogs_with_title_and_published_date_equal": {
        "description": "Search for blogs using the Spaceflight News API based on various parameters.",
        "parameters": {
            "title_contains": {
                "type": str,
                "description": "Search for all documents with a specific phrase in the title.",
                "default": None,
                "required": True,
            },
            "title_contains_all": {
                "type": str,
                "description": "Search for documents with a title containing all keywords from comma-separated values.",
                "default": None,
                "required": False,
            },
            "title_contains_one": {
                "type": str,
                "description": "Search for documents with a title containing at least one keyword from comma-separated values.",
                "default": None,
                "required": False,
            },
            "published_at_gte": {
                "type": str,
                "description": " Get all documents published after a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "published_at_lte": {
                "type": str,
                "description": " Get all documents published before a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "search_spaceflight_blogs_with_title_and_published_date_unequal": {
        "description": "Search for blogs using the Spaceflight News API based on various parameters.",
        "parameters": {
            "title_contains": {
                "type": str,
                "description": "Search for all documents with a specific phrase in the title.",
                "default": None,
                "required": True,
            },
            "title_contains_all": {
                "type": str,
                "description": "Search for documents with a title containing all keywords from comma-separated values.",
                "default": None,
                "required": False,
            },
            "title_contains_one": {
                "type": str,
                "description": "Search for documents with a title containing at least one keyword from comma-separated values.",
                "default": None,
                "required": False,
            },
            "published_at_gt": {
                "type": str,
                "description": " Get all documents published after a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "published_at_lt": {
                "type": str,
                "description": " Get all documents published before a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "get_spaceflight_news_info": {
        "description": "Retrieve information about the Spaceflight News API.",
        "parameters": {},
    },
    "get_spaceflight_article_by_id": {
        "description": "Retrieve an article using the Spaceflight News API based on its ID.",
        "parameters": {
            "article_id": {
                "type": int,
                "default": 1,
                "required": True,
                "description": "ID number of the article.",
            }
        },
    },
    "get_spaceflight_blog_by_id": {
        "description": "Retrieve a blog using the Spaceflight News API based on its ID.",
        "parameters": {
            "blog_id": {
                "type": int,
                "description": "The ID of the blog to retrieve.",
                "default": 1,
                "required": True,
            }
        },
    },
    "search_spaceflight_reports_with_summary_and_published_date_equal": {
        "description": "Search for reports using the Spaceflight News API based on various parameters.",
        "parameters": {
            "summary_contains": {
                "type": str,
                "description": "Search for all documents with a specific phrase in the summary.",
                "default": None,
                "required": True,
            },
            "summary_contains_all": {
                "type": str,
                "description": "Search for documents with a summary containing all keywords from comma-separated values.",
                "default": None,
                "required": False,
            },
            "summary_contains_one": {
                "type": str,
                "description": "Search for documents with a summary containing at least one keyword from comma-separated values.",
                "default": None,
                "required": False,
            },
            "published_at_gte": {
                "type": str,
                "description": " Get all documents published after a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "published_at_lte": {
                "type": str,
                "description": " Get all documents published before a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "search_spaceflight_reports_with_summary_and_published_date_unequal": {
        "description": "Search for reports using the Spaceflight News API based on various parameters.",
        "parameters": {
            "search": {
                "type": str,
                "description": "Search for documents with a specific phrase in the summary.",
                "default": "",
                "required": True,
            },
            "summary_contains": {
                "type": str,
                "description": "Search for all documents with a specific phrase in the summary.",
                "default": None,
                "required": False,
            },
            "summary_contains_all": {
                "type": str,
                "description": "Search for documents with a summary containing all keywords from comma-separated values.",
                "default": None,
                "required": False,
            },
            "summary_contains_one": {
                "type": str,
                "description": "Search for documents with a summary containing at least one keyword from comma-separated values.",
                "default": None,
                "required": False,
            },
            "published_at_gt": {
                "type": str,
                "description": " Get all documents published after a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "published_at_lt": {
                "type": str,
                "description": " Get all documents published before a given ISO8601 timestamp (excluded). The format is DateTime String, YYYY-MM-DDTHH:MM:SS",
                "default": None,
                "required": True,
            },
            "limit": {
                "type": int,
                "description": "Number of results to return per page.",
                "default": 1,
                "required": True,
            },
            "offset": {
                "type": int,
                "description": "The initial index from which to return the results.",
                "default": 0,
                "required": False,
            },
            "ordering": {
                "type": str,
                "description": "Which field to use when ordering the results.",
                "default": None,
                "required": False,
            },
        },
    },
    "get_spaceflight_report_by_id": {
        "description": "Retrieve a report using the Spaceflight News API based on its ID.",
        "parameters": {
            "report_id": {
                "type": int,
                "description": "The ID of the report to retrieve.",
                "default": 1,
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
