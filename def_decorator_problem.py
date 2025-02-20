#Проблемы декорирования функции
# Каждая функция хранит внутри себя некую служебную информацию, например
#
# в  атрибуте __name__ содержится имя функции
# в  атрибуте __doc__ содержится док строка функции, если она имеется
# в  атрибуте __annotations__  содержится информация о типах параметров и о возвращаемом значении, если были использованы
# аннотации в заголовке функции

def say_hello(name: str, surname: str) -> None:
    """Функция приветствует человека"""
    print('Hello', name, surname)


print(f'{say_hello.__name__        =  }')
print(f'{say_hello.__doc__         =  }')
print(f'{say_hello.__annotations__ =  }')

# say_hello.__name__        =  'say_hello'
# say_hello.__doc__         =  'Функция приветствует человека'
# say_hello.__annotations__ =  {'name': <class 'str'>, 'surname': <class 'str'>, 'return': None}

# Проблема декорирования заключается в том, что как только вы продекорируете оригинальную функцию, она потеряет свою
# первоначальную служебную информацию. Если использовать синтаксический сахар и декорировать через символ @, то вы
# потеряете информацию об оригинальной функции сразу же.

# Все дело в том, что использование синтаксиса @ декорирует функцию сразу же во время определения.
#
# Идея декоратора заключается в расширении функционала оригинальной функции. На практике достигается это путем подмены
# одной функции на другую, но подменить нужно именно так, чтобы служебная  информация об исходной функции не менялась.
#
# Почему это важно? Взять хотя бы даже атрибут __name__ . Потеря оригинального имени функции приведет к тому, что мы
# не будем знать какая функция вызывалась. Более того, если вы используете один и тот же декоратор, то вы получите уже две функции, которые будут ссылаться на одну внутреннюю функцию inner
def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    inner.__name__ = func.__name__ # 1 способ сохранения атрибутов оригинальной функции
    inner.__doc__ = func.__doc__
    inner.__annotations__ = func.__annotations__
    return inner


@table
def print_sqr_number(x: int) -> None:
    """
    Печатает квадрат числа x
    :param x
    :return: None
    """
    print(x ** 2)

print(f'{print_sqr_number.__name__        =  }')
print(f'{print_sqr_number.__doc__         =  }')
print(f'{print_sqr_number.__annotations__ =  }')

print_sqr_number(6)

# Второй способ заключается в использовании встроенной функции-декоратора wraps. Перед использованием ее необходимо
# импортировать из модуля functools в самом вверху программы при помощи следующей строки

from functools import wraps #2 способ
def table(func):

    @wraps(func) #2 способ сохранения атрибутов оригинальной функции
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner


@table
def print_sqr_number(x: int) -> None:
    """
    Печатает квадрат числа x
    :param x
    :return: None
    """
    print(x ** 2)

print(f'{print_sqr_number.__name__        =  }')
print(f'{print_sqr_number.__doc__         =  }')
print(f'{print_sqr_number.__annotations__ =  }')

print_sqr_number(6)


#ЗАДАЧИ

#Декоратор no_side_effects_decorator
# Напишите декоратор no_side_effects_decorator, который защищает от побочных действий функций
#
# Sample Input 1:


import copy
from functools import wraps


def no_side_effects_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        # Глубокое копирование только первого аргумента (списка)
        deep_copy = copy.deepcopy(args[0]) if args else None  # ([1, 2, 3], 4)-это кортеж, создаем deepкопию 0 элемента кортежа, т.е. списка в данном случае [1, 2, 3]. None возвращается, если args пустой, то есть нет позиционных аргументов.

        return func(deep_copy, *args[1:],**kwargs)  # deep_copy — это глубокая копия первого элемента в аргументах args, *args[1:]-это выражение использует распаковку аргументов. Оно означает, что из всего кортежа args (который содержит все позиционные аргументы, переданные в функцию) берутся все элементы начиная с индекса 1 и передаются в функцию, Это распаковка именованных аргументов (ключ-значение), переданных в функцию. kwargs — это словарь, который содержит все именованные аргументы, переданные в функцию. Например, если функция вызвана так: add_element(my_list, 4, element=10), то kwargs будет равен {'element': 10}

    return inner


