# Область видимости
# В программировании область видимости (по-английски этот термин называется «Scope») имени определяет область
# программы, в которой можно однозначно получить доступ к этому имени, например, к имени переменной или функции.
# Имя будет видно и доступно только в его области видимости. Некоторые языки программирования, в том числе и python,
# используют разные области видимости для избежания конфликтов имен и непредсказуемого поведения. Чаще всего различают
# две общие области:
#
# Глобальная область видимости: имена, которые вы определяете в этой области, доступны всему вашему коду.
# Локальная область видимости: имена, которые вы определяете в этой области, доступны или видимы только для кода внутри
# этой области.

# Имена в ваших программах будут иметь область видимости блока кода, в котором вы их определяете.

# y = 'global varible'  # определена глобальная переменная
#
# def my_func():
#     x = "local varible"  # определена локальная переменная
#     print(y)  # есть доступ к глобальной переменной
#     print(x)  # есть доступ к локальной переменной в локальной области
#
# print(y)  # есть доступ к глоб. переменной в глобальной области
# print(x)  # нет доступа к локальной переменной в глобальной области

# Пространство имен — это совокупность определенных в настоящий момент символических имен и информации об объектах, на
# которые они ссылаются. Другими словами, это набор всех созданных имен и объектов, на которые эти имена ссылаются.

# Namespaces are one honking great idea -- let's do more of those!

# Пространство имен - это система, которая гарантирует, что все имена в программе уникальны и могут использоваться без
# каких-либо конфликтов. Python реализует пространства имен как словари. Существует сопоставление «имя-объект» с именами
# в виде ключей и объектов в качестве значений. Каждая пара ключ-значение соотносит имя с соответствующим ему объектом.
# Несколько пространств имен могут использовать одно и то же имя и сопоставлять их с другим объектом

# Всего в python существует 4 вида пространства имен:
# builtins (встроенное пространство имен).
# global (глобальное пространство имен)
# enclosing (объемлющее пространство имен)
# local (локальное пространство имен)

# Встроенное пространство имен (built-in namespace) — представляет собой набор имен всех встроенных функций и объектов в
# Python. Всё, чем вы привыкли пользоваться в Python, например, такие функции, как len, min и max, а также имена типов
# данных, таких как int, float и str - все эти имена относятся ко встроенному пространству имён и, следовательно, образуют
# встроенную область видимости.
#
# Как получается, что все эти имена доступны нам по умолчанию? Все дело в том, что все эти объекты реализованы в виде
# стандартного библиотечного модуля, называемого builtins.  Они автоматически загружаются во встроенную область видимости
# при запуске интерпретатора Python.
#
# При помощи функции dir можно взглянуть на весь состав встроенного пространства имен
# print(dir())

# Все имена встроенных объектов всегда загружаются в вашу глобальную область действия Python под специальным именем
# __builtins__,
# print(dir(__builtins__))

# Функция dir() возвращает список имен в текущей области видимости. Если же в функцию dir() передать
# объект, тогда она вернет список его атрибутов и методов. Объектом в python является все, поэтому вы можете передать,
# например, объект встроенной функции суммы
# print(dir(sum))

# Глобальное пространство имен (global namespace) содержит имена, определенные на уровне основной программы, и создаётся
# сразу при запуске тела этой программы. Сохраняется же оно до момента завершения работы интерпретатора. Все имена,
# определенные в глобальном пространстве имен, соответственно находятся в глобальной области видимости. Когда же
# создается глобальная область видимости?

# Сразу после запуска вашей программы вы окажетесь в глобальной области видимости. Интерпретатор Python внутри себя
# превратит файл вашей программы в модуль с именем __main__, который обеспечивает выполнение основной программы.
# Убедиться в том, что ваш файл будет загружен под названием __main__, вы можете с помощью следующей строчки
# print(__name__)
#Посмотреть на имена глобальной области видимости вы можете при помощи функции dir без аргументов
# print(dir())

# Локальное пространство имен (local namespace) содержит имена, которые доступны только внутри определенной функции.
#
# Локальная область создается при вызове функций, причем каждый раз, когда вы вызываете функцию, будет создаваться новая
# локальная область видимости. Все параметры и имена, которые вы создаете внутри функции, образуют локальную область
# этой функции в пределах одного конкретного вызова. Когда функция завершает работу, локальная область видимости
# уничтожается, а имена забываются. Вот как это работает:

