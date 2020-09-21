# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

def modificator(mod_list: list) -> list:
    new_list = [i for i in mod_list if mod_list.count(i) == 1]
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