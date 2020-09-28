# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т.

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_of_squer_meter, thickness):
        return self._width * self._length * mass_of_squer_meter * thickness

total_mass = Road(20, 5000)
print(f'To cover this area needs : {total_mass.mass(25, 5) / 1000} tons.')