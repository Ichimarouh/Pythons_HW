# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

default_list = [2, 5, 7, 4, 3]
print(f"Rating: {default_list}")
num = int(input('Insert a number (press "10000" to quit): '))
while num != 10000:
    for i in range(len(default_list)):
        if default_list[i] == num:
            default_list.insert(i + 1, num)
            break
        elif default_list[0] < num:
            default_list.insert(0, num)
        elif default_list[-1] > num:
            default_list.append(num)
        elif default_list[i] > num and default_list[i + 1] < num:
            default_list.insert(i + 1, num)
    print(f'Modified list: {default_list}')
    num = int(input('Insert a number: '))