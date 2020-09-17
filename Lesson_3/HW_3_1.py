# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(*args):
    try:
        a = float(input('Insert first number: '))
        b = float(input('Insert second number: '))
        c = a / b
    except ZeroDivisionError:
        return "Infinit (you can not divide on zero!)"
    return c

print(f'Result of division is {div_func ()}')