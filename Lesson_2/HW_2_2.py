#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

default_list = []
el = None
while True:
    el = input('Insert an element (for quit type "stop"): ')
    if el != "stop":
        default_list.append(el)
    else:
        break
print(f'\n Inserted list- {default_list}')

n = 0
for i in range(int(len(default_list)/2)):
    default_list[n], default_list[n+1] = default_list[n+1], default_list[n]
    n += 2
print(f'\n Modified list- {default_list}')