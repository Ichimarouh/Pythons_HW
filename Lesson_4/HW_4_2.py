# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

def modificator(mod_list: list) -> list:
    new_list = [j for i, j in enumerate(mod_list) if mod_list[i] > mod_list[i - 1] and i != 0]
    return new_list

while True:
    input_list = (input('Enter numbers separated by space (press Enter to stop): ')).split(' ')
    try:
        for index, num in enumerate(input_list):
            input_list[index] = int(num)
        break
    except ValueError:
        print('Inserted element is not a number!')
        continue

print(modificator(input_list))