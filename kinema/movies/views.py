import requests
from .models import Movie
import json
import os
from dotenv import load_dotenv


def get_movie_info(movie_id):
    api_key = os.getenv("API_KEY")
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(base_url, headers=headers)
    data = response.json()

    movie = Movie()
    movie.title = data["title"]
    movie.Description = data["overview"]
    movie.Release_Date = data["release_date"]
    movie.Genre = data["genres"][1]
    movie.Category = data["adult"]
    movie.Language = data["original_language"]
    movie.Duration = data["runtime"]
    movie.Director = data["production_companies"][0]["name"]
    movie.country = data["production_countries"][0]["name"]
    movie.Poster = data["poster_path"]
    movie.save()
