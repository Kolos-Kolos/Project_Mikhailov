# Вариант 16.
#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Положительные числа:
#Количество положительных чисел:
#Отрицательные числа:
#Количество отрицательных чисел:
#2. Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».

try:
    # Исходные данные
    numbers = [-15, 24, -8, 10, 35, -12, 7, -4, 18]

    # Запись исходных данных в файл
    with open('data_16_1.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(map(str, numbers)))

    # Чтение данных из файла
    with open('data_16_1.txt', 'r', encoding='utf-8') as file:
        data = file.read().split()

    numbers = [int(x) for x in data]

    positive_numbers = [x for x in numbers if x > 0]
    negative_numbers = [x for x in numbers if x < 0]

    # Формирование нового файла
    with open('result_16_1.txt', 'w', encoding='utf-8') as file:
        file.write('Исходные данные:\n')
        file.write(' '.join(map(str, numbers)))

        file.write('\n\nКоличество элементов:\n')
        file.write(str(len(numbers)))

        file.write('\n\nПоложительные числа:\n')
        file.write(' '.join(map(str, positive_numbers)))

        file.write('\n\nКоличество положительных чисел:\n')
        file.write(str(len(positive_numbers)))

        file.write('\n\nОтрицательные числа:\n')
        file.write(' '.join(map(str, negative_numbers)))

        file.write('\n\nКоличество отрицательных чисел:\n')
        file.write(str(len(negative_numbers)))

    print('Файл result_16_1.txt успешно создан.')

except FileNotFoundError:
    print('Ошибка: файл не найден.')

except ValueError:
    print('Ошибка: некорректные данные в файле.')

except Exception as error:
    print(f'Неизвестная ошибка: {error}')