# def add(a, b):
#     summa = a + b
#     print(f'Результат сложения {a} и {b} = {summa}')
#
#
# add(5, 7)
# add(8, 13)
# print(summa) # raises NameError

# def add(a, b):
#     summa = a + b
#     print(dir()) # ['a', 'b', 'summa']
#     print(f'Результат сложения {a} и {b} = {summa}')
#
#
# add(5, 7)
# add(8, 13)

# def add(a, b):
#     summa = a + b
#     print(locals())
#     print(f'Результат сложения {a} и {b} = {summa}')
#
#
# add(5, 7)
# add(8, 13)

# Объемлющая или нелокальная область видимости возникает, когда вы вкладываете определение функции внутрь другой функции.
# def main_func(): # объемлющая
#     main_variable = 1
#
#     def inner_func(): #вложенная
#         print('Печатаем из inner_func', main_variable)
#
#     inner_func()
#     print('Печатаем из main_func', main_variable)
#
# main_func()
# Все имена, которые вы создаете в объемлющей области видимости, видны внутренней функции, за исключением тех, которые
# создаются после вызова внутренней функции.

# Чтобы убедиться, что переменные из объемлющей функции входят в область видимости вложенной функции, мы можем вызвать
# функцию locals()
#
# def outer_function():
#     x = 15
#     y = 10
#
#     def inner_function():
#         w = 40
#         print(x + y + w)
#         print('Доступные имена в inner_function', locals())
#
#     inner_function()
#     print('Доступные имена в outer_function', locals())
#
#
# outer_function()

# Свободные (нелокальные) переменные, оператор nonlocal

# Оператор nonlocal заявляет, что будет изменяться имя из объемлющей области видимости. Главное, чтобы имена,
# перечисленные в инструкции nonlocal,  ссылались на существовавшие переменные в охватывающей области. Объявим,
# что мы хотим изменять нелокальные переменные в нашей функции inner_function

# def outer_function():
#     x = 15
#     y = 10
#
#     def inner_function():
#         w = 40
#         nonlocal x, y
#         x = 33
#         y = 45
#         print(x + y + w)
#         print('Доступные имена в inner_function', locals())
#
#     inner_function()
#     print('Доступные имена в outer_function', locals())
#
#
# outer_function()

# Правило LEGB
# это аббревиатура, обозначающая порядок, в котором Python ищет имена переменных, когда вы используете их в своем коде.

# Таким образом, когда вы используете вложенные функции, поиск имени происходит следующим образом:
#
#    ✔️ Python просматривает локальную область самой внутренней функции. Если имя не находится, переходит к след. пункту;
#
#    ✔️ Python просматривает все области видимости внешних функций. Если имя не находится в них, переходит к след. пункту;
#
#     ✔️ Python просматривает глобальную область видимости. Если имя отсутствует, переходит к след. пункту;
#
#     ✔️ Python просматривает встроенную область видимости. Если имя отсутствует, переходит к след. пункту;
#
#     ✔️ Вы получите сообщение об ошибке NameError.

# L (local) — локальная область видимости
# E (enclosing) — локальная область объемлющих функций
# G (global) — глобальная область видимости
# B (built-in) — встроенная

# Задача Обменный пункт
# Одной из базовых банковских услуг является обмен валют.
#
# Напишите функцию convert, которая умеет конвертировать доллар в другую валюту и наоборот. Для конвертации используются текущие курсы валют, которые хранятся в глобальном словаре exchange_rates.
#
# Результат округлите до двух знаков после запятой при помощи функции round

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}

def convert(valuta: str,exchange: str, num: float) -> float:
    if valuta == "USD":
        fin_change = exchange_rates[valuta] * num * exchange_rates[exchange]
        fin_change_round = round(fin_change, 2)
        return fin_change_round
    if valuta != "USD":
        fin_change = num / exchange_rates[valuta]
        fin_change_round = round(fin_change, 2)
        return fin_change_round

currency = convert("EUR", "USD", 100)
print(currency)