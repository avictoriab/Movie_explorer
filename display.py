from utils import format_value

def display_movie(movie):
    print(f"\nTítulo: {format_value(movie['title'])}")
    print(f"Fecha de estreno: {format_value(movie['release_date'])}")
    print(f"Puntuación: {format_value(movie['vote_average'])}")
    print(f"Sinopsis: {format_value(movie['overview'])}")

def display_movies(movies):
    print("\nResultados Obtenidos\n")
    
    for index, movie in enumerate(movies, start=1):
    
        print(f"{index}. {format_value(movie['title'])} ({format_value(movie['release_date'][:4])})")
