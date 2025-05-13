from temp_conv import TemperatureConverter, ForecastXmlParser


def main():
    """
    Основная функция для запуска скрипта разбора XML-файла прогноза погоды.
    """
    temperature_converter = TemperatureConverter()
    forecast_xml_parser = ForecastXmlParser(temperature_converter)
    forecast_xml_parser.parse('forecast.xml')


if __name__ == "__main__":
    main()
    