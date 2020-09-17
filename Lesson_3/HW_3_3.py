# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def sum_of_two(a, b, c):
    if a >= b and b >= c:
        return a + b
    elif b > a and a < c:
        return b + c
    else:
        return a + c

a = float(input('Insert first number: '))
b = float(input('Insert second number: '))
c = float(input('Insert third number: '))

print(f'Sum of two largest numbers is {sum_of_two(a, b, c)}.')