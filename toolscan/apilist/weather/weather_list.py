WEATHER_API = {
  "get_user_current_date" : {
      "description": "Get the user's current date.",
      "parameters": {},
      "returns": {
        "type": str,
        "description": "The current date in 'YYYY-MM-DD' format."
      }
    },
    "get_user_current_location" : 
    {
      "description": "Get the user's current city.",
      "parameters": {},
      "returns": {
        "type": str,
        "description": "The user's current city."
      }
    },
    "get_historical_temp" : 
    {
      "description": "Get historical temperature data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the historical data (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type": str,
            "description": "The end date of the historical data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Historical temperature data."
      }
    },
    "get_historical_rain" : 
    {
      "description": "Get historical rainfall data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the historical data (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type": str,
            "description": "The end date of the historical data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Historical rainfall data."
      }},
    "get_historical_snow":
    {
      "description": "Get historical snowfall data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the historical data (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type": str,
            "description": "The end date of the historical data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Historical snowfall data."
      }},
    "get_snow_forecast" : 
    {
      "description": "Get snowfall forecast data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the forecast (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type":str,
            "description": "The end date of the forecast (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Snowfall forecast data."
      }
    },
    "get_current_snow":
    {
      "description": "Get current snowfall data for a specified location and date.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "current_date": {
            "type": str,
            "description": "The current date to retrieve snowfall data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Current snowfall data."
      }
    },
    "get_current_temp" : 
    {
      "description": "Get current temperature data for a specified location and date.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "current_date": {
            "type": str,
            "description": "The current date to retrieve temperature data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Current temperature data."
      }
    },
    "get_latitude_longitude" : 
    {
      "description": "Get latitude and longitude information for a specified location name.",
      "parameters": {
          "name": {
            "type": str,
            "description": "The name of the location. (e.g., city name)",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "latitude and longitude information for the specified location."
      }},
    "get_elevation":
    {
      "description": "Get elevation data for a specified location.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Elevation data for the specified location."
      }},
    "get_temp_forecast":
    {
      "description": "Get temperature forecast data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the forecast (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type": str,
            "description": "The end date of the forecast (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Temperature forecast data."
      }
    },
    "get_rain_forecast" :
    {
      "description": "Get rainfall forecast data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the forecast (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type": str,
            "description": "The end date of the forecast (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Rainfall forecast data."
      }
    },
    "get_current_rain" : 
    {
      "description": "Get current rainfall data for a specified location and date.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "current_date": {
            "type": str,
            "description": "The current date to retrieve rainfall data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Current rainfall data."
      }},
    "get_distance" : 
    {
      "description": "Calculate the distance between two sets of latitude and longitude coordinates.",
      "parameters": {
          "latitude1": {
            "type": float,
            "description": "The latitude of the first location.",
            "required" : True
          },
          "longitude1": {
            "type": float,
            "description": "The longitude of the first location.",
            "required" : True
          },
          "latitude2": {
            "type": float,
            "description": "The latitude of the second location.",
            "required" : True
          },
          "longitude2": {
            "type": float,
            "description": "The longitude of the second location.",
            "required" : True
          }
        },
      "returns": {
        "type": "number",
        "description": "The distance between the two sets of coordinates in kilometers."
      }},
    "get_historical_air_quality_index" : {
      "description": "Get historical air quality index data for a specified location and date range.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "start_date": {
            "type": str,
            "description": "The start date of the historical data (YYYY-MM-DD).",
            "required" : True
          },
          "end_date": {
            "type": str,
            "description": "The end date of the historical data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Historical air quality index (PM2.5) data."
      }},
    "get_current_air_quality_index" : {
      "description": "Get current air quality index data for a specified location and date.",
      "parameters": {
          "latitude": {
            "type": float,
            "description": "The latitude of the location.",
            "required" : True
          },
          "longitude": {
            "type": float,
            "description": "The longitude of the location.",
            "required" : True
          },
          "current_date": {
            "type": str,
            "description": "The current date to retrieve air quality index data (YYYY-MM-DD).",
            "required" : True
          }
        },
      "returns": {
        "type": "object",
        "description": "Current air quality index (PM2.5) data."
      }},
    "get_air_quality_level" :  {
      "description": "Determine the air quality level based on the air quality index (AQI).",
      "parameters": {
          "air_quality_index": {
            "type": int,
            "description": "The air quality index (AQI) value.",
            "required" : True
          }
        },
      "returns": {
        "type": "string",
        "description": "The air quality level, which can be 'good', 'fair', 'moderate', 'poor', 'very poor', or 'extremely poor'."
      }},
    "check_valid_actions" : {
      "description": "Get supported actions for current tool.",
      "parameters": {},
      "returns": {
          "actions": {
            "type": "array",
            "description": "Supported actions for current tool."
          }
        }
      },
    "finish":
    {
      "description": "Return an answer and finish the task",
      "parameters": {
          "answer": {
            "type": [
              "string",
              "number",
              "array"
            ],
            "description": "The answer to be returned",
            "required" : True
          }
        }
      }
}