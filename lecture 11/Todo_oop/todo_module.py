class BadIdError(Exception):
    """
    Исключение, которое выбрасывается при обнаружении неверного идентификатора задачи.
    """
    def __init__(self, id, message):
        """
        Инициализирует исключение BadIdError.
        Args:
            id (int): Неверный идентификатор задачи.
            message (str): Сообщение об ошибке.
        """
        self.id = id
        self.message = message

    def __str__(self):
        """
        Возвращает строковое представление исключения BadIdError.
        """
        return f"BadIdError: id: {self.id}, message: {self.message}"


class BadNameError(Exception):
    """
    Исключение, которое выбрасывается при обнаружении неверного имени задачи.
    """
    def __init__(self, name, message):
        """
        Инициализирует исключение BadNameError.
        Args:
            name (str): Неверное имя задачи.
            message (str): Сообщение об ошибке.
        """
        self.name = name
        self.message = message

    def __str__(self):
        """
        Возвращает строковое представление исключения BadNameError.
        """
        return f"BadNameError: name: {self.name}, message: {self.message}"

class BadPriorityError(Exception):
    """
    Исключение, которое выбрасывается при обнаружении неверного приоритета задачи.
    """
    def __init__(self, priority, message):
        """
        Инициализирует исключение BadPriorityError.
        Args:
            priority (int): Неверный приоритет задачи.
            message (str): Сообщение об ошибке.
        """
        self.priority = priority
        self.message = message

    def __str__(self):
        """
        Возвращает строковое представление исключения BadPriorityError.
        """
        return f"BadPriorityError: priority: {self.priority}, message: {self.message}"

class Task:
    """
    Класс, представляющий задачу.
    """
    def __init__(self, tname, tpriority):
        """
        Инициализирует объект Task.
        Args:
            tname (str): Название задачи.
            tpriority (int): Приоритет задачи (от 1 до 100).
        """
        self.tname = tname
        self.tpriority = tpriority

    def __str__(self):
        """
        Возвращает строковое представление задачи.
        """
        return f"name: {self.tname} | priority: {self.tpriority}"

class TodoList:
    """
    Класс, представляющий список задач.
    """
    __auto_id = 1  # Приватный атрибут класса для автоматической генерации ID

    def __init__(self):
        """
        Инициализирует объект TodoList.
        """
        self.__task_storage: dict[int, Task] = {}  # Приватный атрибут экземпляра для хранения задач

    @classmethod
    def incrId(cls):
        """
        Увеличивает значение счетчика ID задач.
        """
        cls.__auto_id += 1

    @classmethod
    def getId(cls):
        """
        Возвращает текущее значение счетчика ID задач.
        """
        return cls.__auto_id

    def create(self, name, priority):
        """
        Создает новую задачу и добавляет ее в хранилище.
        Args:
            name (str): Название задачи.
            priority (int): Приоритет задачи (от 1 до 100).
        Raises:
            BadNameError: Если имя задачи менее 7 символов.
            BadPriorityError: Если приоритет задачи вне диапазона 1-100.
        """
        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")

        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")

        self.__task_storage[TodoList.getId()] = Task(name, priority)  # Добавляем задачу в хранилище
        TodoList.incrId()  # Увеличиваем счетчик ID
        return True

    def read(self, tid):
        """
        Читает задачу из хранилища по ID.
        Args:
            tid (int): ID задачи.
        Raises:
            BadIdError: Если ID задачи меньше 1 или не существует в хранилище.
        Returns:
            Task: Объект Task, соответствующий указанному ID.
        """
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")

        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")

        return self.__task_storage[tid]

    def read_all(self):
        """
        Читает все задачи из хранилища.
        Returns:
            str: Строка, содержащая информацию о всех задачах.
        """
        res_str = "номер задачи: значение\n"
        for k, v in self.__task_storage.items():
            res_str += f"{k} | {v}\n"

        return res_str

    def update(self, tid, name, priority):
        """
        Обновляет задачу в хранилище по ID.
        Args:
            tid (int): ID задачи.
            name (str): Новое название задачи.
            priority (int): Новый приоритет задачи (от 1 до 100).
        Raises:
            BadIdError: Если ID задачи меньше 1 или не существует в хранилище.
            BadNameError: Если имя задачи менее 7 символов.
            BadPriorityError: Если приоритет задачи вне диапазона 1-100.
        """
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")

        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")

        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")

        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")

        self.__task_storage[tid] = Task(name, priority)

        return True

    def delete(self, tid):
        """
        Удаляет задачу из хранилища по ID.
        Args:
            tid (int): ID задачи.
        Raises:
            BadIdError: Если ID задачи меньше 1 или не существует в хранилище.
        """
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")

        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")

        del self.__task_storage[tid]

        return True