@no_side_effects_decorator
def add_element(data, element):
    data.append(element)
    return data


my_list = [1, 2, 3]
print('Результат вызова =', add_element(my_list, 4))
print('Результат вызова =', add_element(my_list, 5))
print(my_list)
print(add_element.__name__)


@no_side_effects_decorator
def add_element(data, key, value=None):
    data[key] = value
    return data


my_dict = {1: 'Hello', 2: 'World'}
print('Результат вызова =', add_element(my_dict, 3))
print('Результат вызова =', add_element(my_dict, 4, 'four'))
print(my_dict)
print(add_element.__name__)

# В декораторе мы применяем deepcopy только к первому аргументу, который должен быть списком (или другим изменяемым
# объектом). Если первый аргумент существует, мы создаем его копию.
# Позиционные и именованные аргументы передаются корректно в func, с учетом того, что мы передаем скопированный список,
# а остальные аргументы остаются без изменений.
# Теперь вызовы add_element не будут изменять исходный список my_list, а вместо этого будет возвращаться новый список
# в каждом вызове.

# Декоратор limit_query
# Напишите декоратор limit_query, который ограничивает вызов оригинальной функции так, чтобы она могла
# вызываться не больше трех раз. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на
# экран фразу
#
#  «Лимит вызовов закончен, все 3 попытки израсходованы»
#
# Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None

def limit_query(func):
    count = 3
    def inner_limit(*args, **kwargs):
        nonlocal count
        if count > 0:
            count -= 1
            return func(*args, **kwargs)
        else:
            print(f"Лимит вызовов закончен, все 3 попытки израсходованы")
            return None  # Возвращаем None или можно выбросить исключение

    inner_limit.__name__ = func.__name__  # Устанавливаем __name__ только один раз
    return inner_limit

@limit_query
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)

# Декоратор add_args
# Напишите декоратор add_args, который добавляет к переданным аргументам еще два значения: строку «begin» в начало
# аргументов, строку «end» в конец. Также декоратор должен сохранить первоначальное имя декорируемой функции и ее
# строку документации

from functools import wraps


def add_args(func):
    @wraps(func)
    def inner_add(*args, **kwargs):
        a = "begin"
        c = "end"
        return func(a, *args, c, **kwargs)

    return inner_add

@add_args
def find_max_word(*args):
    """
    Возвращает слово максимальной длины
    """
    return max(args, key=len)

print(find_max_word('my'))
print(find_max_word('my', 'how'))
print(find_max_word('my', 'how', 'maximum'))
print(find_max_word.__name__)
print(find_max_word.__doc__.strip())

# Декоратор explicit_args
# Реализуйте декоратор explicit_args, который не позволяет запускать оригинальную функцию, если были переданы позиционные
# аргументы. Декоратор explicit_args должен выводить фразу
#
# Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
# и предотвращать запуск оригинальной функции

from functools import wraps


def explicit_args(func):
    @wraps(func)
    def inner_add(*args, **kwargs):
        # Если переданы позиционные аргументы, выводим сообщение и не выполняем функцию
        if args:
            print("Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений")
            return None
        # Если позиционных аргументов нет, вызываем оригинальную функцию
        return func(*args, **kwargs)

    return inner_add

@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, 20))

# Декоратор reverse
# Реализуйте декоратор reverse, который сделает так, чтобы декорированная функция принимала все свои позиционные
# аргументы в обратном порядке. Именованные аргументы должны игнорироваться декоратором reverse.
#
# Также нужно сохранить информацию о декорируемой функции.

from functools import wraps

def reverse(func):
    @wraps(func)  # Сохраняем имя и другие метаданные функции
    def inner_reverse(*args, **kwargs):
        # Переворачиваем только позиционные аргументы
        args = args[::-1]
        return func(*args)  # Распаковываем args при вызове функции
    return inner_reverse


