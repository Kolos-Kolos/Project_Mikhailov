# Базовый класс "Фрукт"
class Fruit:
    # Конструктор класса
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # Вывод информации о фрукте
    def show_info(self):
        print("Название:", self.name)
        print("Вес:", self.weight, "г")


# Класс "Яблоко", наследуется от Fruit
class Apple(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

    def show_info(self):
        super().show_info()
        print("Цвет:", self.color)


# Класс "Апельсин", наследуется от Fruit
class Orange(Fruit):
    def __init__(self, name, weight, color):
        super().__init__(name, weight)
        self.color = color

    def show_info(self):
        super().show_info()
        print("Цвет:", self.color)


# Тестовый запуск

apple = Apple("Яблоко", 180, "Красный")
orange = Orange("Апельсин", 220, "Оранжевый")

print("Информация о яблоке:")
apple.show_info()

print()

print("Информация об апельсине:")
orange.show_info()
