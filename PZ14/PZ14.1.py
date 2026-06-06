# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов

import re

try:
    # Чтение файла
    with open('price.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Поиск цен
    prices = re.findall(r'\d+[.,]?\d*', text)

    print("Найденные цены:")
    for price in prices:
        print(price)

    print("\nКоличество цен:", len(prices))

except FileNotFoundError:
    print("Файл price.txt не найден.")

except Exception as error:
    print("Ошибка:", error)