@reverse
def get_max_index(*args):
    if not args:
        return None
    max_index = 0
    for i in range(len(args)):
        if args[i] > args[max_index]:
            max_index = i
    return max_index


print(get_max_index(1, 2, 3, 4, 5))
print(get_max_index(3, 4, 1, 5, 2))
print(get_max_index(5, 3, 4, 1, 2))
print(get_max_index.__name__)

# Декоратор monkey_patching
# Monkey patch -  это прием в программировании, который используется для динамического изменения поведения фрагмента
# кода во время выполнения.
#
# Ваша задача написать декоратор monkey_patching, который заменяет значения всех переданных аргументов при вызове
# оригинальной функции следующим образом:
#
#     ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»
#➕   значение каждого именованного аргумента заменяется на строку «patching»

from functools import wraps


def monkey_patching(func):
    @wraps(func)
    def inner_fun(*args, **kwargs):
        if args:
            list_args = list(args)
            for arg in range(len(list_args)):
                list_args[arg] = "Monkey"
            args = tuple(list_args)

        if kwargs:
            for k, v in kwargs.items():
                kwargs[k] = "patching"
        return func(*args, **kwargs)

    return inner_fun

@monkey_patching
def info_kwargs(**kwargs):
    """Выводит информацию о переданных kwargs"""
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

info_kwargs(first_name="John", last_name="Doe", age=33)
info_kwargs(c=43, b= 32, a=32)
print(info_kwargs.__name__)
print(info_kwargs.__doc__.strip())

# Декоратор counting_calls
# Реализуйте декоратор counting_calls, который будет подсчитывать количество вызовов оригинальной функции.
#
# После декорирования при помощи counting_calls у функции должен появиться атрибут call_count, который отслеживает
# текущее количество вызовов.

from functools import wraps

def counting_calls(func):
    # Устанавливаем атрибут call_count внутри самой функции, а не внутри декоратора
    @wraps(func)
    def inner(*args, **kwargs):
        # Увеличиваем счетчик вызовов
        inner.call_count += 1
        return func(*args, **kwargs)  # Возвращаем результат функции
    # Инициализируем счетчик вызовов
    inner.call_count = 0
    return inner

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(30, 5))
print(add(3, 5))
print(add(4, 5))
print('Количество вызовов =', add.call_count)
print(add(11, 5))
print('Количество вызовов =', add.call_count)

# Декоратор check_count_args
# Напишите декоратор check_count_args, который проверяет количество переданных аргументов. Проверка заключается в следующем
# -в оригинальную функцию должно быть передано только два аргумента и неважно позиционно или по ключу. Если это условие
# выполняется, возвращаем результат вызова оригинальной функции
# -Если передано меньшее количество, декоратор должен вывести строку «Not enough arguments» и не должен запускать
# оригинальную функцию;
# -Если передано более двух аргументов, то декоратор должен вывести строку «Too many arguments» и не должен запускать
# оригинальную функцию.
#
# Не забывайте сохранять имя функции и строку документации. Для решения необходимо написать только реализацию декоратора
# check_count_args

from functools import wraps


def check_count_args(func):
    @wraps(func)
    def inner_check(*args, **kwargs):
        if len(args) + len(kwargs) == 2:
            return func(*args, **kwargs)

        if len(args) + len(kwargs) < 2:
            print("Not enough arguments")

        if len(args) + len(kwargs) >= 3:
            print("Too many arguments")

    return inner_check

@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


print(add_numbers(6, y=7))
print(add_numbers.__name__)
print(add_numbers.__doc__.strip())


