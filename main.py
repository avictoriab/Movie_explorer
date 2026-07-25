from api import search_movie
from display import display_movie, display_movies

while True:

    movie_name = input("Ingrese el nombre de la película: ").strip()

    if not movie_name: 
        print("Debe ingresar un nombre de película")
        continue
   
    movies = search_movie(movie_name)

    if not movies:
        print("No hay coincidencias")
        continue

    display_movies(movies)
    
    while True:

        try:
            selected_index = int(input("\nSeleccione una película: "))

            if 1 <= selected_index <= len(movies):
                break

            print(f"Ingrese un número entre 1 y {len(movies)}.")

        except ValueError:
            print("Debe ingresar un número.")

    selected_movie = movies[selected_index - 1]

    display_movie(selected_movie)

    option = input("\n¿Desea buscar otra película? (s/n): ")

    if option.lower() != "s":
        break

    
        

