# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Store:

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        self.full_store = []
        self.final_store = []
        self.element = {'Model': self.name, 'Amount': self.amount, 'Price': self.price}

    def __str__(self):
        return f'{self.name} amount {self.amount} price {self.price}'

    def reception(self):
        try:
            model = input(f'Insert a name of model: ')
            amount = int(input(f'Insert amount: '))
            price = int(input(f'Enter a price: '))
            elem_of_store = {'Model': model, 'Price': price, 'Amount': amount}
            self.element.update(elem_of_store)
            self.final_store.append(self.element)
            print(f'Current list:\n {self.final_store}')
        except:
            return f'Wrong input-output'

        print(f'Type Stop to stop, press Enter to continue')
        exit = input('>>> ')
        if exit == 'Stop' or exit == 'stop':
            self.full_store.append(self.final_store)
            print(f'All titles:\n {self.full_store}')
            return f'End'
        else:
            return Store.reception(self)

class Office:
    def __init__(self, name, amount, price, serial_number):
        self.name = name
        self.amount = amount
        self.price = price
        self.serial_number = serial_number

class Printer(Office):
    def printing(self):
        return f'{self.serial_number}'

class Scanner(Office):
    def scanning(self):
        return f'{self.serial_number}'

class Copier(Office):
    def copying(self):
        return f'{self.serial_number}'