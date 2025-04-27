def avg(score):
    """функция для вычисления средней отметки фильма."""
    return round((sum(score)/len(score)), 2)


def show_movies(movies_grades):
    """Функия, показывающая оценки фильма."""
    print("Список фильмов \n")
    for key, value in movies_grades.items():
        print("Название фильма:", key)
        print("Жанр фильма:", value["genre"])
        print("Оценки:", value["grades"])

def show_avg(movies_grades):
    """Функия показывающая средний бал фильмов."""
    print("Средние оценки фильмов \n")
    for key, value in movies_grades.items():
        print("Название фильма:", key)
        print("Средняя оценка фильма:", avg(value["grades"]))

def find_best_movie(movies_grades):
    """Функция для нахождения фильма с лучшей средней оценкой."""
    best_movie = None
    best_avg = -1
    for key, value in movies_grades.items():
        current_avg = avg(value["grades"])
        if current_avg > best_avg:
            best_avg = current_avg
            best_movie = key
    if best_movie:
        print(f"Лучший фильм: {best_movie} (Жанр: {movies_grades[best_movie]['genre']}, Средняя оценка: {best_avg}) \n")
    else:
        print("Нет фильмов в списке. \n")

def delete_movie(movies_grades, movie_name):
    """Функция для удаления фильма из списка."""
    movie_name = movie_name.title()
    if movie_name in movies_grades:
        del movies_grades[movie_name]
        print(f"Фильм '{movie_name}' успешно удален. \n")
    else:
        print(f"Фильм '{movie_name}' не найден в списке. \n")
