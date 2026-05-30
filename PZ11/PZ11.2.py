#2. Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

import string

try:
    upper_count = 0

    # Вывод содержимого файла и подсчёт заглавных букв
    with open('text18-16.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    print('Содержимое файла:\n')
    print(text)

    for symbol in text:
        if symbol.isupper():
            upper_count += 1

    print('\nКоличество букв в верхнем регистре:', upper_count)

    # Замена знаков пунктуации на !
    new_text = ''

    for symbol in text:
        if symbol in string.punctuation + '«»—…':
            new_text += '!'
        else:
            new_text += symbol

    # Запись результата в новый файл
    with open('text18-16-result.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)

    print('Файл text18-16-result.txt успешно создан.')

except FileNotFoundError:
    print('Ошибка: файл text18-16.txt не найден.')

except Exception as error:
    print(f'Неизвестная ошибка: {error}')
