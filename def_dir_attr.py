# Атрибуты и методы функции
# Функции — это объекты первого класса. К тому же у них тоже есть свои атрибуты.
# Атрибут — это переменная, связанная с объектом. Метод, в свою очередь, это функция, связанная с объектами.
# С некоторыми атрибутами мы с вами уже познакомились. Вот они:
#
#     ✔️  __doc__ хранит информацию о док-строке функции
#
#     ✔️ __annotations__ хранит информацию об аннотации функции
#
# Давайте взглянем на весь перечень атрибутов и методов для функции при помощи функции dir

def get_product(a: int, b: int) -> int:
    return a + b

print(dir(get_product))

# Создание атрибутов для функции
# Перечисленные атрибуты __doc__ и __annotations__ были созданы и привязаны к функции самим python автоматически
# без нашего участия. Но у нас есть возможность создавать свои собственные атрибуты к объектам-функциям.
# Для этого нужно выбрать имя для атрибута, избегая названия, начинающегося и заканчивающегося на два нижних
# подчеркивания. Затем прописываете сперва вашу функцию, потом через точку указываете название атрибута и
# присваиваете ему значение.

# имя_функции.имя_атрибута = значение

ef get_product(a: int, b: int) -> int:
    return a + b


get_product.category = 'math'
get_product.sub_category = 'arithmetic operation'

print(get_product.category)
print(get_product.sub_category)

# Созданные атрибуты будут отображаться при помощи функции dir
def get_product(a: int, b: int) -> int:
    return a + b

get_product.category = 'math'
get_product.sub_category = 'arithmetic operation'

print(dir(get_product))

# setattr(obj, name_attr, value)

Она принимает объект, имя атрибута строкой или переменной, и значение для атрибута. Функция setattr установит
переданному объекту по атрибуту name_attr новое значение value.
Если атрибута у объекта вообще не было, функция setattr его создаст. Тогда наш пример кода будет выглядеть так

def get_product(a: int, b: int) -> int:
    return a + b

name = 'category'
setattr(get_product, name, 'math') # создается атрибут category со значением math
print(dir(get_product))
print(get_product.category)

# Обращение к атрибутам

# Доступ к атрибутам объекта можно получить двумя способами. Первый - обратиться к объекту и через точку указать
# название атрибута. Вот пример такого обращения к атрибуту

print(get_product.category)  # получает доступ к атрибуту category
print(get_product.sub_category)  # получает доступ к атрибуту sub_category
print(get_product.__doc__)  # получает доступ к атрибуту __doc__
print(get_product.__annotations__)  # получает доступ к атрибуту __annotations__

# Второй способ получить доступ к значению атрибута - воспользоваться встроенной функцией getattr. У нее следующий формат обращения
#
# getattr(obj, name_attr)
# Название имени атрибута нужно передавать именно строковым значением. Вот пример обращения к атрибутам при помощи getattr

def get_product(a: int, b: int) -> int:
    return a + b


setattr(get_product, 'category', 'math')  # создается атрибут category
get_product.sub_category = 'arithmetic operation'  # создается атрибут sub_category

print(getattr(get_product, 'category'))  # получает доступ к атрибуту category
print(getattr(get_product, 'sub_category'))  # получает доступ к атрибуту sub_category
print(getattr(get_product, '__doc__'))  # получает доступ к атрибуту __doc__
print(getattr(get_product, '__annotations__')) # получает доступ к атрибуту __annotations__

# Если попытаться обратиться к несуществующему атрибуту,
#
# print(getattr(get_product, 'my_attribure'))
# вновь возникнет исключение
#
# AttributeError: 'function' object has no attribute 'my_attribure'
#
# Но его можно обойти при помощи третьего необязательно параметра default_value функции getattr
#
# getattr(obj, name_attr, default_value)
# Это значение по умолчанию, которое будет возвращать функция getattr в случае, если не будет найден атрибут.
#
# print(getattr(get_product, 'my_attribure', 1000)) # Вернет 1000

# Функция hasattr
# Встроенная функция hasattr позволяет проверить наличие атрибута у объекта. Формат вызова следующий
#
# hasattr(obj, name_attribute) -> bool
# Вы передаете объект и строковое название атрибута или метода в параметр name_attribute.
# Если у объекта среди методов и атрибутов находится имя name_attribute, функция вернет True, в противном случае - False.
#
# def print_goods(lst):
#     pass
#
#
# print_goods.is_working = False
#
# print(hasattr(print_goods, 'is_working'))  # True
# print(hasattr(print_goods, 'status'))  # False
# print(hasattr(print_goods, '__doc__'))  # True
#
# print(hasattr(list, 'append'))  # True
# print(hasattr(list, 'lower'))  # False

# Атрибут __name__
# Атрибут __name__ содержит имя функции:
#
# def get_product(a: int, b: int) -> int:
#     return a + b
#
# print(get_product.__name__)

