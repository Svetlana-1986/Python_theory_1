# Декоратор с параметром
# Теперь самый интересный прием: что если создать не декоратор, а функцию, которая создает и возвращает декоратор.
# Тогда нам потребуется создать еще один уровень вложенности и подвинуть на один уровень отступов вправо процесс создания
# декоратора. Назовем эту функцию decorator_factory, вот ее код

def decorator_factory():
    print('Запуск функции создания декоратора')

    def decorator(fn):
        print("Запуск декоратора")
        def wrapper(*args, **kwargs):
            print("Запуск функции wrapper")
            return fn(*args, **kwargs)
        return wrapper
    return decorator


print('Начало работы')


@decorator_factory() # обратите внимание на оператор вызова
def original_func():
    print('Запуск оригинальной функции')

original_func()

# Если не пользоваться синтаксическим сахаром, то строчки
@decorator_factory()
def original_func():
    print('Запуск оригинальной функции')

original_func()
# равнозначны следующим
def original_func():
    print('Запуск оригинальной функции')

decorator = decorator_factory() # получаем декоратор из decorator_factory
original_func = decorator(original_func) # декорируем
# или даже так
original_func = decorator_factory()(original_func)

# И вот дойдя до этой конструкции, вы можете обратить внимание на возможность передачи аргументов внутрь decorator_factory.
# Именно decorator_factory может принять необходимое количество позиционных и именованных аргументов, к которым можно
# получить доступ из любого места внутри decorator_factory , включая вложенные функции

def decorator_factory(a, b):
    print('Запуск функции создания декоратора')

    def decorator(fn):
        print("Запуск декоратора")
        def wrapper(*args, **kwargs):
            print("Запуск функции wrapper")
            print('Переданные переменные: ', a, b)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


print('Начало работы')

@decorator_factory(10, 20)
def original_func():
    print('Запуск оригинальной функции')

original_func()

# Пример
def html_tag(name_tag='h1'):
    def decorator(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{name_tag}>{result}</{name_tag}>'
        return inner
    return decorator

@html_tag('p')
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'

@html_tag('h4')
def say_bye(name, surname):
    return f'Bye-bye {name} {surname}'

print(say_hello_to('Kostya', 'Genich'))
print(say_bye('Vasiliy', 'Ytkin'))

#<p>Hello Kostya Genich</p>
# <h4>Bye-bye Vasiliy Ytkin</h4>

# Пример декорирования ниже

@html_tag('p')
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'
# в ручном варианте будет выглядеть следующим образом

def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


say_hello_to = html_tag('p')(say_hello_to)

# Не забываем про wraps
from functools import wraps

def html_tag(name_tag='h1'):
    def decorator(func):

        @wraps(func) # Применяем wraps
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{name_tag}>{result}</{name_tag}>'

        return inner

    return decorator

@html_tag('p')
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


print(say_hello_to.__name__) # печатает 'say_hello_to'

# Cоздадим декоратор-функцию cached_with_expiry, который позволит нам кешировать данные, причем с возможностью
# хранения данных в кеше на определенное время. Данные в кеше будут храниться заведомо известное количество времени, по истечению которого мы будем считать, что данные становятся устаревшими и уже не могут быть использованы.

# Для реализации такого функционала нам понадобится модуль time

import time
# В нем есть функции, позволяющие определить текущий момент времени, найти разницу между моментами времени и сделать
# паузу в выполнении программы.

import time

a = time.time()
print(f'Текущий момент времени {a}')
time.sleep(2)
b = time.time()
print(f'Следующий момент времени {b}')
print(f'Разница между временами {b-a}')

# Модуль time мы будем использовать для нахождения разницы во времени. Теперь самое главное - декоратор cached_with_expiry,
# он будет принимать параметр expiry_time - время хранения кеша в секундах. Реализация декоратора cached_with_expiry
# будет следующая

import time


def cached_with_expiry(expiry_time):
    def decorator(original_function):
        cache = {} # словарь для хранения кеша

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())
            if key in cache:
                cached_value, cached_timestamp = cache[key] #распаковываем в 2 переменные
                if time.time() - cached_timestamp < expiry_time:
                    return f"[CACHED] - {cached_value}"

            result = original_function(*args, **kwargs)
            cache[key] = (result, time.time())

            return result

        return wrapper

    return decorator


@cached_with_expiry(expiry_time=5)  # Устанавливаем время кеширования 5 сек
def get_product(x, y):
    return x * y


print(get_product(23, 5))  # Вычисляем в первый раз
print(get_product(23, 5))  # Во второй раз срабатывает кеш
time.sleep(5)
print(get_product(23, 5))  # Кеш просрочился, поэтому вновь вычисляется значение

# Задачи
# Валидация args - 2
# Помните декоратор validate_all_args_str, который проверял, что все переданные позиционные значения являются строками?
# А если вдруг нам потребуется создать декоратор, который будет проверять аргументы не на принадлежность к строке, а,
# скажем, к списку или числу? Тогда нам понадобится создавать отдельный декоратор на каждый тип данных. Или сделать
# параметризированный декоратор validate_all_args, который будет принимать тип данных в качестве аргумента и проверять,
# что все значения в args относятся к переданному типу данных.
#
# Ваша задача написать такой декоратор validate_all_args, который имеет параметр type_. Если все позиционные аргументы
# принадлежат типу type_, то запускается оригинальная функция; в противном случае необходимо отменить ее запуск и вывести сообщение:
#
# Все аргументы должны принадлежать типу {type_}

from functools import wraps

def validate_all_args(type_):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            # Проверяем, что все аргументы в *args принадлежат типу type_
            if all(isinstance(arg, type_) for arg in args):
                return func(*args, **kwargs)
            else:
                print(f"Все аргументы должны принадлежать типу {type_}")
        return inner
    return wrapper

@validate_all_args(int)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)

# Декоратор compose
# Ваша задача написать параметризированный декоратор compose, который принимает произвольное количество функций и
# применяет их последовательно к результату декорируемой функции

from functools import wraps

def compose(*functions):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rez = func(*args, **kwargs) #сохраняем в переменную результат вызова оригинал функции
            for function in functions: # проходим циклом по функциям поступающим в compose
                rez = (function(rez)) # сохраняем результат каждой функции в одну и ту же переменную
            return rez

        return wrapper

    return decorator


def double_it(a):
    return a * 2


def increment(a):
    return a + 1


@compose(double_it, increment)
def get_sum(*args):
    return sum(args)


print(get_sum(5))
print(get_sum(20, 10))
print(get_sum(5, 15, 25))

# Декоратор add_attrs
# Ваша задача написать параметризированный декоратор add_attrs, который принимает произвольное количество именованных
# аргументов и на их основании добавляет новые атрибуты для оригинальной функции

from functools import wraps


def add_attrs(**attrs):
    def wrapper(func):
        # Добавляем атрибуты к оригинальной функции func.  Атрибуты добавляются прямо к оригинальной функции func, а не к её обёрнутой версии inner. Это позволяет иметь доступ к атрибутам через саму функцию add, а не её обёртку.
        for key, value in attrs.items():
            setattr(func, key, value)

        @wraps(func)  # Сохраняем метаданные оригинальной функции
        def inner(*args, **kwargs):
            return func(*args, **kwargs)  # Вызываем оригинальную функцию

        return inner

    return wrapper

@add_attrs(test=True, ordered=True)
def add(a, b):
    return a + b

print(add(10, 5))
print(add.test)
print(add.ordered)

