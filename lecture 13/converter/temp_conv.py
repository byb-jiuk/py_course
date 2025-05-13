import xml.etree.ElementTree as ET


class TemperatureConverter:
    """
    Класс для конвертации температуры из градусов Цельсия в градусы Фаренгейта.
    """
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        """
        Конвертирует температуру из градусов Цельсия в градусы Фаренгейта.

        Args:
            temperature_in_celsius (float): Температура в градусах Цельсия.

        Returns:
            float: Температура в градусах Фаренгейта.
        """
        return 9.0/5.0 * temperature_in_celsius + 32
    

class ForecastXmlParser:
    """
    Класс для разбора XML-файла с прогнозом погоды и вывода информации о температуре.
    """
    def __init__(self, temperature_converter):
        """
        Инициализирует объект ForecastXmlParser.

        Args:
            temperature_converter (TemperatureConverter): Объект TemperatureConverter для конвертации температуры.
        """
        self.temperature_converter = temperature_converter

    def parse(self, file):
        """
        Разбирает XML-файл с прогнозом погоды и выводит информацию о температуре для каждого дня.

        Args:
            file_path (str): Путь к XML-файлу.
        """
        tree = ET.parse(file)
        root = tree.getroot()
        
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find('temperature_in_celsius').text)
            temperature_in_fahrenheit = round(self.temperature_converter.convert_celsius_to_fahrenheit(temperature_in_celsius), 1)
            print(f'{day}: {temperature_in_celsius} Celsius, {temperature_in_fahrenheit} Fahrenheit')
