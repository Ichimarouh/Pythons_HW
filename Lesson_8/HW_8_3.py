# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.

class Num_scanner:
    def __init__(self):
        self.numbers = []

    def check_numbers(self):
        while True:
            user_number = input('Insert a number or "E" to exit: ')
            self.numbers.append(int(user_number)) if user_number.isdigit() else print('Please insert a number!')
            print(f'Your list is {self.numbers}')
            if user_number == 'E':
                break
        return 'End'

n = Num_scanner()
print(n.check_numbers())