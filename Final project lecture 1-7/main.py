import best_film_logic as bf
import best_films_list as fl

def main():
    """Функция позволяющая вызывать меню для создания фильма, удаления,
    средней отметки, показывать лучший фильмы и выход из программы."""
    movies_grades = {}  # Initialize the dictionary here
    msg = """
1 - Ввести новый фильм или добавить оценку существующему
2 - Показать средние оценки фильмов
3 - Показать список фильмов
4 - Найти лучший фильм по оценке
5 - Удалить фильм из списка
exit - выйти из программы \n
Выберете пункт меню: """


    print("**********Меню*********** \n")

    operation = input(msg)
    print(" \n")
    while operation != "exit":
        match operation:
            case "1":
                name = input("Введите название фильма:")
                if name.title() not in movies_grades:  # Проверка на нахождение фильма в списке, чтобы не вводить заново его жанр, а только добавить оценку
                    genre = input("Введите жанр фильма:")
                else:
                    genre = movies_grades[name.title()]["genre"]
                    print(f"Фильм '{name}' уже существует. Жанр: {genre} \n")
                try:
                    grade = float(input("Введите оценку фильма: "))
                    fl.new_movie(movies_grades, name, genre, grade)
                    print("Запись успешно добавлена \n")  # Вызов функции ввода нового фильма
                except ValueError:
                    print("Ошибка: Введите числовое значение для отметки. \n")
            case "2":
                bf.show_avg(movies_grades)  # Вызов функции показа средних оценок фильмов
                print("")
            case "3":
                bf.show_movies(movies_grades)  # Вызов функции вывода списка фильмов
                print("") 
            case "4":
                bf.find_best_movie(movies_grades)  # Вызов функции для нахождения лучшего фильма по средней оценке
            case "5":
                name = input("Введите название фильма для удаления:")
                bf.delete_movie(movies_grades, name)  # Вызов функции удаление фильма
            case _:
                print("Неверно")
        print("**********Меню***********\n")
        operation = input(msg)
        print(" \n")


if __name__ == "__main__":
    main()
