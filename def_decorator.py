# Декоратор — это функция, которая позволяет обогатить любую другую функцию дополнительным поведением без необходимости
# изменения ее кода. Декоратор очень часто называют оберткой для функции, потому что он оборачивает ее и позволяет
# добавить новый функционал как перед вызовом функции, так и после завершения ее работы.

# Прежде чем мы создадим свой первый декоратор, давайте перечислим основные концепции, на которых базируются декораторы
#
# Функция — это объект, ее можно присваивать переменным и обращаться через данную переменную.
def my_function():
    print('Hello world')


say_hello = my_function
say_hello()

# Функция может быть вложена в другую функцию.
def my_function():
    def inner_function():
        print('Hello world from inner function')

    inner_function()

my_function()

# Функция может возвращать другую функцию в качестве результата
def my_function():
    message = 'Hello world from inner function'

    def inner_function():
        print(message)

    return inner_function


result = my_function()
result()
# Функцию можно передать в другую функцию в качестве аргумента
def apply_function(func):
    func()
    print('I applied function')


def say_hello():
    print('Hello world')


apply_function(say_hello)

# Создание декоратора
#
# Чтобы создать декоратор, необходимо определить внешнюю функцию, которая будет принимать функцию в качестве аргумента.
# Затем внутри внешней функции необходимо создать внутреннюю функцию, в которой будет происходить вызов декорированной
# функции. Как правило, вызов окружается какими-либо дополнительными действиями, согласно следующему синтаксису
# базовый синтаксис декоратора в python

def my_decorator(func):

    def wrapper_func():
        # Делаем что-то до вызова функции
        func()
        # Делаем что-то после вызова функции

    return wrapper_func
# На основании данного синтаксиса давайте напишем декоратор, который будет выводить сообщение «Start decorator» перед
# вызовом функции и сообщение «Finish decorator» после вызова. Вот как будет выглядеть данный код

def decorator(func):

    def wrapper():
        print('Start decorator')
        func()
        print('Finish decorator')

    return wrapper
# Вызов функции decorator будет возвращать внутреннюю функцию wrapper, которая декорирует или, другими словами, обрамляет
# входную функцию func двумя принтами: первый print сработает до вызова функции func(), второй - после вызова.

# Декоратор - это функция, которая принимает исходную функцию и возвращает другую функцию, как правило, с дополненным
# поведением

# определяем декоратор
def decorator(func):

    def wrapper(): # определяем функцию, которая будет подменять поведение оригинальной
        print('Start decorator') # вывод перед вызовом оригинальной функции
        func()   # вызов оригинальной функции
        print('Finish decorator') # вывод после вызова оригинальной функции

    return wrapper # возвращаем функцию, которая заменит оригинальную функцию


def say_hello():
    print('Hello world')

# декорируем функцию say_hello
say_hello = decorator(say_hello)

# вызываем say_hello
say_hello()

print('--------')

# определяем новую функцию say_bye
def say_bye():
    print('bye world')

# декорируем функцию say_bye
say_bye = decorator(say_bye)

# вызываем say_bye
say_bye()

# Чтобы объединить процесс определения функции и ее декорирования, а также сократить код, был придуман специальный
# синтаксис применения декоратора при помощи символа @, описанный в PEP 318. Согласно PEP 318, чтобы заменить следующий код

def say_hello():
    print('Hello world')

# декорируем функцию say_hello
say_hello = decorator(say_hello)
# вам достаточно написать название декоратора над заголовком функции, поставив вперед символ @

@decorator
def say_hello():
    print('Hello world')

# Вот взгляните, как это работает

def decorator(func):
    def inner():
        print('Стартуем декоратор')
        func()
        print('Заканчиваем декоратор')

    return inner


@decorator
def say_hello():
    print('hello world')


@decorator
def say_bye():
    print('bye world')


say_hello()
print('--------')
say_bye()
# Можно сказать, что мы навесили декоратор decorator на функции say_hello() и say_bye().

# Работа с параметрами и атрибутами при декорировании

# Наша задача пробросить параметры name_inner и surname_inner дальше нашей функции func. Давайте это сделаем.

def decorator(func):
    def inner(name_inner, surname_inner):
        print('Стартуем декоратор')
        func(name_inner, surname_inner)
        print('Заканчиваем декоратор')
    return inner


@decorator
def say_hello_to(name, surname):
    print('hello', name, surname)


say_hello_to('Vasya', 'Ivanov')

 # Вот так будет выглядеть финальная версия декоратора, которая может обработать любое количество аргументов

def decorator(func):
    def inner(*args, **kwargs):
        print('Стартуем декоратор')
        func(*args, **kwargs)
        print('Заканчиваем декоратор')
    return inner


@decorator
def say_hello_to(name, surname):
    print('hello', name, surname)

say_hello_to('Vasya', 'Ivanov')

@decorator
def say_hello_to_all(*args):
    for name in args:
        print('Hello', name)

say_hello_to_all('Dima', 'Andrei', 'Pasha')

