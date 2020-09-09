# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

prod = int(input('Insert the proceeds: '))
costs = int(input('Insert the costs: '))

if prod - costs > 0:
    print(f'You have profit: {prod - costs}')
    pers = int(input('Insert the number of stuff: '))
    print (f'You have profit per person: {(prod - costs) / pers}')
else:
    print('You have loss. Required financial advice.')