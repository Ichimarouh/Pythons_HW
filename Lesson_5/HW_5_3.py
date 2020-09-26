# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

try:
    with open('text_5_3.txt', 'r', encoding='UTF-8') as salary_report:
        total_sum = 0
        count = 0
        for position in salary_report:
            try:
                total_sum += float(position.split()[1])
                count += 1
                if float(position.split()[1]) < 20000:
                    print(f'\nSalary of {position.split()[0]} is less than 20 thousands')
            except ValueError:
                print('Sequence is out of order')
                quit()
        try:
            print('-' * 50)
            print(f'Average salary is {total_sum / count}')
        except ZeroDivisionError:
            print('Division by zero!')
            quit()
except FileNotFoundError or FileExistsError:
    print('File is not found')