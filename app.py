import streamlit as st
from api import search_movie
from display_streamlit import display_movies, display_movie

st.title("🎬 Movie Finder")
st.write("Busca información sobre tus películas favoritas.")

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

movie_name = st.text_input("Nombre de la película")

if st.button("Buscar"):

    movies = search_movie(movie_name)

    if not movies:
        st.warning("No se encontraron coincidencias.")
    else:
        st.session_state.movies = movies
        st.session_state.selected_movie = None


if st.session_state.selected_movie:
    display_movie(st.session_state.selected_movie)
    
elif "movies" in st.session_state:
        display_movies(st.session_state.movies)