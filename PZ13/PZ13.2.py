# В двумерном списке найти сумму элементов второй половины матрицы.

try:
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    print("Матрица:")

    for row in matrix:
        print(row)

    total = 0

    # Вторая половина столбцов
    half = len(matrix[0]) // 2

    for row in matrix:
        for element in row[half:]:
            total += element

    print("\nСумма элементов второй половины матрицы:", total)

except Exception as error:
    print("Ошибка:", error)
