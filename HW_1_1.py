#1. Поработайте с переменными, создайте несколько, выведите на экран,
#запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

name = input('Insert your name: ')
location = input('Where are you from: ')
any_num = int(input('Insert any number: '))

print('%s from %s choosed %d.' % (name, location, any_num))