#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.

num = int(input('Insert a number: '))

print(f'The sum is {num + int(str(num) * 2) + int(str(num) * 3)}.')