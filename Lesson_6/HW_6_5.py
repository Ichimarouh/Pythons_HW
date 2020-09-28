# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return {self.title}

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took {self.title}'

pen = Pen('a pen')
pencil = Pencil('a pencil')
handle = Handle('a handle')
print(f'{pen.draw()} to write a letter.')
print(f'{pencil.draw()} to draw a portrait.')
print(f'{handle.draw()} to mark an article in a newspaper.')