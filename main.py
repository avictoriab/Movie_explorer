from config import API_KEY
from api import search_movie

response = search_movie("Interstellar")

data = response.json()

#Imprimir todos los datos del diccionario
#print(data) 

#Inspeccionar el diccionario para conocer sus llaves principales
#print(data.keys())

#Imprimir la lista de peliculas usando la llave principal "results"
#print(data["results"])

#Imprimir cuantas peliculas encontro
#print(len(data["results"]))

#Acceder al primer elemento
first_movie = data["results"][0]
#Inspeccionar las llaves principales
print(first_movie.keys())
#Imprimir solo las llaves con la informacion deseada
print(f"""
Título: {first_movie['title']}
Fecha de estreno: {first_movie['release_date']}
Puntuación: {first_movie['vote_average']}
Sinopsis: {first_movie['overview']}
""")