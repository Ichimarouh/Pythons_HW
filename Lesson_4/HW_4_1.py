# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary(prod: float, rate_per_h: float, award: float) -> float:
    return float(prod) * float(rate_per_h) + float(award)

_, prod, rate_per_h, award = argv

print(f'Employee salary is {salary(argv[1], argv[2], argv[3])}')