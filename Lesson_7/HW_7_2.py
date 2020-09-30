# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def consumption_for_coat(self):
        return self.width / 6.5 + 0.5

    def consumption_for_jacket(self):
        return self.height * 2 + 0.3

    @property
    def total_consumption(self):
        return str(f'Total consumption of cloth is {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)} m^2')

class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat_area = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Consumption on coat is nearly {self.coat_area} m^2'

class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.jacket_area = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Consumption on jacket is nearly {self.jacket_area} m^2'

coat = Coat(2, 2)
jacket = Jacket(1.8, 1.8)

print(f'\n')
print(coat)
print(jacket)
print(round(jacket.consumption_for_coat(), 2))
print(round(coat.consumption_for_coat(), 2))
print(coat.total_consumption)