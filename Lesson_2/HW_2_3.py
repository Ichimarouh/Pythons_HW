# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Enter an ordinal of month: '))
seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
seasons_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
if month in[1, 2, 12]:
    print(f'Is {seasons_list[0]}.')
    print(f'Is {seasons_dict.get(1)}.')
elif month in[3, 4, 5]:
    print(f'Is {seasons_list[1]}.')
    print(f'Is {seasons_dict.get(2)}.')
elif month in[6, 7, 8]:
    print(f'Is {seasons_list[2]}.')
    print(f'Is {seasons_dict.get(3)}.')
elif month in[9, 10, 11]:
    print(f'Is {seasons_list[3]}.')
    print(f'Is {seasons_dict.get(4)}.')
else:
    print('There is no month with that ordinal.')