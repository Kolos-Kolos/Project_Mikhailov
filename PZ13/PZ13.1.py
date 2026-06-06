# В двумерном списке найти суммы элементов каждой строки и поместить их в новый
#массив. Выполнить замену элементов третьего столбца исходной матрицы на
#полученные суммы.

try:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Исходная матрица:")

    for row in matrix:
        print(row)

    # Суммы строк
    sums = [sum(row) for row in matrix]

    print("\nМассив сумм строк:")
    print(sums)

    # Замена третьего столбца
    for i in range(len(matrix)):
        matrix[i][2] = sums[i]

    print("\nРезультирующая матрица:")

    for row in matrix:
        print(row)

except Exception as error:
    print("Ошибка:", error)