# Атрибуты __defaults__ и __kwdefaults__
# Атрибут __defaults__ представляет собой кортеж, содержащий все значения позиционных параметров по умолчанию.
# Для нашей функции get_product атрибут __defaults__ будет хранить значение None, так как у нас отсутствуют
# значения по умолчанию
#
# def get_product(a: int, b: int) -> int:
#     return a + b
#
#
# print(get_product.__defaults__)
# Если добавим значения по умолчанию, то увидим их в отображении атрибута __defaults__
#
# def get_product(a: int = 6, b: int = 3) -> int:
#     return a + b
#
#
# print(get_product.__defaults__)
# Атрибут __kwdefaults__ отображает значения по умолчанию для именованных параметров.
# Давайте для примера разберем функцию my_func, в которой есть как позиционные, так и ключевые параметры
# со значениями по умолчанию

# В атрибут __defaults__ попали только параметры b и c,  так как они являются позиционными и у них есть значения по
# умолчанию. В атрибут__kwdefaults__ попал только параметр kw2, потому что он является именованным и имеет значение по
# умолчанию. Параметр kw1 тоже является именованным, но у него нету значения по умолчанию

def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
    pass
И сразу взглянем на значения, хранящиеся в атрибутах __name__, __defaults__ и __kwdefaults__.

def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
    pass

print(my_func.__name__) # my_func
print(my_func.__defaults__) # (2, 3)
print(my_func.__kwdefaults__)# {'kw2': 4}

# Атрибут __code__
# Следующим атрибутом, про который мы поговорим, является __code__.
# Интересен он тем,  что хранит в себе информацию об объекте с одноименным названием  code.

def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
    pass

print(my_func.__code__)

#  этого объекта code можно также взглянуть на состав атрибутов при помощи функции dir
# #
# # def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
# #     pass
# #
# # print(dir(my_func.__code__))
#
# Вот на какие имена обратите внимание:
#
#     ✔️  co_varnames  хранит информацию об именах параметров функции и о локальных переменных в виде кортежа
#
#     ✔️  co_argcount  возвращает количество аргументов (за вычетом именованных аргументов,  *args и **kwargs)
#
# Обращаться к перечисленным атрибутам нужно через точку от атрибута
#
# def my_func(a, b=2, c=3, *, kw1, kw2=4, **kwargs):
#     my_local = None
#
# print(my_func.__code__.co_varnames) # ('a', 'b', 'c', 'kw1', 'kw2', 'kwargs', 'my_local')
# print(my_func.__code__.co_argcount) # Печатает 3

# Задачи
# Напишите функцию get_info_about_object, которая принимает объект и выводит информацию обо всех его
# атрибутах и методах в следующем формате:
#
# сперва выводится список всех атрибутов и методов
# на следующей строке фраза «Всего у объекта {count} атрибутов и методов»


def print_goods(lst):
    pass

print_goods.info = 'Функция для вывода информации о товарах'
print_goods.is_working = False
print_goods.status = 'Not ready'

def get_info_about_object(object):
    print(dir(object))
    print(f"Всего у объекта {len(dir(object))} атрибутов и методов")

get_info_about_object(print_goods)

# Напишите функцию check_exist_attrs, которая принимает объект obj и список строк, в котором хранятся
# имена атрибутов.
#
# Функция check_exist_attrs должна вернуть словарь, в котором ключами будут являться имена атрибутов из
# переданного списка. Напротив каждого ключа должно быть булево значение: True, если атрибут присутствует
# в объекте obj , в обратном случае - False.
#
# Ключи в итоговом словаре необходимо создавать в порядке следования имен атрибутов во входном списке
def print_goods(lst):
    pass

print_goods.is_working = False
print_goods.status = 'Not ready'

def check_exist_attrs(obj, attrs):
    return {attr: hasattr(obj, attr) for attr in attrs}

print(check_exist_attrs(print_goods, ['is_working', 'status', 'time', 'speed']))

# Напишите функцию create_attrs, которая принимает объект obj и список кортежей. Каждый кортеж состоит из пары
# значений: имя атрибута в виде строки и его будущее значение.
#
# Задача функции create_attrs — создать на основании внутренних кортежей списка новые атрибуты к переданному
# объекту.
#
# Для проверки работоспособности программы скопируйте реализацию функции check_exist_attrs из предыдущего
# задания
def print_goods(lst):
    pass

def create_attrs(obj, attrs_values):
    for attr, value in attrs_values:
        setattr(obj, attr, value)

def check_exist_attrs(obj, attrs):
    return {attr: hasattr(obj, attr) for attr in attrs}

create_attrs(print_goods, [('house', 1), ('level', 3), ('cost', 1000000)])
print(print_goods.house)
print(print_goods.level)
print(print_goods.cost)

