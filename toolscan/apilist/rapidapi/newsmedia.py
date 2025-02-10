RAPID_API = {
    "INDONESIANEWS_API": {
        "vivanews_detail_for_indonesia_news": {
            "description": "vivanews-detail",
            "parameters": {
                "id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1612364",
                    "required": True,
                }
            },
        },
        "vivanews_search_for_indonesia_news": {
            "description": "vivanews-search",
            "parameters": {
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": True,
                },
                "keyword": {
                    "type": "STRING",
                    "description": "",
                    "default": "banjir",
                    "required": True,
                },
            },
        },
        "kompas_detail_for_indonesia_news": {
            "description": "kompas-detail",
            "parameters": {
                "guid": {
                    "type": "STRING",
                    "description": "",
                    "default": ".xml.2023.06.20.114935178",
                    "required": True,
                }
            },
        },
        "kompas_search_for_indonesia_news": {
            "description": "kompas-search",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": True,
                },
                "command": {
                    "type": "STRING",
                    "description": "",
                    "default": "banjir",
                    "required": True,
                },
            },
        },
        "detik_detail_for_indonesia_news": {
            "description": "detik-detail",
            "parameters": {
                "url": {
                    "type": "STRING",
                    "description": "",
                    "default": "https://finance.detik.com/bursa-dan-valas/d-5206657/bei-buka-suspensi-saham-pollux",
                    "required": True,
                }
            },
        },
        "detik_search_for_indonesia_news": {
            "description": "search detik.com news",
            "parameters": {
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": True,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": True,
                },
                "keyword": {
                    "type": "STRING",
                    "description": "",
                    "default": "detik",
                    "required": True,
                },
            },
        },
        "tirto_detail_for_indonesia_news": {
            "description": "detail tirto news",
            "parameters": {
                "id": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1253421",
                    "required": True,
                }
            },
        },
        "tirto_search_for_indonesia_news": {
            "description": "search tirto news data",
            "parameters": {
                "limit": {
                    "type": "STRING",
                    "description": "",
                    "default": "10",
                    "required": True,
                },
                "q": {
                    "type": "STRING",
                    "description": "",
                    "default": "banjir",
                    "required": True,
                },
                "page": {
                    "type": "STRING",
                    "description": "",
                    "default": "1",
                    "required": True,
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
