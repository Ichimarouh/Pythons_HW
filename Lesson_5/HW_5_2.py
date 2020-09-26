# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    print('-' * 50)
    original_text = open('text_5_2.txt', 'r')
    cont = original_text.read()
    print(f'Original text: \n {cont}')
    print('-' * 50)

    original_text = open('text_5_2.txt', 'r')
    cont = original_text.readlines()
    print(f'Number of strings - {len(cont)}')
    print('-' * 50)

    original_text = open('text_5_2.txt', 'r')
    cont = original_text.readlines()
    for i in range(len(cont)):
        print(f'Amount of words in {i + 1} string is {cont[i].count(" ") + 1}')
        print('-' * 50)

    original_text.close()
except FileNotFoundError or FileExistsError:
    print('File is not found')