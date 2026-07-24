from api import search_movie, format_value, display_movie

while True:

    movie_name = input("Ingrese el nombre de la película: ").strip()

    if not movie_name:
        print("Debe ingresar un nombre de película")
    else:
        movies = search_movie(movie_name)

    print("\nResultados Obtenidos\n")

    for index, movie in enumerate(movies, start=1):

        print(f"{index}. {format_value(movie['title'])} ({format_value(movie['release_date'][:4])})")


    while True:

        try:
            selected_index = int(input("\nSeleccione una película: "))

            if 1 <= selected_index <= len(movies):
                break

            print(f"Ingrese un número entre 1 y {len(movies)}.")

        except ValueError:
            print("Debe ingresar un número.")

    selected_movie = movies[selected_index - 1]

    if movie:
        display_movie(selected_movie)
    else:
        print("No se encontraron resultados.")

    option = input("\n¿Desea buscar otra película? (s/n): ")

    if option.lower() != "s":
        break

