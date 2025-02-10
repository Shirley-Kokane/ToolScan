MOVIE_API = {
      "get_search_movie" : {
      "description": "Search for a movie by name and return basic details",
      "parameters": {
          "movie_name": {
            "type": str,
            "description": "The name of the movie to search for.",
            "required" : True}},
      "returns": {
          "id": {
            "description": "The ID of the found movie."
          },
          "overview": {
            "description": "The overview description of the movie."
          },
          "title": {
            "description": "The title of the movie."
          }
        }},
      "get_movie_details" : {
      "description": "Get detailed information about a movie by ID",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required" : True
          }},
      "returns": {
          "budget": {
            "description": "The budget of the movie."
          },
          "genres": {
            "description": "The genres of the movie."
          },
          "revenue": {
            "description": "The revenue of the movie."
          },
          "vote_average": {
            "description": "The average vote score of the movie."
          },
          "release_date": {
            "description": "The release date of the movie."
          }
        }},
      "get_movie_production_companies":{
      "description": "Get the production companies of a movie by its ID",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required" : True
          }
      },
      "returns": {
          "production_companies": {
            "description": "The production companies of the movie."
          }}
    },
      "get_movie_production_countries" : {
      "description": "Get the production countries of a movie by its ID",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required": True
          }
        },
      "returns": {
          "production_countries": {
            "description": "The production countries of the movie."
          }
        }
      },
      "get_movie_cast" : 
    {
      "description": "Retrieve the list of the top 10 cast members from a movie by its ID.",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required":True
          }
        },
      "returns": {
          "cast": {
            "description": "List of the top 10 cast members."
          }
        }
      },
    "get_movie_crew": {
      "description": "Retrieve the list of crew members (limited to 10) from a movie by its ID. The list primarily includes Director, Producer, and Writer roles.",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required": True
          }
        },
      "returns": {
          "crew": {
            "description": "List of the top 10 of crew members"
          }
        }
      },
    "get_movie_keywords":
    {
      "description": "Get the keywords associated with a movie by ID",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required" : True
          }
        },
      "returns": {
          "keywords": {
            "description": "The keywords associated with the movie."
          }
        }
      },
    "get_search_person" : {
      "description": "Search for a person by name.",
      "parameters": {
          "person_name": {
            "type": str,
            "description": "The name of the person to search for.",
            "required" : True
          }
        },
      "returns": {
          "id": {
            "description": "The ID of the found person."
          },
          "name": {
            "description": "The name of the person."
          }
        }
      },
    "get_person_details" : {
      "description": "Get detailed information about a person by ID",
      "parameters": {
          "person_id": {
            "type": int,
            "description": "The ID of the person.",
            "required" : True
          }
        },
      "returns": {
          "biography": {
            "description": "The biography of the person."
          },
          "birthday": {
            "description": "The birthday of the person."
          },
          "place_of_birth": {
            "description": "The place of birth of the person."
          }
        }
      },
    "get_person_cast" : {
      "description": "Retrieve the top 10 movie cast roles of a person by their ID",
      "parameters": {
          "person_id": {
            "type": int,
            "description": "The ID of the person.",
            "required" : True
          }
        },
      "returns": {
          "cast": {
            "description": "A list of movies where the person has acted, limited to top 10"
          }
        }
      },
    "get_person_crew" : {
      "description": "Retrieve the top 10 movie crew roles of a person by their ID",
      "parameters": {
          "person_id": {
            "type": int,
            "description": "The ID of the person.",
            "required" : True
          }
        },
      "returns": {
          "crew": {
            "description": "A list of movies where the person has participated as crew, limited to top 10"
          }}},
    "get_person_external_ids" : {
      "description": "Get the external ids for a person by ID",
      "parameters": {
          "person_id": {
            "type": int,
            "description": "The ID of the person.",
            "required" : True
          }
        },
      "returns": {
          "imdb_id": {
            "description": "The IMDB id of the person."
          },
          "facebook_id": {
            "description": "The Facebook id of the person."
          },
          "instagram_id": {
            "description": "The Instagram id of the person."
          },
          "twitter_id": {
            "description": "The Twitter id of the person."
          }}},
    "get_movie_alternative_titles" : {
      "description": "Get the alternative titles for a movie by ID",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required" : True
          }
        },
      "returns": {
          "titles": {
            "description": "The alternative titles of the movie."
          },
          "id": {
            "description": "The ID of the movie."
          }
        }
      },
    "get_movie_translation" : {
      "description": "Get the description translation for a movie by ID",
      "parameters": {
          "movie_id": {
            "type": int,
            "description": "The ID of the movie.",
            "required" : True
          }
        },
      "returns": {
          "translations": {
            "description": "The description translation of the movie."
          },
          "id": {
            "description": "The ID of the movie."
          }
        }
      },
    "check_valid_actions" : 
    {
      "description": "Get supported actions for current tool.",
      "parameters": {},
      "returns": {
          "actions": {
            "type": "array",
            "description": "Supported actions for current tool."
          }
        }
      },
    "finish" : 
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