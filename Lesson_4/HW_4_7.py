# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
        yield total

while True:
    try:
        num = int(input('Enter integer number: '))
        break
    except ValueError:
        print('It s not a number!')

for i, j in enumerate(factorial(num)):
    print(f'Factorial of {i + 1} is {j}')