# Декоратор cache_result
# Кэширование – это способ оптимизации работы приложения, при котором повторно запрашиваемые данные сохраняются
# и далее используются для обслуживания последующих запросов. Кешом называется место, куда будут сохраняться данные
# после первого вызова.
#
# Ваша задача написать декоратор cache_result, который оптимизирует производительность за счет сохранения и извлечения
# результатов функций, устраняя избыточные вычисления для повторяющихся входных данных и улучшая скорость отклика
# приложения, особенно для длительных вычислений.
# Взгляните на пример ниже

@cache_result
def multiply(a, b):
    return f"Product = {a * b}"

print(multiply(4, 5))  # Вызываем 1й раз функцию с аргументами 4 и 5. Идет сохранение результата

print(multiply(4, 5))  # При повторном вызове достаем из кеша

print(multiply(5, 8))  # Впервые вызывает с аргументами 5 и 8
print(multiply(5, 8))  # Достаем из кеша результат вызова multiply(5, 8)
print(multiply(5, 8))  # Вновь достаем из кеша

print(multiply(-3, 7))  # Впервые вычисляем результат вызова multiply(-3, 7), сохраняем в кеше
print(multiply(-3, 7))  # Достаем из кеша multiply(-3, 7)

# Декоратор cache_result должен сохранять результат вызова оригинальной функции с учетом передаваемых аргументов.
#
# При повторном вызове функции с теми же аргументами, результат должен возвращаться из кеша, предварительно
# сопроводив выводом следующего текста на экран
#
# [FROM CACHE] Вызов {имя_функции} = {результат_из_кеша}
# Ваша задача написать только функцию-декоратор cache_result

from functools import wraps


def cache_result(func):
    cache_dict = {}  # Общий кеш для всех вызовов

    @wraps(func)
    def inner_cache(*args, **kwargs):
        # Создаем ключ, который включает как позиционные, так и именованные аргументы
        key = (args, frozenset(kwargs.items()))

        if key not in cache_dict:
            # Вычисляем результат, если его нет в кеше
            result = func(*args, **kwargs)
            cache_dict[key] = result  # Сохраняем результат в кеш
            return result
        else:
            # Если результат уже в кеше, выводим его и возвращаем
            cached_result = cache_dict[key]
            print(f'[FROM CACHE] Вызов {func.__name__} = {cached_result}')
            return cached_result

    return inner_cache

@cache_result
def multiply(a, b):
    return a * b


print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(5, 4))
print(multiply.__name__)

# Декоратор counting_calls - 2
# Усовершенствуем ранее созданный декоратор counting_calls, добавив отслеживание переданных аргументов при каждом вызове.
#
# Для этого декоратор counting_calls должен добавить в декорируемой функции атрибут calls - список, в который будут
# сохраняться все переданные аргументы в момент вызова в виде словаря. Каждый словарь должен иметь два ключа:
# args и kwargs для сохранения соответствующих аргументов.

from functools import wraps

def counting_calls(func):
    # Устанавливаем атрибут call_count внутри самой функции, а не внутри декоратора
    @wraps(func)
    def inner(*args, **kwargs):
        # Увеличиваем счетчик вызовов
        inner.call_count += 1

        # Добавляем текущие args и kwargs в список calls
        inner.calls.append({'args': args, 'kwargs': kwargs})

        # Вызываем оригинальную функцию и возвращаем ее результат
        return func(*args, **kwargs)

    # Инициализируем счетчик вызовов и список calls
    inner.call_count = 0
    inner.calls = []

    return inner

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print('Количество вызовов =', add.call_count)
print(add.calls)

print(add(5, 6))
print(add.calls[1])

# Напишите декоратор check_count_args, который проверяет количество переданных аргументов. Проверка заключается в следующем
# - в оригинальную функцию должно быть передано только два аргумента и неважно позиционно или по ключу. Если это условие
# выполняется, возвращаем результат вызова оригинальной функции
# - Если передано меньшее количество, декоратор должен вывести строку «Not enough arguments» и не должен запускать
# оригинальную функцию;
# Если передано более двух аргументов, то декоратор должен вывести строку «Too many arguments» и не должен запускать
# оригинальную функцию.
# Не забывайте сохранять имя функции и строку документации. Для решения необходимо написать только реализацию
# декоратора check_count_args