# Здесь обратите внимание на две вещи, которые необходимо сделать:
#
# объявить параметры во внутренней функции
# def inner(*args, **kwargs):
# пробросить все принятые аргументы дальше в декорируемую функцию func
# func(*args, **kwargs)

# Работа с возвращаемым значением
# С параметрами работать научились, теперь давайте разбираться с возвращаемым значением. Все функции, с которыми мы работали выше, ничего не возвращали. Но мы то с вами знаем, что под фразой ничего не возвращали кроется на самом деле значение None. То есть все наши функции возвращали значение None. Давайте убедимся в этом, сохранив результат работы декоратора в переменную

def decorator(func):
    def inner(*args, **kwargs):
        print('Стартуем декоратор')
        func(*args, **kwargs)
        print('Заканчиваем декоратор')
        # return None # <- тут подразумевается возврат значения None
    return inner


@decorator
def say_hello_to(name, surname):
    print('hello', name, surname)


res = say_hello_to('Vasya', 'Ivanov')
print(res)
print(res is None)
# Я оставил комментарий, где подразумевается возврат значения None из вложенной функции.
#
# Но вы можете вернуть свое значение из этой вложенной функции, тогда оно вернется как результат вызова декорируемой функции

def decorator(func):
    def inner(*args, **kwargs):
        print('Стартуем декоратор')
        func(*args, **kwargs)
        print('Заканчиваем декоратор')
        return {'args': args, 'kwargs': kwargs}

    return inner


@decorator
def say_hello_to(name, surname):
    print('hello', name, surname)


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')
print(res is None)

# В этом примере я возвращаю словарь, который составлен из параметров args и kwargs, поэтому в одной строке вывода
# мы видим сообщение

res={'args': ('Vasya', 'Ivanov'), 'kwargs': {}}

# Но в переменной res после вызова say_hello_to у нас оказывается словарь. Как правило, внутренние функции
# декоратора возвращают не свои какие-то придуманные значения ( в нашем случае словарь {'args': args, 'kwargs': kwargs}),
# а результат декорируемой функции. Давайте это исправим

def decorator(func):
    def inner(*args, **kwargs):
        print('Стартуем декоратор')
        func_res = func(*args, **kwargs)
        print(f'Функция func вернула значение "{func_res}"')
        print('Заканчиваем декоратор')
        return func_res # изменили возвращаемое значение
    return inner


@decorator
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'

# В декораторах в принципе часто возникают ситуации, когда возвращаемое значение декорируемой функции нужно исказить,
# преобразовать или выполнить определенные проверки. Например, мы можем изменить результат функции say_hello_to таким
# образом, чтобы все заглавные буквы стали строчными, а строчные - заглавными. Взгляните, как мы это сделаем, написав
# декоратор swapcase

def swapcase(func):
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        print(f'Функция func вернула значение "{func_res}"')
        return func_res.swapcase()
    return wrapper


@swapcase
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')

print(say_hello_to('gennadi', 'LOSKOV'))


# К полученному результату в виде строки мы вызываем метод .swapcase(), который как раз меняет регистр у букв на противоположный.
#
# А вот пример реализации декоратора header_h1, который по правилам html-кода обрамляет строку в открывающийся тег <h1> и
# закрывающийся тег </h1>.

