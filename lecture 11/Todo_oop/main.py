from todo_module import App, TodoList

def main():
    """
    Функция main создает экземпляр TodoList и App, а затем запускает приложение.
    """
    td1 = TodoList()  # Создаем экземпляр TodoList
    app = App(td1)  # Создаем экземпляр App, передавая ему TodoList
    app.Run()  # Запускаем приложение

if __name__ == "__main__":
    main()  # Запускаем функцию main, если этот скрипт запускается напрямую
