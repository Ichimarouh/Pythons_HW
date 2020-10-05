# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_num:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(f'Sum of z_1 и z_2 is')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Composition of z_1 и z_2 is')
        return f'z = {self.x * other.x - self.y * other.y} + {self.x * other.y + other.x * self.y} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'

z_1 = Complex_num(2, 3)
z_2 = Complex_num(5, -7)
print(z_1 + z_2)
print(z_1 * z_2)