# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summation():
    try:
        with open('text_5_5.txt', 'w+') as file:
            input_text = input('Enter a number separated by a space: ')
            file.writelines(input_text)
            num = input_text.split()
            print(sum(map(int, num)))
    except IOError:
        print('File fail')
    except ValueError:
        print('Dialed wrong number. Input-output error.')
summation()