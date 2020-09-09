#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

set_sec = int(input('Insert time in seconds: '))

hours = set_sec // 3600
minutes = (set_sec - hours * 3600) // 60
seconds = set_sec - hours * 3600 - minutes * 60

print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))