RAPID_API = {
    "LOCALBUSINESSDATA_API": {
        "business_reviews_for_local_business_data": {
            "description": "Get all business reviews. Supports pagination, query and several sort options.",
            "parameters": {
                "business_id": {
                    "type": "STRING",
                    "description": "Unique Business Id of the business for which to get reviews.",
                    "default": "0x89c259b5a9bd152b:0x31453e62a3be9f76",
                    "required": True,
                },
                "sort_by": {
                    "type": "ENUM",
                    "description": "How to sort the reviews in the results.\n\n**Allowed values**: *`most_relevant, newest, highest_ranking, lowest_ranking`*.\n\n**Default**: *`most_relevant`*",
                    "default": "",
                    "required": False,
                },
                "region": {
                    "type": "STRING",
                    "description": "Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\n\n**Default:** *`us`*",
                    "default": "us",
                    "required": False,
                },
                "language": {
                    "type": "STRING",
                    "description": "Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes .\n\n**Default**: *`en`*",
                    "default": "en",
                    "required": False,
                },
                "offset": {
                    "type": "NUMBER",
                    "description": "Number of business reviews to skip (for pagination/scrolling).\n\n**Default**: *`0`*",
                    "default": "",
                    "required": False,
                },
                "fields": {
                    "type": "STRING",
                    "description": "A comma separated list of review fields to include in the response (field projection). By default all fields are returned.\n\n**e.g.** `review_id,review_text,rating`",
                    "default": "",
                    "required": False,
                },
                "query": {
                    "type": "STRING",
                    "description": "Return reviews matching a text query.",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Maximum number of business reviews to return (1-150).\n\n**Default**: *`20`*",
                    "default": "5",
                    "required": False,
                },
            },
        },
        "business_photos_for_local_business_data": {
            "description": "Get all business photos.",
            "parameters": {
                "business_id": {
                    "type": "STRING",
                    "description": "Unique Business Id of the business for which to get photos.",
                    "default": "0x89c259b5a9bd152b:0x31453e62a3be9f76",
                    "required": True,
                },
                "fields": {
                    "type": "STRING",
                    "description": "A comma separated list of review fields to include in the response (field projection). By default all fields are returned.\n\n**e.g.** `type,photo_url`",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Maximum number of business photos to return (1-10000).\n\n**Default**: *`20`*",
                    "default": "5",
                    "required": False,
                },
                "region": {
                    "type": "STRING",
                    "description": "Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\n\n**Default:** *`us`*",
                    "default": "us",
                    "required": False,
                },
            },
        },
        "business_details_for_local_business_data": {
            "description": "Get full business details including emails and social contacts. Supports batching of up to 20 Business Ids.",
            "parameters": {
                "business_id": {
                    "type": "STRING",
                    "description": "Unique Business Id. Batching of up to 20 Business Ids are supported in a single request using a comma separated list (e.g. business_id=id1,id2).",
                    "default": "0x880fd393d427a591:0x8cba02d713a995ed",
                    "required": True,
                },
                "language": {
                    "type": "STRING",
                    "description": "Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes .\n\n**Default**: *`en`*",
                    "default": "en",
                    "required": False,
                },
                "fields": {
                    "type": "STRING",
                    "description": "A comma separated list of business fields to include in the response (field projection). By default all fields are returned.\n\n**e.g.** `business_id,type,phone_number,full_address`",
                    "default": "",
                    "required": False,
                },
                "extract_emails_and_contacts": {
                    "type": "BOOLEAN",
                    "description": "Whether to extract emails, contacts and social profiles for the business. In case true, businesses will be enriched with a `emails_and_contacts` field, potentially containing emails, phones, Facebook, LinkedIn, Instagram and other social profiles.\n\n**Default**: *`true`*",
                    "default": "true",
                    "required": False,
                },
                "extract_share_link": {
                    "type": "BOOLEAN",
                    "description": "Whether to extract place's share link for the business. In case true, businesses will be enriched with a `share_link` field containing a shortened Google URL for sharing (e.g. https://goo.gl/maps/oxndE8SVaNU5CV6p6).\n\n**Default**: *`false`*",
                    "default": "false",
                    "required": False,
                },
                "region": {
                    "type": "STRING",
                    "description": "Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\n\n**Default:** *`us`*",
                    "default": "us",
                    "required": False,
                },
                "coordinates": {
                    "type": "STRING",
                    "description": "Geographic coordinates of the location from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the `region` parameter).",
                    "default": "",
                    "required": False,
                },
            },
        },
        "search_in_area_for_local_business_data": {
            "description": 'Search businesses in a specific geographic area defined by a center coordinate point and zoom level. To see it in action, make a query on Google Maps, wait for the results to show, move the map or change the zoom and click "Search this area" at the top.',
            "parameters": {
                "lat": {
                    "type": "NUMBER",
                    "description": "Latitude of the center coordinate point of the area to search in.",
                    "default": 37.359428,
                    "required": True,
                },
                "zoom": {
                    "type": "STRING",
                    "description": "Zoom level on which to make the search (the search area / viewport is determined by lat, lng and zoom on a 1000x1000 screen).",
                    "default": "13",
                    "required": True,
                },
                "query": {
                    "type": "STRING",
                    "description": "Search query / keyword.\n\n**e.g.** `Bars and pubs`\n**e.g.** `Plumbers`",
                    "default": "pizza",
                    "required": True,
                },
                "lng": {
                    "type": "NUMBER",
                    "description": "Longitude of the center coordinate point of the area to search in.",
                    "default": -121.925337,
                    "required": True,
                },
                "region": {
                    "type": "STRING",
                    "description": "Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\n\n**Default:** *`us`*",
                    "default": "us",
                    "required": False,
                },
                "language": {
                    "type": "STRING",
                    "description": "Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes .\n\n**Default**: *`en`*",
                    "default": "en",
                    "required": False,
                },
                "subtypes": {
                    "type": "STRING",
                    "description": "Find businesses with specific subtypes, specified as a comma separated list of types (business categories). For the complete list of types, see https://daltonluka.com/blog/google-my-business-categories.\n\n**e.g.** `Plumber,Carpenter,Electrician`\n**e.g.** `Night club,Dance club,Bar,Pub`",
                    "default": "",
                    "required": False,
                },
                "fields": {
                    "type": "STRING",
                    "description": "A comma separated list of business fields to include in the response (field projection). By default all fields are returned.\n\n**e.g.** `business_id,type,phone_number,full_address`",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "STRING",
                    "description": "Maximum number of businesses to return (1-500).\n\n**Default**: *`20`*",
                    "default": "20",
                    "required": False,
                },
            },
        },
        "search_nearby_for_local_business_data": {
            "description": 'Search businesses near by specific geographic coordinates. To see it in action, right click on a specific point in the map on Google Maps and select "Search nearby", enter a query and search.',
            "parameters": {
                "query": {
                    "type": "STRING",
                    "description": "Search query / keyword.\n\n**e.g.** `Bars and pubs`\n**e.g.** `Plumbers`",
                    "default": "plumbers",
                    "required": True,
                },
                "lng": {
                    "type": "NUMBER",
                    "description": "Longitude of the geographic coordinates to search near by.",
                    "default": "-121.925337",
                    "required": True,
                },
                "lat": {
                    "type": "NUMBER",
                    "description": "Latitude of the geographic coordinates to search near by.",
                    "default": "37.359428",
                    "required": True,
                },
                "language": {
                    "type": "STRING",
                    "description": "Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes .\n\n**Default**: *`en`*",
                    "default": "en",
                    "required": False,
                },
                "subtypes": {
                    "type": "STRING",
                    "description": "Find businesses with specific subtypes, specified as a comma separated list of types (business categories). For the complete list of types, see https://daltonluka.com/blog/google-my-business-categories.\n\n**e.g.** `Plumber,Carpenter,Electrician`\n**e.g.** `Night club,Dance club,Bar,Pub`",
                    "default": "",
                    "required": False,
                },
                "fields": {
                    "type": "STRING",
                    "description": "A comma separated list of business fields to include in the response (field projection). By default all fields are returned.\n\n**e.g.** `business_id,type,phone_number,full_address`",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "STRING",
                    "description": "Maximum number of businesses to return (1-500).\n\n**Default**: *`20`*",
                    "default": "20",
                    "required": False,
                },
                "region": {
                    "type": "STRING",
                    "description": "Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\n\n**Default:** *`us`*",
                    "default": "us",
                    "required": False,
                },
            },
        },
        "search_for_local_business_data": {
            "description": "Search local businesses on Google Maps.",
            "parameters": {
                "query": {
                    "type": "STRING",
                    "description": "Search query / keyword.\n\n**e.g.** `Plumbers near New-York, USA`\n**e.g.** `Bars in 94102, USA`",
                    "default": "Hotels in San Francisco, USA",
                    "required": True,
                },
                "subtypes": {
                    "type": "STRING",
                    "description": "Find businesses with specific subtypes, specified as a comma separated list of types (business categories). For the complete list of types, see https://daltonluka.com/blog/google-my-business-categories.\n\n**e.g.** `Plumber,Carpenter,Electrician`\n**e.g.** `Night club,Dance club,Bar,Pub`",
                    "default": "",
                    "required": False,
                },
                "limit": {
                    "type": "STRING",
                    "description": "Maximum number of businesses to return (1-500).\n\n**Default**: *`20`*",
                    "default": "20",
                    "required": False,
                },
                "lat": {
                    "type": "STRING",
                    "description": "Latitude of the coordinates point from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the `region` parameter).",
                    "default": "37.359428",
                    "required": False,
                },
                "language": {
                    "type": "STRING",
                    "description": "Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes .\n\n**Default**: *`en`*",
                    "default": "en",
                    "required": False,
                },
                "lng": {
                    "type": "STRING",
                    "description": "Longitude of the coordinates point from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the `region` parameter).",
                    "default": "-121.925337",
                    "required": False,
                },
                "fields": {
                    "type": "STRING",
                    "description": "A comma separated list of business fields to include in the response (field projection). By default all fields are returned.\n\n**e.g.** `business_id,type,phone_number,full_address`",
                    "default": "",
                    "required": False,
                },
                "region": {
                    "type": "STRING",
                    "description": "Query Google Maps from a particular region or country. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\n\n**Default:** *`us`*",
                    "default": "us",
                    "required": False,
                },
                "zoom": {
                    "type": "STRING",
                    "description": "Zoom level on which to make the search (the viewport is determined by lat, lng and zoom).\n\n**Default**: *`13`*",
                    "default": "13",
                    "required": False,
                },
            },
        },
        "autocomplete_for_local_business_data": {
            "description": "Returns place/address, business and query predictions for text-based geographic queries.",
            "parameters": {
                "query": {
                    "type": "STRING",
                    "description": "Free-text geographic query.",
                    "default": "train sunnyval",
                    "required": True,
                },
                "language": {
                    "type": "STRING",
                    "description": "Set the language of the results. For a list of supported language codes see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 .\nDefault: `en`",
                    "default": "en",
                    "required": False,
                },
                "region": {
                    "type": "STRING",
                    "description": "Return results biased to a particular region. For a list of supported region/country codes see https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes (Alpha-2 code).\nDefault: `us`",
                    "default": "us",
                    "required": False,
                },
                "coordinates": {
                    "type": "STRING",
                    "description": "Geographic coordinates of the location from which the query is applied - recommended to use so that results are biased towards this location. Defaults to some central location in the region (see the `region` parameter).",
                    "default": "37.381315,-122.046148",
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
    "RANDOMCHUNKAPI_API": {
        "getrandomcolor_for_random_chunk_api": {
            "description": "Get a random color.",
            "parameters": {},
        },
        "getrandomquote_for_random_chunk_api": {
            "description": "Get a random quote.",
            "parameters": {
                "category": {
                    "type": "STRING",
                    "description": "",
                    "default": "life",
                    "required": False,
                },
                "count": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": False,
                },
            },
        },
        "getrandomarray_for_random_chunk_api": {
            "description": "Generate a random array with numbers, words or mixed values.",
            "parameters": {
                "data_type": {
                    "type": "STRING",
                    "description": "",
                    "default": "string",
                    "required": False,
                },
                "size": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "5",
                    "required": False,
                },
            },
        },
        "getrandomword_for_random_chunk_api": {
            "description": "Get random words.",
            "parameters": {
                "type": {
                    "type": "STRING",
                    "description": "",
                    "default": "adjective",
                    "required": False,
                },
                "count": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": False,
                },
            },
        },
        "getrandomtvshow_for_random_chunk_api": {
            "description": "Returns random TVshows.",
            "parameters": {},
        },
        "getrandommovie_for_random_chunk_api": {
            "description": "Returns random movies from over 1000 movie list.",
            "parameters": {
                "count": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "2",
                    "required": False,
                }
            },
        },
        "getrandomuser_for_random_chunk_api": {
            "description": "Returns random user data such as name, e-mail, etc.",
            "parameters": {
                "count": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "-2",
                    "required": False,
                }
            },
        },
        "getrandomname_for_random_chunk_api": {
            "description": "Returns random people's names..",
            "parameters": {
                "count": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "2",
                    "required": False,
                },
                "startingletter": {
                    "type": "STRING",
                    "description": "",
                    "default": "X",
                    "required": False,
                },
                "type": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getrandomdate_for_random_chunk_api": {
            "description": "Get random date.",
            "parameters": {
                "start": {
                    "type": "STRING",
                    "description": "",
                    "default": "2022-08-21",
                    "required": False,
                },
                "end": {
                    "type": "STRING",
                    "description": "",
                    "default": "2023-12-30",
                    "required": False,
                },
            },
        },
        "getrandompassword_for_random_chunk_api": {
            "description": "Get random password string.",
            "parameters": {
                "length": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "10",
                    "required": False,
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
    "REALTOR_API": {
        "property_details_for_realtor": {
            "description": "Get property details by  property ID  or by Address",
            "parameters": {
                "property_id": {
                    "type": "STRING",
                    "description": "",
                    "default": "1497548641",
                    "required": False,
                },
                "address": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "search_for_region_for_realtor": {
            "description": "Get location suggestions by keyword",
            "parameters": {
                "location": {
                    "type": "STRING",
                    "description": "",
                    "default": "santa monica",
                    "required": True,
                }
            },
        },
        "search_agents_for_realtor": {
            "description": "Search agents by city/zip",
            "parameters": {
                "location": {
                    "type": "STRING",
                    "description": "",
                    "default": "santa monica",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "1",
                    "required": False,
                },
                "price": {
                    "type": "STRING",
                    "description": "Price range\nexample for range between 50k to 2m : \n50000_2000000",
                    "default": "",
                    "required": False,
                },
                "agentname": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "lang": {
                    "type": "STRING",
                    "description": "[afrikaans\nalbanian\narabic\narmenian\nasl\nbengali\nbosnian\nbulgarian\nchinese\ncroatian\nczech\nDanish\ndutch\nEstonian\nfarsi\nfilipino\nfinnish\nfrench\ngaelic\ngeorgian\ngerman\ngreek\nhawaiian\nhebrew\nhindi\nhungarian\nindonesian\nitalian\njapanese\nkorean\nlao\nlatvian\nlithuanian\nmalay\nmandarin\nnepali\nnorwegian\npolish\nportuguese\npunjabi\nromanian\nrussian\nserbian\nsindhi\nsinghalese\nslovenian\nspanish\nswahili\nswedish\ntagalog\ntaiwanese\nthai\nturkish\nukrainian\nurdu\nvietnamese\nyugoslavian]",
                    "default": "",
                    "required": False,
                },
                "photo": {
                    "type": "BOOLEAN",
                    "description": "If the agent has a photo or not \n1 if yes\n0 if no",
                    "default": "1",
                    "required": False,
                },
                "rating": {
                    "type": "NUMBER",
                    "description": "Rating (between 1 and 5)",
                    "default": "",
                    "required": False,
                },
            },
        },
        "agent_details_for_realtor": {
            "description": "Get agent details by id",
            "parameters": {
                "id": {
                    "type": "STRING",
                    "description": "",
                    "default": "569e892a89a68901006bdb99",
                    "required": True,
                }
            },
        },
        "search_properties_for_sale_for_realtor": {
            "description": "Search properties for sale by Address, School, City, Zip or Neighborhood. Filter the results using different parameter filters",
            "parameters": {
                "location": {
                    "type": "STRING",
                    "description": "",
                    "default": "santa monica",
                    "required": True,
                },
                "beds-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "baths-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "year_built-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "year_built-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "list_date-min": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "open_house-max": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "has_tour": {
                    "type": "BOOLEAN",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "list_price-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "hoa_fee_optional-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "list_date-max": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "list_price-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "baths-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "open_house-min": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "type": {
                    "type": "STRING",
                    "description": "Property type comma-separated or empty for all types:\nsingle_family\nmulti_family\nland\ntownhomes\nduplex_triplex\nmobile\ncondos\ncondo_townhome_rowhome_coop\ncondo_townhome\nfarm\n",
                    "default": "single_family,condos",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Sort properties by :\nNewest_Listing \nHighest_Price \nLowest_Price\nOpen_House_Date\nRecently-Reduced\nLargest_Sqft\nLot_Size",
                    "default": "",
                    "required": False,
                },
                "beds-max": {
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
                "lot_sqft-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "lot_sqft-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "hoa_fee_optional-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "sqft-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "sqft-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "search_properties_for_rent_for_realtor": {
            "description": "Search properties for rent by location",
            "parameters": {
                "location": {
                    "type": "STRING",
                    "description": "",
                    "default": "santa monica",
                    "required": True,
                },
                "move_in_date-max": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "sqft-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "type": {
                    "type": "STRING",
                    "description": "Property type comma-separated or empty for all types:\nsingle_family\napartment\ntownhomes\ncondo_townhome_rowhome_coop\nduplex_triplex\ncondos\ncondo_townhome_rowhome_coop\ncondo_townhome\n",
                    "default": "",
                    "required": False,
                },
                "sqft-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "list_price-min": {
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
                "beds-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "sort": {
                    "type": "STRING",
                    "description": "Sort properties by :\nRecently_Added\nHighest_Price \nLowest_Price",
                    "default": "",
                    "required": False,
                },
                "threeDTours": {
                    "type": "BOOLEAN",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "baths-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "keyword": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "list_price-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "beds-max": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "baths-min": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "noFees": {
                    "type": "BOOLEAN",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "dogs": {
                    "type": "BOOLEAN",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "move_in_date-min": {
                    "type": "DATE (YYYY-MM-DD)",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "cats": {
                    "type": "BOOLEAN",
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
    "ZILLOWV2_API": {
        "zestimate_history_for_zillow_v2": {
            "description": "Zestimate history by zpid",
            "parameters": {
                "zpid": {
                    "type": "STRING",
                    "description": "",
                    "default": "20476226",
                    "required": True,
                }
            },
        },
        "photos_for_zillow_v2": {
            "description": "Returns a property's photos with different sizes and types.",
            "parameters": {
                "zpid": {
                    "type": "STRING",
                    "description": "",
                    "default": "2110846380",
                    "required": True,
                }
            },
        },
        "property_details_for_zillow_v2": {
            "description": "Get a property's details by its zpid",
            "parameters": {
                "zpid": {
                    "type": "STRING",
                    "description": "",
                    "default": "7594920",
                    "required": True,
                }
            },
        },
        "walk_transit_and_bike_score_for_zillow_v2": {
            "description": "Get Walk, Transit and Bike Score of a property by zpid",
            "parameters": {
                "zpid": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "20485700",
                    "required": False,
                }
            },
        },
        "rent_zestimate_and_comparable_properties_for_zillow_v2": {
            "description": "Returns a property's rent zestimate and it's comparable properties in the same area.",
            "parameters": {
                "address": {
                    "type": "STRING",
                    "description": "",
                    "default": "1545 Yale St, Santa Monica, CA 90404",
                    "required": True,
                },
                "bedrooms": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS] \nFilter for number of bedrooms: (To choose multiple values separate with comma eg : 0,1,2)\nPossible values:\n**0\n1\n2\n3\n4plus**\n",
                    "default": "",
                    "required": False,
                },
                "pets": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS] \nFilter for Pets: (To choose multiple values separate with comma eg : dogs,cats)\nPossible values:\n**any (Default)\ndogs\ncats**\n",
                    "default": "",
                    "required": False,
                },
                "amenities": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS] \nFilter for amenities: (To choose multiple values separate with comma eg : cooling,parking)\nPossible values:\n**any (Default)\ncooling\nheating\nparking**\n",
                    "default": "",
                    "required": False,
                },
                "laundry": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS] \nFilter for Laundry: (To choose multiple values separate with comma eg : inUnit,shared)\nPossible values:\n**any (Default)\ninUnit\nshared**\n",
                    "default": "",
                    "required": False,
                },
                "propertyTypes": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS] \nFilter for Property Types: (To choose multiple values separate with comma eg : house,condo)\nPossible values:\n**any (Default)\napartment\nhouse\ntownhouse\ncondo**\n",
                    "default": "",
                    "required": False,
                },
                "activeTypes": {
                    "type": "STRING",
                    "description": "SimilarFloorPlans filter:\nPossible values:\nany (Default)\nactive (Active Rentals)\ninactive (Inactive Rentals)\n",
                    "default": "",
                    "required": False,
                },
                "deactivatedDays": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS]\nFilter for inactive rentals within X days:\nPossible values:\n30 (Within 30 days (max))\n15 (Within 15 days)\n7 (Within 7 days)\n",
                    "default": "",
                    "required": False,
                },
                "activatedDays": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS]\nFilter for Active Rentals within X days:\nPossible values:\nany (Default)\n30 (Within 30 days)\n15 (Within 15 days)\n7 (Within 7 days)\n",
                    "default": "",
                    "required": False,
                },
                "distanceInMiles": {
                    "type": "STRING",
                    "description": "[SIMILARFLOORPLANS] \nFilter for distance in Miles: \nPossible values:\n**any\n1\n2\n3\n4\n5**\n",
                    "default": "",
                    "required": False,
                },
            },
        },
        "agent_s_active_listings_for_zillow_v2": {
            "description": "Get agent's active listings by zuid",
            "parameters": {
                "zuid": {
                    "type": "STRING",
                    "description": "",
                    "default": "X1-ZUz0nmomozy2o9_9bpwk",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "agent_reviews_for_zillow_v2": {
            "description": "Get agent reviews by the agent's zuid",
            "parameters": {
                "zuid": {
                    "type": "STRING",
                    "description": "",
                    "default": "X1-ZUz0nmomozy2o9_9bpwk",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "agent_s_rental_listings_for_zillow_v2": {
            "description": "Get agent's rental listings by zuid",
            "parameters": {
                "zuid": {
                    "type": "STRING",
                    "description": "",
                    "default": "X1-ZUz0nmomozy2o9_9bpwk",
                    "required": True,
                },
                "page": {
                    "type": "NUMBER",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "agent_details_by_username_for_zillow_v2": {
            "description": "Get agent's details by username(contact infos, active listings and reviews etc).\nPS : username is the profile link \nExample : \nusername :  Pardee-Properties\nfor https://www.zillow.com/profile/Pardee-Properties/",
            "parameters": {
                "username": {
                    "type": "STRING",
                    "description": "",
                    "default": "Pardee-Properties",
                    "required": True,
                }
            },
        },
        "search_for_agents_for_zillow_v2": {
            "description": "Search for agents by location and name",
            "parameters": {
                "location": {
                    "type": "STRING",
                    "description": "",
                    "default": "houston, tx",
                    "required": True,
                },
                "language": {
                    "type": "ENUM",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "specialties": {
                    "type": "ENUM",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "name": {
                    "type": "STRING",
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
