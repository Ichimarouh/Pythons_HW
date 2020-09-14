# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например,
# название, а значение — список значений-характеристик, например список названий товаров.

prod_list = []
inserting = None
while True:
    inserting = input(f'\n To continue press "-"; to get analitics type "*", press any other button for quit: ')
    if inserting == '-':
        amount_prod = int(input("\n Insert amount of kinds of products: "))
        j = 1
        while j <= amount_prod:
            prod_dict = dict({'Name of product': input(f'Insert a name of product {j}: '), 'Price': input(f'Insert a price {j}: '),'Amount': input(f'Insert an amount {j}: '), 'Measure': input(f'Insert a measure {j}: ')})
            prod_list.append((j, prod_dict))
            j += 1
        print(prod_list)
        inserting = input(f'\n To continue press "Enter"; to get analitics type "*"; for quit type "-": ')
    if inserting == '*':
        for m in prod_list:
            for key , value in prod_dict.items():
                print(key, value)
    else:
        break
