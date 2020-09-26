# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

final_text = []
while True:
    text = input('Insert a text (for quit press Enter twice): ')
    if text == '':
        print(f'Those elements {final_text} are written to file text.txt')
        break
    else:
        phrase = text + ', '
        final_text.append(phrase)
    with open('text_5_1.txt', 'w') as file:
        file.writelines(final_text)