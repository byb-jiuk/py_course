from lab_phonebook import Phone


def main():
    """
    Основная функция для запуска программы телефонной книги.
    """
    phone = Phone()  # Создаем экземпляр телефонной книги
    phone.import_contacts_from_csv("contacts.csv")  # Импортируем контакты из CSV-файла
    phone.show()  # Выводим список контактов
    phone.search_contacts()  # Ищем контакт
    phone.export_contacts_to_csv("exported_contacts.csv")  # Экспортируем контакты в новый CSV-файл

if __name__ == "__main__":
    main()  # Запускаем функцию main, если скрипт запущен напрямую
    