# Делаем заказ в ресторане - часть 2
#
# Проблема предыдущей версии функции make_order заключается в том, что она перезатирала ранее заказанные блюда. И она также не давала в рамках одного вызова заказать несколько блюд из одной категории.
#
# Ваша задача переписать функцию  make_order так, чтобы она сохраняла блюда из одной категории в виде списка, а в случае нового заказа с блюдами из той же категории, эти блюда добавлялись бы в тот же список..
#
# Давайте разберем примеры, имеется такая структура данных
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
#
# Далее Андрей делает два заказа make_order
#
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша')
#
# Оба заказанных блюда из категории суп, значит в итоге нужно сложить их в один список и получить следующее
#
# {
#  1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': ['Borsh', 'Лапша']}},
#  2: None,
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}
# }
#
# Также новая реализация функции make_order   должна позволять передать несколько блюд через запятую в рамках одной категории
#
# make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
# make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')

tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

order_all = ['salad', 'soup', 'main_dish', 'drink', 'desert']


def reserve_table(num, name, is_vip=False):
    """бронируем стол"""
    if tables[num] is None:
        tables[num] = {'name': name, 'is_vip': is_vip, 'order': {}}


def make_order(num, **kwargs):
    """делаем заказ из меню order_all"""
    for k, v in kwargs.items():
        if k in order_all and k not in tables[num]['order']:
            tables[num]['order'][k] = v.split(",") # добавляем в виде списка, разделяя по запятой
        elif k in tables[num]['order']:
            tables[num]['order'][k] += v.split(",")


def delete_order(*, number_table, delete_all=False, **del_kwargs):
    """обнуляем заказ, если  delete_all=False, то обнуляем там где TRUE, если delete_all=True, то очищаем весь заказ"""
    if delete_all is False: #очищаем частично по True
        for n, t in del_kwargs.items():
            if del_kwargs[n] is True:
                tables[number_table]['order'].pop(n, None)
    else:
        tables[number_table]['order'].clear() #очищаем весь заказ
