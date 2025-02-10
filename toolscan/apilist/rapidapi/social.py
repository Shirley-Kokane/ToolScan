RAPID_API = {
    "SOCIALMEDIADATATT_API": {
        "user_feed_video_posts_for_social_media_data_tt": {
            "description": "Get current user feed. \n\n- Before testing don't forget to fill out the username **OR** sec_uid inputs\n- Endpoint will return an array of objects with very useful metadata. \n- Direct urls to the video , statistics and more.",
            "parameters": {
                "username": {
                    "type": "STRING",
                    "description": "The influencer username. For example: **charlidamelio**\n\n- **NOTE:** By using **sec_uid** instead of the **username** request will be executed faster\n- To use **sec_uid** use input field **BELOW**",
                    "default": "amazon",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Limit the output number of records. \n\n- Default is 100\n- Max number is 500\n",
                    "default": "",
                    "required": False,
                },
                "max_cursor": {
                    "type": "NUMBER",
                    "description": "Pagination cursor. \nTo get more videos, paste here **max_cursor** value that you have received in previous request response.",
                    "default": "",
                    "required": False,
                },
                "sec_uid": {
                    "type": "STRING",
                    "description": "**NOTE:** By using **sec_uid**, request will be executed faster then if you will use username\n\n**NOTE:** **sec_uid** can be obtained from the **User Information** endpoint\n\n**NOTE:** **sec_uid** example: MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
                    "default": "",
                    "required": False,
                },
                "country": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
            },
        },
        "user_feed_video_posts_v2_for_social_media_data_tt": {
            "description": "Get user feed V2\n\nV2 - returns more data then older version of the endpoint",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "Limit the output number of records. \n\n- Default is 30\n- Max number is 30\n",
                    "default": "",
                    "required": False,
                },
                "max_cursor": {
                    "type": "NUMBER",
                    "description": "Pagination cursor. \nTo get more videos, paste here **max_cursor** value that you have received in previous request response.",
                    "default": "",
                    "required": False,
                },
                "username": {
                    "type": "STRING",
                    "description": "The influencer username. For example: **charlidamelio**\n",
                    "default": "tiktok",
                    "required": False,
                },
                "sec_uid": {
                    "type": "STRING",
                    "description": "**NOTE:** By using **sec_uid**, request will be executed faster then if you will use username\n\n**NOTE:** **sec_uid** can be obtained from the **User Information** endpoint\n\n**NOTE:** **sec_uid** example: MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
                    "default": "",
                    "required": False,
                },
            },
        },
        "real_time_hashtag_search_for_social_media_data_tt": {
            "description": "Search for hashtags by keyword",
            "parameters": {
                "keyword": {
                    "type": "STRING",
                    "description": "",
                    "default": "blah",
                    "required": True,
                }
            },
        },
        "direct_post_url_for_social_media_data_tt": {
            "description": "Get direct post url",
            "parameters": {
                "video": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "hashtag_feed_video_posts_for_social_media_data_tt": {
            "description": "Get current hashtag feed. \n\n- Before testing don't forget to fill out the name **OR** hashtag_id inputs\n- Endpoint will return an array of objects with very useful metadata. \n- Direct urls to the video , statistics and more.",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "Limit the output number of records. \n\n- Default is 100\n- Max number is 500\n",
                    "default": "",
                    "required": False,
                },
                "hashtag_id": {
                    "type": "STRING",
                    "description": "**NOTE:** By using **hashtag_id**, request will be executed faster then if you will use hashtag name\n\n**NOTE:** **hashtag_id** can be obtained from the **/live/hashtag** endpoint\n\n**NOTE:** **hashtag_id** example: 4232322",
                    "default": "",
                    "required": False,
                },
                "max_cursor": {
                    "type": "STRING",
                    "description": "Pagination cursor. \nTo get more videos, paste here **max_cursor** value that you have received in previous request response.",
                    "default": "",
                    "required": False,
                },
                "name": {
                    "type": "STRING",
                    "description": "Hashtag name. For example: **duett**\n\n- **NOTE:** By using **hashtag_id** instead of the hashtag **name** request will be executed faster\n- To use **hashtag_id** use input field **BELOW**",
                    "default": "summer",
                    "required": False,
                },
            },
        },
        "hashtag_metadata_information_for_social_media_data_tt": {
            "description": "Get hashtag metadata\n\nBasic informations as number of posts and etc",
            "parameters": {
                "hashtag": {
                    "type": "STRING",
                    "description": "Hashtag name. For example: **summer**",
                    "default": "summer",
                    "required": True,
                }
            },
        },
        "hashtag_metadata_information_v2_for_social_media_data_tt": {
            "description": "Get hashtag metadata V2\n\nV2 - returns more data then older version of the endpoint",
            "parameters": {
                "hashtag": {
                    "type": "STRING",
                    "description": "Hashtag name. For example: **summer**",
                    "default": "summer",
                    "required": True,
                }
            },
        },
        "trending_feed_video_posts_for_social_media_data_tt": {
            "description": "Get current trending feed. \n\n- Due to nature of this endpoint the **max_cursor** is not required. Each request can return different data by default\n- Endpoint will return an array of objects with very useful metadata. \n- Direct urls to the video , statistics and more.",
            "parameters": {
                "limit": {
                    "type": "NUMBER",
                    "description": "Limit the output number of records. \n\n- Default is 20\n- Max number is 20\n",
                    "default": "",
                    "required": False,
                }
            },
        },
        "hashtag_feed_video_posts_v2_for_social_media_data_tt": {
            "description": "Get hashtag feed V2. \n\nV2 - returns more data then older version of the endpoint, video without watermark and etc\n\n- Before testing don't forget to fill out the **name** query\n- Endpoint will return an array of objects with very useful metadata. \n- Direct urls to the video , statistics and more.",
            "parameters": {
                "name": {
                    "type": "STRING",
                    "description": "Hashtag name. For example: **duett**",
                    "default": "summer",
                    "required": False,
                },
                "limit": {
                    "type": "NUMBER",
                    "description": "Limit the output number of records. \n\n- Default is 20\n- Max number is 20\n",
                    "default": "",
                    "required": False,
                },
                "max_cursor": {
                    "type": "STRING",
                    "description": "Pagination cursor. \nTo get more videos, paste here **max_cursor** value that you have received in previous request response.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "video_post_metadata_for_social_media_data_tt": {
            "description": "Get single post metadata",
            "parameters": {
                "video": {
                    "type": "STRING",
                    "description": "Post url",
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
