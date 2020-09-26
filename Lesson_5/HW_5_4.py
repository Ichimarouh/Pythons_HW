# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

translate_dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре', 'Five': 'пять', 'Six': 'шесть', 'Seven': 'семь', 'Eight': 'восемь', 'Nine': 'девять', 'Zero': 'нуль'}
new = ''
try:
    with open('text_5_4_in.txt', 'r', encoding = 'UTF-8') as dictionary:
        for position in dictionary:
            new += translate_dict.get(position.split()[0]) + ' — ' + position.split()[2] + '\n'
    with open('text_5_4_out.txt', 'w', encoding = 'UTF-8') as translated_text:
        translated_text.write(new)
except FileNotFoundError or FileExistsError:
    print('File is not found')