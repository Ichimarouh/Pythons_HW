# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def resume_func(name, surname, birth_date, city, e_mail, phone_num):
    return '-'.join([name, surname, birth_date, city, e_mail, phone_num])

print(resume_func(name='Albert', surname='Einstein', birth_date='14.03.1879', city='Ulm', e_mail='al_ein@universe.space',
              phone_num='07305-123-456'))