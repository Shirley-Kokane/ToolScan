RAPID_API = {
    "CONVEXITY_API": {
        "hsl_to_rgb_for_convexity": {
            "description": "Converts  hsl color code to rgb color code",
            "parameters": {
                "s": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "78",
                    "required": True,
                },
                "h": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "250",
                    "required": True,
                },
                "l": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "45",
                    "required": True,
                },
            },
        },
        "convert_hsl_for_convexity": {
            "description": "Endpoint to converts HSL color code to other color code like Hex , RGB, CMYK",
            "parameters": {
                "s": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "78",
                    "required": True,
                },
                "h": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "250",
                    "required": True,
                },
                "l": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "45",
                    "required": True,
                },
            },
        },
        "rgb_to_cmyk_for_convexity": {
            "description": "Converts  rgb color code to cmyk color code",
            "parameters": {
                "r": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "127",
                    "required": True,
                },
                "g": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "255",
                    "required": True,
                },
                "b": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "212",
                    "required": True,
                },
            },
        },
        "rgb_to_hsl_for_convexity": {
            "description": "Converts  rgb color code to hsl color code",
            "parameters": {
                "r": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "127",
                    "required": True,
                },
                "g": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "255",
                    "required": True,
                },
                "b": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "212",
                    "required": True,
                },
            },
        },
        "rgb_to_hex_for_convexity": {
            "description": "Converts  rgb color code to hex color code",
            "parameters": {
                "b": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "212",
                    "required": True,
                },
                "g": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "255",
                    "required": True,
                },
                "r": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "127",
                    "required": True,
                },
            },
        },
        "convert_rgb_for_convexity": {
            "description": "Endpoint to converts RGB color code to other color code like Hex , HSL, CMYK",
            "parameters": {
                "r": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "127",
                    "required": True,
                },
                "g": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "255",
                    "required": True,
                },
                "b": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "212",
                    "required": True,
                },
            },
        },
        "convert_hex_for_convexity": {
            "description": "Endpoint to converts hex color code to other color code like RGB , HSL, CMYK",
            "parameters": {
                "hex": {
                    "type": "STRING",
                    "description": "",
                    "default": "ffffff",
                    "required": True,
                }
            },
        },
        "hex_to_rgb_for_convexity": {
            "description": "Converts hex color code to rgb color code.",
            "parameters": {
                "hex": {
                    "type": "STRING",
                    "description": "",
                    "default": "ffffff",
                    "required": True,
                }
            },
        },
        "hex_to_cmyk_for_convexity": {
            "description": "Converts hex color code to  cmyk color code",
            "parameters": {
                "hex": {
                    "type": "STRING",
                    "description": "",
                    "default": "ffffff",
                    "required": True,
                }
            },
        },
        "hex_to_hsl_for_convexity": {
            "description": "Converts  hex color code to  hsl color code",
            "parameters": {
                "hex": {
                    "type": "STRING",
                    "description": "",
                    "default": "ffffff",
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
    "DOMAINNAMESEARCH_API": {
        "whois_for_domain_name_search": {
            "description": "Perform WHOIS domain lookup.",
            "parameters": {
                "domain": {
                    "type": "STRING",
                    "description": "Domain for which to perform WHOIS.",
                    "default": "rapidapi.com",
                    "required": True,
                }
            },
        },
        "domain_search_for_domain_name_search": {
            "description": "Search for domains by keyword / query. Supports all 341 TLDs available on Google Domains. Each result includes availability information, pricing, quality aspects and more data available on Google Domains.",
            "parameters": {
                "query": {
                    "type": "STRING",
                    "description": "Search query / keyword.",
                    "default": "rapid",
                    "required": True,
                },
                "tlds": {
                    "type": "STRING",
                    "description": "TLDs to include in the search results, specified as a comma (,) separated list of TLDs.\n\n**e.g.** *com*\n**e.g.** *dev,info,net*",
                    "default": "",
                    "required": False,
                },
                "available_only": {
                    "type": "BOOLEAN",
                    "description": "Only return available domains.",
                    "default": "",
                    "required": False,
                },
                "max_price": {
                    "type": "NUMBER",
                    "description": "Return available domains up to a certain price, specified in the currency value of the `currency` parameter.",
                    "default": "",
                    "required": False,
                },
                "currency": {
                    "type": "STRING",
                    "description": "Set the currency for domain pricing. Specified as ISO 4217 currency code (e.g. GBP), For the full list of currency codes, see: [ISO 4217 currency codes](https://www.iban.com/currency-codes).",
                    "default": "USD",
                    "required": False,
                },
            },
        },
        "domain_availability_for_domain_name_search": {
            "description": "Check domain availability, including domain validation, expiration, prices, domain quality aspects (advantages / considerations) and more data.",
            "parameters": {
                "domain": {
                    "type": "STRING",
                    "description": "Domain for which to get availability info.",
                    "default": "example-domain-123.com",
                    "required": True,
                },
                "currency": {
                    "type": "STRING",
                    "description": "Set the currency for domain pricing. Specified as ISO 4217 currency code (e.g. GBP), For the full list of currency codes, see: [ISO 4217 currency codes](https://www.iban.com/currency-codes).",
                    "default": "USD",
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
    },
    "JIBBERJABBER_API": {
        "sentence_for_jibber_jabber": {
            "description": "Returns a single random **sentence**",
            "parameters": {
                "minimumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "numberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "wordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "minimumNumberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumNumberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "paragraph_for_jibber_jabber": {
            "description": "Returns a **paragraph** with random sentences",
            "parameters": {
                "minimumNumberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "wordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumNumberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "numberOfSentences": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "minimumNumberOfSentences": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumNumberOfSentences": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "numberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "minimumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "words_for_jibber_jabber": {
            "description": "Returns random **words**",
            "parameters": {
                "minimumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "numberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "wordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "sentences_for_jibber_jabber": {
            "description": "Returns some single random **sentence**",
            "parameters": {
                "maximumNumberOfSentences": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "minimumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "minimumNumberOfSentences": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "numberOfSentences": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumNumberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "minimumNumberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "numberOfWords": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "wordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "word_for_jibber_jabber": {
            "description": "Returns a random **word**",
            "parameters": {
                "minimumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "maximumWordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "wordLength": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
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
    },
    "PROXYPAGE_API": {
        "random_proxy_for_proxypage": {
            "description": "Get random proxy,\n\nchoose type and country",
            "parameters": {
                "type": {
                    "type": "STRING",
                    "description": "HTTP, HTTPS, SOCKS4, SOCKS5, CONNECT:25",
                    "default": "HTTP",
                    "required": True,
                },
                "country": {
                    "type": "STRING",
                    "description": "You can specify a country for a proxy that you want to be returened\n",
                    "default": "US",
                    "required": False,
                },
            },
        },
        "tier2_for_proxypage": {
            "description": "Tier 2 proxies\n\nEach proxy returned costs 1 credit\n\n\nWith our /v1/tier2 endpoint you can set different parameters for proxies that you need.\n\nYou can set type which is just your proxy type, either HTTP, HTTPS, SOCKS4, SOCKS5, CONNECT:25 (which is smtp proxy)\n\nfor limit set an integer that will tell us how many proxies you will need. Our users usually set a limit to avoid using too many credits.\n\nWith latency you can set an integer which will filter out all proxies that have a latency higher then specified.\n\nssl is a boolean parameter, you can filter out proxies that support ssl or don't\n\nis_anonymous is also a boolean statemet where you can filter anonymous proxies\n\ncountry is a parameter that you can use to set a country that you want.",
            "parameters": {
                "type": {
                    "type": "STRING",
                    "description": "",
                    "default": "HTTP",
                    "required": True,
                },
                "ssl": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "100",
                    "required": False,
                },
                "is_anonymous": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "country": {
                    "type": "STRING",
                    "description": "",
                    "default": "US",
                    "required": False,
                },
                "latency": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "tier1_for_proxypage": {
            "description": "List our tier 1 proxies with filters\nThis proxies are more comprehensively checked\n\n\nYou can set type which is just your proxy type, either HTTP, HTTPS\n\nfor limit set an integer that will tell us how many proxies you will need. Our users usually set a limit to avoid using too many credits.\n\nWith latency you can set an integer which will filter out all proxies that have a latency higher then specified.\n\nssl is a boolean parameter, you can filter out proxies that support ssl or don't\n\nis_anonymous is also a boolean statemet where you can filter anonymous proxies\n\ncountry is a parameter that you can use to set a country that you want.",
            "parameters": {
                "content_type": {
                    "type": "STRING",
                    "description": "HTTP, HTTPS, SOCKS4, SOCKS5, CONNECT:25",
                    "default": "HTTP",
                    "required": True,
                },
                "latency": {
                    "type": "NUMBER",
                    "description": "ms latency for a proxy, everything that is below that value is returned\n",
                    "default": "",
                    "required": False,
                },
                "country": {
                    "type": "STRING",
                    "description": "You can specify a country for a proxy that you want to be returened\n",
                    "default": "US",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Limit the number of proxies returned, helps you control how many credits can be used\n",
                    "default": "100",
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
    },
    "QRCODEGENERATOR_API": {
        "generate_advance_direct_image_for_qr_code_generator": {
            "description": "Generates a QR code as a direct image with additional settings. (NOTE: doesn't show correctly in RapidAPI)",
            "parameters": {
                "data": {
                    "type": "STRING",
                    "description": "",
                    "default": "1234",
                    "required": True,
                },
                "foreground_color": {
                    "type": "STRING",
                    "description": "",
                    "default": "FF2400",
                    "required": False,
                },
                "background_color": {
                    "type": "STRING",
                    "description": "",
                    "default": "00DBFF",
                    "required": False,
                },
                "size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "500",
                    "required": False,
                },
                "margin": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": False,
                },
                "label": {
                    "type": "STRING",
                    "description": "",
                    "default": "My label",
                    "required": False,
                },
                "label_size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "20",
                    "required": False,
                },
                "label_alignment": {
                    "type": "STRING",
                    "description": "",
                    "default": "center",
                    "required": False,
                },
            },
        },
        "generate_basic_base64_for_qr_code_generator": {
            "description": "Generates a QR code as base64 with limited settings.",
            "parameters": {
                "data": {
                    "type": "STRING",
                    "description": "",
                    "default": "1234",
                    "required": True,
                },
                "size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "500",
                    "required": False,
                },
            },
        },
        "generate_advance_base64_for_qr_code_generator": {
            "description": "Generates a QR code as base64 with additional settings.",
            "parameters": {
                "data": {
                    "type": "STRING",
                    "description": "",
                    "default": "1234",
                    "required": True,
                },
                "background_color": {
                    "type": "STRING",
                    "description": "",
                    "default": "00DBFF",
                    "required": False,
                },
                "foreground_color": {
                    "type": "STRING",
                    "description": "",
                    "default": "FF2400",
                    "required": False,
                },
                "label": {
                    "type": "STRING",
                    "description": "",
                    "default": "My label",
                    "required": False,
                },
                "margin": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": False,
                },
                "size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "500",
                    "required": False,
                },
                "label_size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "20",
                    "required": False,
                },
                "label_alignment": {
                    "type": "STRING",
                    "description": "",
                    "default": "center",
                    "required": False,
                },
            },
        },
        "generate_basic_direct_image_for_qr_code_generator": {
            "description": "Generates a QR code as a direct image with limited settings. (NOTE: doesn't show correctly in RapidAPI)",
            "parameters": {
                "data": {
                    "type": "STRING",
                    "description": "",
                    "default": "1234",
                    "required": True,
                },
                "size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "500",
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
    },
    "UNITCONVERSION_API": {
        "info_for_unitconversion": {
            "description": "List all supported units",
            "parameters": {},
        },
        "volume_from_to_number_for_unitconversion": {
            "description": "Volume unit conversions",
            "parameters": {
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "cubic kilometer",
                    "required": True,
                },
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "60",
                    "required": True,
                },
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "cubic meter",
                    "required": True,
                },
            },
        },
        "time_from_to_number_for_unitconversion": {
            "description": "Temperature unit conversions",
            "parameters": {
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "minute",
                    "required": True,
                },
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "50",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "second",
                    "required": True,
                },
            },
        },
        "temperature_from_to_number_for_unitconversion": {
            "description": "Temperature unit conversions",
            "parameters": {
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "celsius",
                    "required": True,
                },
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "90",
                    "required": True,
                },
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "fahrenheit",
                    "required": True,
                },
            },
        },
        "pressure_from_to_number_for_unitconversion": {
            "description": "Pressure unit conversions",
            "parameters": {
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "pascal",
                    "required": True,
                },
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "100",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "decibar",
                    "required": True,
                },
            },
        },
        "mass_from_to_number_for_unitconversion": {
            "description": "Mass unit conversions",
            "parameters": {
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "100",
                    "required": True,
                },
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "gram",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "pound",
                    "required": True,
                },
            },
        },
        "force_from_to_number_for_unitconversion": {
            "description": "Force unit conversions",
            "parameters": {
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "newton",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "dyne",
                    "required": True,
                },
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1000",
                    "required": True,
                },
            },
        },
        "data_from_to_number_for_unitconversion": {
            "description": "Data unit conversions",
            "parameters": {
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1024",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "byte",
                    "required": True,
                },
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "bit",
                    "required": True,
                },
            },
        },
        "area_from_to_number_for_unitconversion": {
            "description": "Area unit conversions",
            "parameters": {
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "square feet",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "acre",
                    "required": True,
                },
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": True,
                },
            },
        },
        "angle_from_to_number_for_unitconversion": {
            "description": "Angle unit conversions",
            "parameters": {
                "number": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": True,
                },
                "from": {
                    "type": "string",
                    "description": "",
                    "default": "radian",
                    "required": True,
                },
                "to": {
                    "type": "string",
                    "description": "",
                    "default": "turn",
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
    },
    "ALLPURPOSECOMPLEXCONVERTER_API": {
        "convert_number_to_speech_provide_any_integer_number_for_all_purpose_complex_converter": {
            "description": "Converting any integer number to Speech",
            "parameters": {
                "number": {
                    "type": "NUMBER",
                    "description": "Integer numbers only",
                    "default": "10",
                    "required": True,
                },
                "lang": {
                    "type": "string",
                    "description": "Language to convert number into",
                    "default": "en",
                    "required": True,
                },
            },
        },
        "convert_text_to_speech_provide_any_text_for_all_purpose_complex_converter": {
            "description": "Convert Any Text To Speech.",
            "parameters": {
                "text": {
                    "type": "string",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "lang": {
                    "type": "string",
                    "description": "Language to convert text into",
                    "default": "en",
                    "required": True,
                },
            },
        },
        "convert_numbers_to_words_provide_any_integer_number_for_all_purpose_complex_converter": {
            "description": "Convert any number to words.",
            "parameters": {
                "number": {
                    "type": "NUMBER",
                    "description": "Integer numbers only",
                    "default": "10",
                    "required": True,
                },
                "to_convert": {
                    "type": "string",
                    "description": "By Default the number will be converted to cardinal, if you wan to convert it into specific format such as ordinal, ordinal_num, year or currency than you can specify it here.",
                    "default": "ordinal",
                    "required": True,
                },
            },
        },
        "get_languages_for_all_purpose_complex_converter": {
            "description": "Get All The Supported Languages.",
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
