# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Insert a number: '))

max_num = num % 10
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
    num = num // 10

print(max_num)