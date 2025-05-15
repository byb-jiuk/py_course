import logging
from lab_temp_model import BatterySimulation

FORMAT = '%(levelname)s - %(message)s'

def main():
    """
    Основная функция для настройки логгера и запуска симуляции батареи.
    """
    # Настройка логгера
    logger = logging.getLogger('battery.temperature')  # Получаем логгер
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler('battery_temperature.log', mode='w')  # Создаем обработчик для записи в файл
    handler.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень для записи в файл

    formatter = logging.Formatter(FORMAT)  # Создаем форматтер для сообщений
    handler.setFormatter(formatter)  # Устанавливаем форматтер для обработчика

    logger.addHandler(handler)  # Добавляем обработчик к логгеру

    # Создание и запуск симуляции
    battery_simulation = BatterySimulation(logger)
    battery_simulation.simulate_last_hour()

if __name__ == "__main__":
    main()
    print("I prefer to be a module")
else:
    print("I like to be a module")
