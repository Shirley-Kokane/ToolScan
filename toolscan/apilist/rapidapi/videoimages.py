RAPID_API = {
    "APIVIDEO_API": {
        "get_analytics_videos_videoid_for_api_video": {
            "description": " ",
            "parameters": {
                "videoId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "metadata": {
                    "type": "ARRAY",
                    "description": "Metadata and Dynamic Metadata filter.\n(Dynamic metadata filter are available for  Business plans only)",
                    "default": "[]",
                    "required": False,
                },
                "period": {
                    "type": "STRING",
                    "description": "Period must have one of the following formats: \n\n- For a day : 2018-01-01,\n- For a week: 2018-W01, \n- For a month: 2018-01\n- For a year: 2018\n\nFor a range period: \n-  Date range: 2018-01-01/2018-01-15\n",
                    "default": "",
                    "required": False,
                },
                "currentPage": {
                    "type": "NUMBER",
                    "description": "Number of the page to display",
                    "default": 1,
                    "required": False,
                },
                "pageSize": {
                    "type": "NUMBER",
                    "description": "Expected number of items to display on the page. Might be lower on the last page",
                    "default": 25,
                    "required": False,
                },
            },
        },
        "get_analytics_sessions_sessionid_events_for_api_video": {
            "description": "Useful to track and measure video's engagement.",
            "parameters": {
                "sessionId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "currentPage": {
                    "type": "NUMBER",
                    "description": "Number of the page to display",
                    "default": 1,
                    "required": False,
                },
                "pageSize": {
                    "type": "NUMBER",
                    "description": "Expected number of items to display on the page. Might be lower on the last page",
                    "default": 25,
                    "required": False,
                },
            },
        },
        "get_videos_videoid_chapters_language_for_api_video": {
            "description": " ",
            "parameters": {
                "videoId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                },
                "language": {
                    "type": "STRING",
                    "description": "A valid BCP 47 language representation",
                    "default": "",
                    "required": True,
                },
            },
        },
        "get_players_for_api_video": {
            "description": " ",
            "parameters": {
                "pageSize": {
                    "type": "NUMBER",
                    "description": "Expected number of items to display on the page. Might be lower on the last page",
                    "default": 25,
                    "required": False,
                },
                "sortBy": {
                    "type": "STRING",
                    "description": "",
                    "default": "createdAt",
                    "required": False,
                },
                "currentPage": {
                    "type": "NUMBER",
                    "description": "Number of the page to display",
                    "default": 1,
                    "required": False,
                },
                "sortOrder": {
                    "type": "STRING",
                    "description": "Allowed: asc, desc",
                    "default": "asc",
                    "required": False,
                },
            },
        },
        "get_live_streams_livestreamid_for_api_video": {
            "description": " ",
            "parameters": {
                "liveStreamId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "list_videos_for_api_video": {
            "description": " ",
            "parameters": {
                "currentPage": {
                    "type": "NUMBER",
                    "description": "Search results page. Minimum value: 1",
                    "default": "1",
                    "required": False,
                },
                "liveStreamId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "sortOrder": {
                    "type": "STRING",
                    "description": "Allowed: asc, desc",
                    "default": "",
                    "required": False,
                },
                "tags": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "pageSize": {
                    "type": "NUMBER",
                    "description": "Results per page. Allowed values 1-100, default is 25.",
                    "default": "25",
                    "required": False,
                },
                "sortBy": {
                    "type": "STRING",
                    "description": "Allowed: publishedAt, title",
                    "default": "",
                    "required": False,
                },
                "description": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "title": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": False,
                },
                "metadata": {
                    "type": "ARRAY",
                    "description": "metadata[foo]=bar",
                    "default": "[]",
                    "required": False,
                },
            },
        },
        "get_video_status_for_api_video": {
            "description": "This API provides upload status & encoding status to determine when the video is uploaded or ready to playback.\n\nOnce encoding is completed, the response also lists the available stream qualities.",
            "parameters": {
                "videoId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "get_live_streams_for_api_video": {
            "description": " ",
            "parameters": {
                "currentPage": {
                    "type": "NUMBER",
                    "description": "Number of the page to display",
                    "default": 1,
                    "required": False,
                },
                "sortBy": {
                    "type": "STRING",
                    "description": "Allowed: createdAt, publishedAt, name",
                    "default": "",
                    "required": False,
                },
                "streamKey": {
                    "type": "STRING",
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
                "pageSize": {
                    "type": "NUMBER",
                    "description": "Expected number of items to display on the page. Might be lower on the last page",
                    "default": 25,
                    "required": False,
                },
            },
        },
        "get_players_playerid_for_api_video": {
            "description": " ",
            "parameters": {
                "playerId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
                    "required": True,
                }
            },
        },
        "get_video_for_api_video": {
            "description": "This call provides the same JSON information provided on video creation. For private videos, it will generate a unique token url.",
            "parameters": {
                "videoId": {
                    "type": "STRING",
                    "description": "",
                    "default": "",
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
    "ASPOSEIMAGINGCLOUD_API": {
        "converttifftofax_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "name": {
                    "type": "STRING",
                    "description": "Filename of image.",
                    "default": "",
                    "required": True,
                },
                "folder": {
                    "type": "STRING",
                    "description": "Folder with image to process.",
                    "default": "",
                    "required": False,
                },
                "storage": {
                    "type": "STRING",
                    "description": "Your Aspose Cloud Storage name.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "extractimagefeatures_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "imageId": {
                    "type": "STRING",
                    "description": "The image identifier.",
                    "default": "",
                    "required": True,
                },
                "searchContextId": {
                    "type": "STRING",
                    "description": "The search context identifier.",
                    "default": "",
                    "required": True,
                },
                "imageData": {
                    "type": "BINARY",
                    "description": "Input image",
                    "default": "",
                    "required": False,
                },
                "folder": {
                    "type": "STRING",
                    "description": "The folder.",
                    "default": "",
                    "required": False,
                },
                "storage": {
                    "type": "STRING",
                    "description": "The storage.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "modifyjpeg2000_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "name": {
                    "type": "STRING",
                    "description": "Filename of image.",
                    "default": "",
                    "required": True,
                },
                "comment": {
                    "type": "STRING",
                    "description": "The comment (can be either single or comma-separated).",
                    "default": "",
                    "required": True,
                },
                "storage": {
                    "type": "STRING",
                    "description": "Your Aspose Cloud Storage name.",
                    "default": "",
                    "required": False,
                },
                "fromScratch": {
                    "type": "BOOLEAN",
                    "description": "Specifies where additional parameters we do not support should be taken from. If this is true \u2013 they will be taken from default values for standard image, if it is false \u2013 they will be saved from current image. Default is false.",
                    "default": False,
                    "required": False,
                },
                "folder": {
                    "type": "STRING",
                    "description": "Folder with image to process.",
                    "default": "",
                    "required": False,
                },
                "codec": {
                    "type": "STRING",
                    "description": "The codec (j2k or jp2).",
                    "default": "j2k",
                    "required": False,
                },
            },
        },
        "findimageduplicates_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "searchContextId": {
                    "type": "STRING",
                    "description": "The search context identifier.",
                    "default": "",
                    "required": True,
                },
                "similarityThreshold": {
                    "type": "NUMBER",
                    "description": "The similarity threshold.",
                    "default": "",
                    "required": True,
                },
                "folder": {
                    "type": "STRING",
                    "description": "The folder.",
                    "default": "",
                    "required": False,
                },
                "storage": {
                    "type": "STRING",
                    "description": "The storage.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "rotateflipimage_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "method": {
                    "type": "STRING",
                    "description": "RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY).",
                    "default": "",
                    "required": True,
                },
                "name": {
                    "type": "STRING",
                    "description": "Filename of an image.",
                    "default": "",
                    "required": True,
                },
                "storage": {
                    "type": "STRING",
                    "description": "Your Aspose Cloud Storage name.",
                    "default": "",
                    "required": False,
                },
                "folder": {
                    "type": "STRING",
                    "description": "Folder with image to process.",
                    "default": "",
                    "required": False,
                },
                "format": {
                    "type": "STRING",
                    "description": "Resulting image format. Please, refer to https://docs.aspose.cloud/display/imagingcloud/Supported+File+Formats#SupportedFileFormats-CommonOperationsFormatSupportMap for possible use-cases.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "downloadfile_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "path": {
                    "type": "STRING",
                    "description": "File path e.g. '/folder/file.ext'",
                    "default": "",
                    "required": True,
                },
                "storageName": {
                    "type": "STRING",
                    "description": "Storage name",
                    "default": "",
                    "required": False,
                },
                "versionId": {
                    "type": "STRING",
                    "description": "File version ID to download",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getimageframe_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "name": {
                    "type": "STRING",
                    "description": "Filename of image.",
                    "default": "",
                    "required": True,
                },
                "frameId": {
                    "type": "NUMBER",
                    "description": "Number of a frame.",
                    "default": "",
                    "required": True,
                },
                "folder": {
                    "type": "STRING",
                    "description": "Folder with image to process.",
                    "default": "",
                    "required": False,
                },
                "x": {
                    "type": "NUMBER",
                    "description": "X position of start point for cropping rectangle.",
                    "default": "",
                    "required": False,
                },
                "rotateFlipMethod": {
                    "type": "STRING",
                    "description": "RotateFlip method (Rotate180FlipNone, Rotate180FlipX, Rotate180FlipXY, Rotate180FlipY, Rotate270FlipNone, Rotate270FlipX, Rotate270FlipXY, Rotate270FlipY, Rotate90FlipNone, Rotate90FlipX, Rotate90FlipXY, Rotate90FlipY, RotateNoneFlipNone, RotateNoneFlipX, RotateNoneFlipXY, RotateNoneFlipY). Default is RotateNoneFlipNone.",
                    "default": "",
                    "required": False,
                },
                "newHeight": {
                    "type": "NUMBER",
                    "description": "New height.",
                    "default": "",
                    "required": False,
                },
                "saveOtherFrames": {
                    "type": "BOOLEAN",
                    "description": "If result will include all other frames or just a specified frame.",
                    "default": False,
                    "required": False,
                },
                "storage": {
                    "type": "STRING",
                    "description": "Your Aspose Cloud Storage name.",
                    "default": "",
                    "required": False,
                },
                "newWidth": {
                    "type": "NUMBER",
                    "description": "New width.",
                    "default": "",
                    "required": False,
                },
                "rectWidth": {
                    "type": "NUMBER",
                    "description": "Width of cropping rectangle.",
                    "default": "",
                    "required": False,
                },
                "rectHeight": {
                    "type": "NUMBER",
                    "description": "Height of cropping rectangle.",
                    "default": "",
                    "required": False,
                },
                "y": {
                    "type": "NUMBER",
                    "description": "Y position of start point for cropping rectangle.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "objectexists_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "path": {
                    "type": "STRING",
                    "description": "File or folder path e.g. '/file.ext' or '/folder'",
                    "default": "",
                    "required": True,
                },
                "versionId": {
                    "type": "STRING",
                    "description": "File version ID",
                    "default": "",
                    "required": False,
                },
                "storageName": {
                    "type": "STRING",
                    "description": "Storage name",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getimagesearchstatus_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "searchContextId": {
                    "type": "STRING",
                    "description": "The search context identifier.",
                    "default": "",
                    "required": True,
                },
                "storage": {
                    "type": "STRING",
                    "description": "The storage.",
                    "default": "",
                    "required": False,
                },
                "folder": {
                    "type": "STRING",
                    "description": "The folder.",
                    "default": "",
                    "required": False,
                },
            },
        },
        "getimageframeproperties_for_aspose_imaging_cloud": {
            "description": " ",
            "parameters": {
                "name": {
                    "type": "STRING",
                    "description": "Filename with image.",
                    "default": "",
                    "required": True,
                },
                "frameId": {
                    "type": "NUMBER",
                    "description": "Number of a frame.",
                    "default": "",
                    "required": True,
                },
                "folder": {
                    "type": "STRING",
                    "description": "Folder with image to process.",
                    "default": "",
                    "required": False,
                },
                "storage": {
                    "type": "STRING",
                    "description": "Your Aspose Cloud Storage name.",
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
    "BINGVIDEOSEARCH_API": {
        "trending_for_bing_video_search": {
            "description": "Get currently trending videos.",
            "parameters": {},
        },
        "video_details_for_bing_video_search": {
            "description": "Get insights about a video, such as related videos.",
            "parameters": {
                "modules": {
                    "type": "STRING",
                    "description": "",
                    "default": "A comma-delimited list of one or more insights to request.",
                    "required": True,
                },
                "id": {
                    "type": "STRING",
                    "description": "",
                    "default": "An ID that uniquely identifies a video. The Video object's videoId field contains the ID that you set this parameter to.",
                    "required": True,
                },
            },
        },
        "video_search_for_bing_video_search": {
            "description": "Get videos relevant for a given query.",
            "parameters": {
                "q": {
                    "type": "STRING",
                    "description": "The user's search query string",
                    "default": "",
                    "required": True,
                },
                "safeSearch": {
                    "type": "STRING",
                    "description": "A filter used to filter results for adult content.",
                    "default": "",
                    "required": False,
                },
                "mkt": {
                    "type": "STRING",
                    "description": "The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form -. For example, en-US.\n\nFull list of supported markets:\nes-AR, en-AU, de-AT, nl-BE, fr-BE, pt-BR, en-CA, fr-CA, es-CL, da-DK, fi-FI, fr-FR, de-DE, zh-HK, en-IN, en-ID, en-IE, it-IT, ja-JP, ko-KR, en-MY, es-MX, nl-NL, en-NZ, no-NO, zh-CN, pl-PL, pt-PT, en-PH, ru-RU, ar-SA, en-ZA, es-ES, sv-SE, fr-CH, de-CH, zh-TW, tr-TR, en-GB, en-US, es-US",
                    "default": "",
                    "required": False,
                },
                "count": {
                    "type": "NUMBER",
                    "description": "The number of video results to return in the response. The actual number delivered may be less than requested.",
                    "default": "",
                    "required": False,
                },
                "offset": {
                    "type": "NUMBER",
                    "description": "The zero-based offset that indicates the number of video results to skip before returning results.",
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
    "MLEMAPI_API": {
        "new_mlem_for_mlemapi": {
            "description": "Returns one most recently published mlem image in JSON",
            "parameters": {},
        },
        "mlem_id_for_mlemapi": {
            "description": "Returns one mlem image by ID in JSON",
            "parameters": {
                "mlemid": {
                    "type": "NUMBER",
                    "description": "Mlem ID",
                    "default": "",
                    "required": True,
                }
            },
        },
        "tags_for_mlemapi": {
            "description": "Returns all tags in JSON",
            "parameters": {},
        },
        "random_mlem_for_mlemapi": {
            "description": "Returns one random mlem image in JSON",
            "parameters": {
                "brightness": {
                    "type": "STRING",
                    "description": "Image brightness: dark or bright",
                    "default": "",
                    "required": False,
                },
                "maxheight": {
                    "type": "NUMBER",
                    "description": "Maximum height",
                    "default": "",
                    "required": False,
                },
                "minwidth": {
                    "type": "NUMBER",
                    "description": "Maximum width",
                    "default": "",
                    "required": False,
                },
                "minheight": {
                    "type": "NUMBER",
                    "description": "Minimum height",
                    "default": "",
                    "required": False,
                },
                "tag": {
                    "type": "STRING",
                    "description": "Tag of mlem",
                    "default": "",
                    "required": False,
                },
                "maxwidth": {
                    "type": "NUMBER",
                    "description": "Minimum width",
                    "default": "",
                    "required": False,
                },
                "orientation": {
                    "type": "STRING",
                    "description": "Image orientation: square, landscape, portrait",
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
}