class App():
    """
    Класс, представляющий приложение для управления списком задач.
    """
    def __init__(self, TodoListInst):
        """
        Инициализирует объект App.
        Args:
            TodoListInst (TodoList): Объект TodoList, которым управляет приложение.
        """
        self.__todolist = TodoListInst

    def Run(self):
        """
        Запускает интерактивный интерфейс для управления списком задач.
        """
        condition = input(App.condition_dispaly())  # Получаем ввод от пользователя

        while condition != "-1":  # Запускаем цикл, пока пользователь не введет "-1" для выхода
            try:
                if condition == "1":  # Если пользователь выбрал "1", добавляем новую задачу
                    name = input("Введите name: ")  # Запрашиваем имя задачи
                    priority = int(input("Введите priority: "))  # Запрашиваем приоритет задачи
                    self.__todolist.create(name, priority)  # Создаем задачу в TodoList
                elif condition == "2":  # Если пользователь выбрал "2", просматриваем список задач
                    print(self.__todolist.read_all())  # Выводим все задачи
                elif condition == "3":  # Если пользователь выбрал "3", просматриваем задачу по ID
                    tid = int(input("Введите id: "))  # Запрашиваем ID задачи
                    print(self.__todolist.read(tid))  # Выводим задачу по ID
                elif condition == "4":  # Если пользователь выбрал "4", обновляем задачу
                    tid = int(input("Введите id: "))  # Запрашиваем ID задачи
                    name = input("Введите name: ")  # Запрашиваем новое имя задачи
                    priority = int(input("Введите priority: "))  # Запрашиваем новый приоритет задачи
                    self.__todolist.update(tid, name, priority)  # Обновляем задачу
                elif condition == "5":  # Если пользователь выбрал "5", удаляем задачу
                    tid = int(input("Введите id: "))  # Запрашиваем ID задачи
                    self.__todolist.delete(tid)  # Удаляем задачу
                else:  # Если пользователь ввел некорректную команду
                    print("Неизвестная операция!")  # Выводим сообщение об ошибке
                    print(App.condition_dispaly())  # Показываем меню снова
            except BadIdError as e:  # Обрабатываем исключение BadIdError
                print("Проблема: ", e)  # Выводим сообщение об ошибке
            except BadNameError as e:  # Обрабатываем исключение BadNameError
                print("Проблема: ", e)  # Выводим сообщение об ошибке
            except BadPriorityError as e:  # Обрабатываем исключение BadPriorityError
                print("Проблема: ", e)  # Выводим сообщение об ошибке
            except Exception as e:  # Обрабатываем все остальные исключения
                print("Неизвестная проблема...!", e)  # Выводим сообщение об ошибке
            else:  # Если ни одно исключение не было выброшено
                print("Операция прошла успешно!")  # Выводим сообщение об успехе

            condition = input("Выберите операцию: ")  # Запрашиваем следующую операцию

        print("This is the end..")  # Выводим сообщение о завершении
        print("Bye Bye")  # Выводим прощальное сообщение

    @staticmethod
    def condition_dispaly():
        """
        Возвращает строку, содержащую меню для взаимодействия с пользователем.
        """
        return """
        Номер задачи (от 1)
        Имя задачи (не менее 7 символов)
        Приоритеты (от 1 до 100)

        1 - create - добавление новой задачи.
        2 - read_all - просмотр списка.
        3 - read - просмотр задачи по id.
        4 - update - обновление задачи по id.
        5 - delete - удаление задачи по id.
        -1 - exit - выход из программы.
        Введите номер пункта меню:
        """
