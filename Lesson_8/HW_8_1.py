# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def retrieving(cls, d_m_y):
        inserted_date = []
        for i in d_m_y.split():
            if i != '-': inserted_date.append(i)
        return int(inserted_date[0]), int(inserted_date[1]), int(inserted_date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2077 >= year:
                    return f'Date is all right'
                else:
                    return f'Wake the #### up, Samurai. We have a city to burn.'
            else:
                return f'Enter the ordinal number of the month (1-12)!'
        else:
            return f'Enter the ordinal number of the day (1-31)!'

    def __str__(self):
        return f'Current date: {Date.retrieve(self.d_m_y)}'

print(Date.retrieving('15 - 03 - 2008'))
print(Date.validation(8, 15, 2017))
print(Date.retrieving('18 - 11 - 2025'))
print(Date.validation(25, 7, 2078))
print(Date.validation(20, 5, 2012))