from functools import wraps


def check_count_args(func):
    @wraps(func)
    def inner_check(*args, **kwargs):
        if len(args) + len(kwargs) == 2:
            return func(*args, **kwargs)

        if len(args) + len(kwargs) < 2:
            print("Not enough arguments")

        if len(args) + len(kwargs) >= 3:
            print("Too many arguments")

    return inner_check

@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


print(add_numbers(6, y=7))
print(add_numbers.__name__)
print(add_numbers.__doc__.strip())


# Декоратор cache_result
# Кэширование – это способ оптимизации работы приложения, при котором повторно запрашиваемые данные сохраняются и далее
# используются для обслуживания последующих запросов. Кешом называется место, куда будут сохраняться данные после первого
# вызова.
#
# Ваша задача написать декоратор cache_result, который оптимизирует производительность за счет сохранения и извлечения
# результатов функций, устраняя избыточные вычисления для повторяющихся входных данных и улучшая скорость отклика
# приложения, особенно для длительных вычислений.
# Декоратор cache_result должен сохранять результат вызова оригинальной функции с учетом передаваемых аргументов.
#
# При повторном вызове функции с теми же аргументами, результат должен возвращаться из кеша, предварительно
# сопроводив выводом следующего текста на экран
#
# [FROM CACHE] Вызов {имя_функции} = {результат_из_кеша}

from functools import wraps


def cache_result(func):
    cache_dict = {}  # Общий кеш для всех вызовов

    @wraps(func)
    def inner_cache(*args, **kwargs):
        # Создаем ключ, который включает как позиционные, так и именованные аргументы
        key = (args, frozenset(kwargs.items()))

        if key not in cache_dict:
            # Вычисляем результат, если его нет в кеше
            result = func(*args, **kwargs)
            cache_dict[key] = result  # Сохраняем результат в кеш
            return result
        else:
            # Если результат уже в кеше, выводим его и возвращаем
            cached_result = cache_dict[key]
            print(f'[FROM CACHE] Вызов {func.__name__} = {cached_result}')
            return cached_result

    return inner_cache

@cache_result
def add(a, b):
    return a + b

print(add(4, 4)) # 1й раз с такими атрибутами
print(add(4, 5)) # 1й раз с такими атрибутами
print(add(4, 6)) # 1й раз с такими атрибутами
print(add(4, 5)) # достаем из кеша
print(add(5, 4)) # 1й раз с такими атрибутами
print(add(6, 3)) # 1й раз с такими атрибутами
print(add(a=6, b=3)) # 1й раз с такими атрибутами: позицицинные!=именованные
print(add(a=6, b=3)) # достаем из кеша

# Декоратор counting_calls - 2
# Усовершенствуем ранее созданный декоратор counting_calls, добавив отслеживание переданных аргументов при каждом вызове.
#
# Для этого декоратор counting_calls должен добавить в декорируемой функции атрибут calls - список, в который будут
# сохраняться все переданные аргументы в момент вызова в виде словаря. Каждый словарь должен иметь два ключа:
# args и kwargs для сохранения соответствующих аргументов.

from functools import wraps


def counting_calls(func):
    # Устанавливаем атрибут call_count внутри самой функции, а не внутри декоратора
    @wraps(func)
    def inner(*args, **kwargs):
        # Увеличиваем счетчик вызовов
        inner.call_count += 1

        # Добавляем текущие args и kwargs в список calls
        inner.calls.append({'args': args, 'kwargs': kwargs})

        # Вызываем оригинальную функцию и возвращаем ее результат
        return func(*args, **kwargs)

    # Инициализируем счетчик вызовов и список calls
    inner.call_count = 0
    inner.calls = []

    return inner

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(7, 5))
print(add(12, 45))
print('Количество вызовов =', add.call_count)
print(add.calls[2])

print(add(b=11, a=22))
print(add.calls[3])