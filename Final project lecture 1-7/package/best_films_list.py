def new_movie(movies_grades, movie_name, genre, grade):
    """функция для добавления нового фильма."""
    if len(movie_name) < 2:
        return False
    movie_name = movie_name.title()
    if movie_name in movies_grades:
        movies_grades[movie_name]["grades"] += (grade,)
        return True
    else:
        movies_grades[movie_name] = {"genre": genre, "grades": (grade,)}
        return True
    