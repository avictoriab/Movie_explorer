import requests
from config import API_KEY, LANGUAGE

BASE_URL = "https://api.themoviedb.org/3"

def search_movie(movie_name):
    endpoint = "/search/movie"

    params = {
        "api_key": API_KEY,
        "query": movie_name,
        "language": LANGUAGE
    }

    response = requests.get(BASE_URL + endpoint, params=params)

    #Obtener la respuesta y convertirla en un diccionario
    data = response.json()

    #Agregar validacion a la lista "results"
    if not data["results"]:
        return None
   
    return data["results"]

def format_value(value):
    if value:
        return value
    return "No disponible"

def display_movie(movie):
    print(f"\nTítulo: {format_value(movie['title'])}")
    print(f"Fecha de estreno: {format_value(movie['release_date'])}")
    print(f"Puntuación: {format_value(movie['vote_average'])}")
    print(f"Sinopsis: {format_value(movie['overview'])}")