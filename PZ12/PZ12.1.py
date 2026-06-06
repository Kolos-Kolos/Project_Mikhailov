#В последовательности на n целых чисел умножить все элементы на первый элемент

try:
    numbers = [2, 4, 6, 8, 10]

    first_number = numbers[0]

    result = [x * first_number for x in numbers]

    print("Исходная последовательность:")
    print(numbers)

    print("Новая последовательность:")
    print(result)

except Exception as error:
    print("Ошибка:", error)
