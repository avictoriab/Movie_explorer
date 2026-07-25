import streamlit as st
from utils import format_value, get_poster_url

def display_movies(movies):

    st.subheader("Resultados")

    for movie in movies:

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"### 🎬 {movie['title']}")
                st.write(f"📅 {format_value(movie['release_date'])}")
                st.write(f"⭐ {format_value(movie['vote_average'])}")

                if st.button("Ver detalles", key=movie["id"]):
                    st.session_state.selected_movie = movie
                    st.rerun()

            with col2:
                poster_url = get_poster_url(movie["poster_path"])

                if poster_url:
                    st.image(poster_url)
                else:
                    st.write("Sin poster")
                
def display_movie(movie):

    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:
        
        poster_url = get_poster_url(movie["poster_path"])

        if poster_url:
            st.image(poster_url, width=250)
        else:
            st.write("Sin poster")

        if st.button("← Volver a resultados"):
            st.session_state.selected_movie = None
            st.rerun()
            st.stop()

    with col2:

        st.header(movie["title"])

        st.write(
            f"📅 Fecha de estreno: {format_value(movie['release_date'])}"
        )

        st.write(
            f"⭐ Puntuación: {format_value(movie['vote_average'])}"
        )

        st.subheader("Sinopsis")
        st.write(format_value(movie["overview"]))

        
 
