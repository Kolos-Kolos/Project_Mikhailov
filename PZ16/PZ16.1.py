#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.


class Book:
    # Конструктор класса
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Метод чтения книги
    def read(self):
        print("Книга читается.")

    # Метод записи книги
    def write(self):
        print("Книга записывается.")

    # Вывод информации о книге
    def show_info(self):
        print("Название:", self.title)
        print("Автор:", self.author)
        print("Количество страниц:", self.pages)


# Тестовый запуск

book1 = Book("Война и мир", "Л.Н. Толстой", 1225)

book1.show_info()
book1.read()
book1.write()
