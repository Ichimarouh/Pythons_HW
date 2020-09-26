# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

try:
    with open('text_5_7_in.txt', 'r', encoding='UTF-8') as text:
        profit_dict = {}
        sum_of_profit = 0
        count = 0
        try:
            for pos in text:
                if float(pos.split()[2]) - float(pos.split()[3]) >= 0:
                    sum_of_profit += float(pos.split()[2]) - float(pos.split()[3])
                    count += 1
                profit_dict[pos.split()[0]] = round(float(pos.split()[2]) - float(pos.split()[3]), 3)
        except ValueError:
            print('Sequence is out of order')
            quit()
        try:
            average_profit = {'Average_profit': round(sum_of_profit / count, 2)}
        except ZeroDivisionError:
            print('Division by zero')
            quit()
    with open('text_5_7_out.txt', 'w', encoding='UTF-8') as file_json:
        json.dump([profit_dict, average_profit], file_json)
except FileNotFoundError or FileExistsError:
    print('File is not found')
