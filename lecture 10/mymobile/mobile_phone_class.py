class MobilePhone:
    """
    Класс, представляющий мобильный телефон.

    Атрибуты:
        number (int): Номер телефона.
        switch (bool): Флаг, указывающий, включен ли телефон (True - включен, False - выключен).

    """
    def __init__(self, number):
        """Инициализирует объект MobilePhone."""
        self.number = number
        self.switch = False

    def turn_on(self):
        """Включает мобильный телефон."""
        self.switch = True
        return f"mobile phone {self.number} is turned on"

    def turn_off(self):
        """Выключает мобильный телефон."""
        self.switch = False
        return f"mobile phone {self.number} is turned off"

    def call(self, cally):
        """Звонит по указанному номеру."""
        if self.switch:
            return f"calling {cally}"
        else:
            return "Mobile phone is turned off. Can't make a call."
        
phone1 = MobilePhone("3752900770007")
phone2 = MobilePhone("375330011001")

print(phone1.turn_on())
print(phone2.turn_on())

print(phone2.call("2889933"))

print(phone1.turn_off())
print(phone2.turn_off())
