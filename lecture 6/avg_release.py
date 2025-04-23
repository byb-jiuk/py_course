# Программа для расчета средней отметки студента.
def avg(score):
    """функция для вычисления среднего балла студента.
    Arguments:
    score - tuple - набор оценок.
    Returns:
    float - средний балл,  2 знака после запятой.
    """
    return round((sum(score)/len(score)), 2)

def new_grade(students_name, grade):
    """функция для добавления новой оценки студента.
    Arguments:
    students_name - str - имя, не менее 2-х символов.
    grade - int, mark
    Returns:
    True - если оценка добавлена успешно.
    False - если имя менье 2 символов.
    """
    if len(students_name) < 2:
        return False
    students_name = students_name.title()
    if students_name in students_grades:
        students_grades.update(students_grades.get(students_name) + (grade, ))
    else:
        students_grades.update({students_name:(grade, )})
    return True

def show_grades():
    """Функия, показывающая оценки студента."""
    print("show grades")
    for key, value in students_grades.items():
        print("name:", key)
        print("grades:", value)

def show_avg():
    """Функия показывающая средний бал студента."""
    print("show avg")
    for key, value in students_grades.items():
        print("name:", key)
        print("avg:", avg(value))


def main():
    """Функция позволяющая вызывать меню для создания отметки,
    средней отметки, показывать отметки и выход из программы."""
    msg = """1 - Новая оценка студента
    2 - Средняя оценка студента
    3 - Все отметки студента
    выход - выйти из программы."""
    operation = input(msg)
    while operation != "выход":
        match operation:
            case "1":
                name = input("Введите ФИО:")
                grade = int(input("Введите отметку:"))
                new_grade(name, grade)
            case "2":
                show_avg()
            case "3":
                show_grades()
            case _:
                print("Неверно")
        operation = input(msg)

students_grades = {}
main()
