import logging
import random

format = '%(levelname)s - %(message)s'

class BatterySimulation:
    """
    Класс для симуляции работы батареи и записи данных о температуре в лог.
    """
    def __init__(self, logger):
        """
        Инициализирует объект BatterySimulation.

        Args:
            logger (logging.Logger): Объект логгера для записи сообщений.
        """
        self.logger = logger

    def simulate_last_hour(self):
        """
        Симулирует изменение температуры батареи в течение часа и записывает данные в лог.
        """
        for minute in range(1, 60 +1):
            temperature = random.randint(20, 40)  # Генерируем случайную температуру

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))  # Записываем в лог с уровнем DEBUG
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning('{0} C'.format(temperature))  # Записываем в лог с уровнем WARNING
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))  # Записываем в лог с уровнем CRITICAL
            else:
                raise Exception('Temperature out of range.')  # Выбрасываем исключение, если температура вне диапазона
            
if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")