def header_h1(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<h1>{result}</h1>'

    return inner


@header_h1
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')

print(say_hello_to('gennadi', 'LOSKOV'))
# В результате вызова say_hello_to('Vasya', 'Ivanov') мы получаем строку

# <h1>Hello Vasya Ivanov</h1>

res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')

# Когда использовать декораторы?
# Декораторы полезно использовать, когда вам нужно изменить поведение функции, не изменяя саму функцию.
# Наиболее типичные примеры декораторов:
#
# логирование вызова функции,
# замер производительности,
# кэширование результата работы,
# проверка прав доступа и т. д.
# Декораторы полезны еще и тем, что они позволяют избежать дублирования кода. Написав один раз функцию декоратор, вы
# можете ее использовать для любых своих функций.

# Работа с возвращаемым значением
# С параметрами работать научились, теперь давайте разбираться с возвращаемым значением. Все функции, с которыми мы
# работали выше, ничего не возвращали. Но мы то с вами знаем, что под фразой ничего не возвращали кроется на самом деле
# значение None. То есть все наши функции возвращали значение None. Давайте убедимся в этом, сохранив результат работы
# декоратора в переменную

# Именно вот здесь между принтами у вас будет осуществляться вызов декорируемой функции и, следовательно, нам нужно
# сохранить возвращаемое значение. Давайте это сделаем

def decorator(func):
    def inner(*args, **kwargs):
        print('Стартуем декоратор')
        func_res = func(*args, **kwargs)
        print(f'Функция func вернула значение "{func_res}"')
        print('Заканчиваем декоратор')
        return {'args': args, 'kwargs': kwargs}
    return inner


@decorator
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')
print(res is None)

# Внутри функции inner нам теперь доступно возвращаемое значение функции say_hello_to, это видно по строке вывода
#
# Функция func вернула значение "Hello Vasya Ivanov"
#
# Но в переменной res после вызова say_hello_to у нас оказывается словарь. Как правило, внутренние функции
# декоратора возвращают не свои какие-то придуманные значения ( в нашем случае словарь {'args': args, 'kwargs': kwargs}),
# а результат декорируемой функции. Давайте это исправим

def decorator(func):
    def inner(*args, **kwargs):
        print('Стартуем декоратор')
        func_res = func(*args, **kwargs)
        print(f'Функция func вернула значение "{func_res}"')
        print('Заканчиваем декоратор')
        return func_res # изменили возвращаемое значение
    return inner


@decorator
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')

# Теперь в глобальной переменной res хранится строка, которая вернулась из функции say_hello_to без какого-либо искажения.
#
# В декораторах в принципе часто возникают ситуации, когда возвращаемое значение декорируемой функции нужно исказить,
# преобразовать или выполнить определенные проверки. Например, мы можем изменить результат функции say_hello_to таким
# образом, чтобы все заглавные буквы стали строчными, а строчные - заглавными. Взгляните, как мы это сделаем, написав
# декоратор swapcase

def swapcase(func):
    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        print(f'Функция func вернула значение "{func_res}"')
        return func_res.swapcase()
    return wrapper


@swapcase
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')

print(say_hello_to('gennadi', 'LOSKOV'))

# К полученному результату в виде строки мы вызываем метод .swapcase(), который как раз меняет регистр у букв
# на противоположный.
#
# А вот пример реализации декоратора header_h1, который по правилам html-кода обрамляет строку в открывающийся тег <h1>
# и закрывающийся тег </h1>.

def header_h1(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<h1>{result}</h1>'

    return inner


@header_h1
def say_hello_to(name, surname):
    return f'Hello {name} {surname}'


res = say_hello_to('Vasya', 'Ivanov')
print(f'{res=}')

print(say_hello_to('gennadi', 'LOSKOV'))
# В результате вызова say_hello_to('Vasya', 'Ivanov') мы получаем строку
# <h1>Hello Vasya Ivanov</h1>


# Напишите декоратор repeater, который трижды вызывает декорированную функцию
#
# Ваша задача написать только определение функции декоратора repeater
ddef repeater(func):

    def inner(*args, **kwargs):
        count = 3 # Объявляем счетчик здесь, чтобы он сбрасывался при каждом вызове
        while count > 0:
            func(*args, **kwargs)
            count -= 1

    return inner


@repeater
def some_func(a, b, c):
    print(a ** b + c)


some_func(4, 5, 4)
some_func(14, 51, 34)

2 вариант решения через For:

def repeater(func):
    def inner(*args, **kwargs):
        for _ in range(3):
            func(*args, **kwargs)
    return inner

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(9, 4)



# Фильтрация аргументов
# Ваша задача создать два декоратора
#
#     1️⃣ filter_even, который фильтрует только позиционные аргументы. Среди всех переданных значений он оставляет только
# четные числа, False и коллекции, длина которых четная
#
#     2️⃣ delete_short, который фильтрует только именованные аргументы. Среди всех переданных значений он оставляет только
# те, имена которых более четырех символов

1 способ

from collections.abc import \
    Iterable  # Модуль collections.abc является частью стандартной библиотеки Python и содержит абстрактные базовые классы (ABC) для различных типов коллекций.Iterable — это абстрактный базовый класс, который определяет интерфейс для объектов, по которым можно итерироваться.


def filter_even(func):
    def wrapper(*args, **kwargs):
        # Фильтруем позиционные аргументы (args)
        filtered_args = [
            arg for arg in args
            if (isinstance(arg, int) and arg % 2 == 0)  # Четные числа
               or arg is False  # Ложное значение
               or (isinstance(arg, Iterable) and len(arg) % 2 == 0)  # Коллекции четной длины
        ]
        return func(*filtered_args, **kwargs)  # возвращаем отфильтрованные args

    return wrapper


def delete_short(func):
    def wrapper(*args, **kwargs):
        # Фильтруем именованные аргументы (kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if len(k) > 4}
        return func(*args, **filtered_kwargs)  # возвращаем отфильтрованные kwargs

    return wrapper

@delete_short
def info_kwargs(**kwargs):
    """Выводит информацию о переданных kwargs"""
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

info_kwargs(first_name="John", last_name="Doe", age=33)

# 2 способ
# Надо решить правильно!!!
def filter_even(func):
    def inner_args(*args, **kwargs):
        # Фильтруем позиционные аргументы (args)
        filtered_args = [
            arg for arg in args
            if (isinstance(arg, int) and arg % 2 == 0)  # Четные числа
               or arg is False  # Ложное значение
               or (hasattr(arg, '__len__') and len(arg) % 2 == 0)  # Коллекции четной длины
        ]
        return func(*filtered_args, **kwargs)  # возвращаем отфильтрованные args

    return inner_args


def delete_short(func):
    def inner_kwargs(*args, **kwargs):
        # Фильтруем именованные аргументы (kwargs)
        filtered_kwargs = {k: v for k, v in kwargs.items() if len(k) > 4}
        return func(*args, **filtered_kwargs)  # возвращаем отфильтрованные kwargs

    return inner_kwargs


@filter_even
def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result


print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))

