# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

def total(lessons):
    amount = lessons.split()
    i = 0
    while i < len(amount):
        if not amount[i] in {'-', '—'}:
            amount[i] = int(amount[i][:amount[i].index('('):])
            i += 1
        else:
            amount.remove(amount[i])
    return sum(amount)

total_of_lessons = {}
try:
    with open('text_5_6.txt', 'r', encoding = 'UTF-8') as text:
        try:
            for position in text:
                total_of_lessons[position[:position.index(' ')-1:]] = total(position[position.index(' ')+1::])
        except ValueError:
            print('Sequence is out of order')
            quit()
    print(total_of_lessons)
except FileNotFoundError or FileExistsError:
    print('File is not found')