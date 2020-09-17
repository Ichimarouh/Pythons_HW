# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def expon(x, y):
    return 1 / x ** abs(y)

x = float(input('Insert a number: '))
y = -abs(int(input('Insert a negative number: ')))

print(f'{x} to the power of {y} is {expon(x, y)}')



# Вариант возведения в степень через цикл.

# def power(*args):
#     x = float(input('Insert a number: '))
#     y = -abs(int(input('Insert a number: ')))
#     ans = 1
#     for i in range(abs(y)):
#         ans = ans / x
#     return ans
#
# print(power())