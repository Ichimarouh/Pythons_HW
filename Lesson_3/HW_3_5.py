# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum():
    total = 0
    finish = False
    while finish == False:
        check = input('Enter a number (press F to quit): ').split()
        result = 0
        for i in range(len(check)):
            if check[i] == 'f' or check[i] == 'F':
                finish = True
                break
            else:
                result = result + int(check[i])
        total = total + result
        print(f'Current total is {total}')
    print(f'Your final total is {total}')

sum()