import csv


class PhoneContact:
    """
    Класс, представляющий контакт в телефонной книге.
    """
    def __init__(self, name, phone):
        """
        Инициализирует объект PhoneContact.

        Args:
            name (str): Имя контакта.
            phone (str): Номер телефона контакта.
        """
        self.name = name
        self.phone = phone

    def __str__(self):
        """
        Возвращает строковое представление контакта.
        """
        return f"Contact: {self.name}:{self.phone}"  # Форматированная строка с информацией о контакте
    

class Phone:
    """
    Класс, представляющий телефонную книгу.
    """
    def __init__(self):
        """
        Инициализирует объект Phone.
        """
        self.contacts = []  # Список для хранения объектов PhoneContact

    def show(self):
        """
        Выводит список контактов в консоль.
        """
        print("Список контактов:")
        for contact in self.contacts:  # Перебираем контакты в списке
            print(contact)  # Выводим информацию о контакте

    def import_contacts_from_csv(self, file):
        """
        Импортирует контакты из CSV-файла.

        Args:
            file (str): Путь к CSV-файлу.
        """
        print("Импортирую контакты.")
        with open(file, newline="") as csvfile:  # Открываем CSV-файл для чтения
            fieldnames = ["Name", "Phone"]  # Определяем имена столбцов
            reader = csv.DictReader(csvfile, fieldnames)  # Создаем объект DictReader для чтения данных

            for row in reader:
                self.contacts.append(PhoneContact(row["Name"], row["Phone"]))  # Создаем объект PhoneContact и добавляем в список

        print("Импорт был успешен...")

    def export_contacts_to_csv(self, file):
        """
        Экспортирует контакты в CSV-файл.

        Args:
            file (str): Путь к CSV-файлу.
        """
        print("Экспортирую контакты.")
        with open(file, "w", newline="") as csvfile:  # Открываем CSV-файл для записи
            writer = csv.writer(csvfile, delimiter="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)  # Создаем объект writer для записи данных

            for contact in self.contacts:  # Перебираем контакты в списке
                writer.writerow([contact.name, contact.phone])  # Записываем информацию о контакте в CSV-файл
        print("Экспорт был успешен...")
    
    def search_contacts(self):
        """
        Поиск контакта по имени или номеру телефона.
        """
        phrase = input("Search contacts: ")  # Запрашиваем фразу для поиска
        print("Поиск контакта по фразе:")
        count = 0  # Счетчик найденных контактов
        for contact in self.contacts:  # Перебираем контакты в списке
            if phrase.lower() in contact.name.lower() or phrase in contact.phone:  # Проверяем, содержит ли имя или номер телефона фразу
                print(f"Найден контакт: {contact.name} {contact.phone}")   # Выводим информацию о контакте
                count += 1  # Увеличиваем счетчик
            if count == 0:  # Если контакты не найдены
                print("Контакт не найден!")  # Выводим сообщение
