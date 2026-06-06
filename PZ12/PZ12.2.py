#Составить генератор (yield), который переведет символы строки из нижнего регистра в верхний.

try:
    text = "привет мир"

    def upper_generator(string):
        for symbol in string:
            yield symbol.upper()

    result = ""

    for letter in upper_generator(text):
        result += letter

    print("Исходная строка:")
    print(text)

    print("Результат:")
    print(result)

except Exception as error:
    print("Ошибка:", error)
