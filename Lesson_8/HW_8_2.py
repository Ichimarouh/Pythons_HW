# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division_error:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def division_by_zero(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return (f'Division by zero is impossible!')

print(Division_error.division_by_zero(15, 0.002))
print(Division_error.division_by_zero(7, 0))