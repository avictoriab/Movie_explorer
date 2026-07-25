def format_value(value):
    print(f"DEBUG: {repr(value)}")
    if value:
        return value
    return "No disponible"


def get_poster_url(poster_path):

    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"

    return None