# Замыкания (Closure)
# В этом уроке мы познакомимся с темой, которая часто вызывает у новичков проблемы с ее пониманием. Данная тема
# называется  «Замыкание», базируется на следующих знаниях:
#
#      ➕ функции являются объектами первого класса, значит их можно сохранять в переменные и удалять, хранить
#      в структурах данных, передавать в качестве аргументов другим функциям, использовать в качестве возвращаемых
#      значений и т. д. Среди всех этих свойств давайте выделим последнее — «использовать в качестве возвращаемых
#      значений», именно оно нам пригодится
#
#     ➕ вложенные функции
#
#     ➕ объемлющая область видимости, которая позволяет внутренним функциям использовать переменные объемлющих функций
#
# На этих трех китах базируется понятие «Замыкание»

# Замыкание (closure) — функция, которая находится внутри другой функции и ссылается на переменные объявленные в
# теле объемлющей функции (нелокальные переменные).

# Не раз на протяжении этого курса я вам говорил, что локальная область видимости создается в момент вызова функции
# и исчезает, как только функция завершит свою работу. Все локальные переменные функции бесследно исчезают. Все это верно,
# но, как всегда, есть исключения. В python таким исключением является замыкание, оно позволяет за счет объемлющей области
# видимости упаковать воедино объект внутренней функции и состояние всех свободных переменных и вернуть все это великолепие
# в качестве результата.
#
# Вот три шага, которые вам необходимо сделать, чтобы определить замыкание:
#
#     ➖ Создайте внутреннюю функцию.
#
#     ➖ Определите переменные в объемлющей функции.
#     ➖ Верните внутреннюю функцию в качестве результата без вызова.

def main_func():

    name = 'Ivan'

    def inner_func():
        print('hello my friend', name)

    return inner_func

f = main_func()
print(f.__name__)
f()
f()

# В переменной f после вызова main_func() хранится ссылка на объект функции inner_func. Не смотря на то, что переменная
# name была создана вне функции inner_func, она осталась доступна и используется ей для вывода информации.
#
# То есть получается, что после main_func() завершения работы функции main_func(), ее локальная переменная
# не уничтожилась, сохранила свое значение и используется при каждом новом вызове. «Как такое возможно?» - спросите вы.
# Ответ прост: ни один объект в python не уничтожается, пока на него хранится ссылка. В нашем случае внутренняя
# функция inner_func «захватила» ссылку на объект 'Ivan', хранящийся в переменной name, и не хочет его отпускать даже
# после завершения работы функции main_func().

# Замыкания позволяют сохранять состояние внутренней функции и значения переменных из объемлющей области видимости.

# Замыкание заставляет внутреннюю функцию сохранять состояние ее окружения при вызове. Замыкание — это не сама внутренняя
# функция, а внутренняя функция вместе с ее объемлющем окружением. Замыкание «захватывает» локальные переменные
# объемлющей функции и сохраняет их.

def adder(start_value):
    def inner(income):
        return start_value + income

    return inner


add_from_2 = adder(2)
add_from_7 = adder(7)

print(add_from_2(5))
print(add_from_2(3))

print(add_from_7(4))
print(add_from_7(9))

# В переменной add_from_2 сохранится объект внутренней функции inner с зафиксированным значением переменной
# start_value равной 2. Следовательно, сделав вызов add_from_2(5) мы будем складывать пятерку с двойкой, а при вызове
# add_from_2(3) мы найдем сумму 2 и 3.
#
# В следующем примере мы будем пользоваться оператором nonlocal для изменения значения свободной переменной. Это нам
# необходимо, чтобы создать замыкание, умеющее подсчитывать количество раз своего вызова. Для этого нам понадобится
# завести переменную-счетчик count внутри замыкания. При каждом новом вызове мы должны увеличивать счетчик на единицу.
# Вот пример реализации такой функции

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

q = counter()
r = counter()
print(q())
q()
print(q())
print(r())


# Задачи
# Ваша задача создать функцию-замыкание create_accumulator, которая должна накапливать (суммировать) внутри себя все
# значения, которые ей будут переданы. При создании замыкания стартовая сумма должна быть равна нулю. Посмотрите пример
# ниже:
#
# summator_1 = create_accumulator()
# print(summator_1(1)) # печатает 1
# print(summator_1(5)) # печатает 6
# print(summator_1(2)) # печатает 8
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7
# При каждом вызове должна возвращаться накопленная сумма, которая хранится в замыкании.
#
# Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
#
# Необходимо только определить функцию-замыкание create_accumulator, остальное мы сделаем за вас

def create_accumulator():
    sum = 0

    def sum_create_accumulator(digit):
        nonlocal sum
        sum += digit
        return sum

    return sum_create_accumulator

summator_1 = create_accumulator()
print(summator_1(5))
print(summator_1(7))
print(summator_1(2))

summator_2 = create_accumulator()
print(summator_2(3))
print(summator_2(6))

# Напишите функцию-замыкание countdown, которая будет вести обратный отсчёт от переданного числа N до нуля. После того как
# замыкание будет вызвано более N раз, необходимо выводить сообщение «Превышен лимит, вы вызвали более N раз»

def countdown(N):
    count = N

    def check():
        nonlocal count
        if count > 0:
            print(count)
            count -= 1
        else:
            print(f"Превышен лимит, вы вызвали более {N} раз")

    return check

count = countdown(3)
count()
count()
count()
count()
count()

# В этом задании вам нужно сделать функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
# Особенность этого замыкания заключается в том, что количество вызовов должно храниться в атрибуте total_calls.

def count_calls():
    total_calls = 0  # Переменная для хранения количества вызовов

    def inner():
        nonlocal total_calls  # Указываем, что используем переменную из внешнего окружения
        total_calls += 1  # Увеличиваем счетчик на 1
        inner.total_calls = total_calls  # Обновляем атрибут total_calls
        return total_calls  # Возвращаем текущее значение вызовов

    inner.total_calls = total_calls  # Атрибут для хранения количества вызовов
    return inner  # Возвращаем внутреннюю функцию

counter = count_calls()
counter()
counter()
print(counter.total_calls)
counter()
print(counter.total_calls)

# В следующем примере мы будем передавать в качестве параметра для замыкания функцию. Далее мы хотим, чтобы в замыкании
# происходил подсчет количества вызовов переданной функции. Вот такой код мы получаем

# При каждом новом вызове будет увеличиваться счетчик count и заодно будет выводится сообщение о том, какая функция и
# какое количество раз была вызвана на данный момент.

def add(a, b):
    return a + b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args,**kwargs)

    return inner
q = counter(add)

q(10, 20)
q(2,5)

# Это получилось следующим образом: мы вызвали функцию counter и передали ей в качестве аргумента объект-функцию add.
# Далее в переменной q сохранится наше замыкание (функция inner), и когда мы будем вызывать q будет отрабатывать код,
# находящийся в функции inner. Он увеличивает счётчик, говорим какая именно наша функция вызывалась и сколько раз,
# а далее идёт вызов самой функции func, в ней, напомню, сохранилась функция add.

# В следующем примере мы напишем функцию-замыкание timer, которая позволяет определить сколько прошло времени с момента
# создания замыкания. Для того, чтобы работать со временем в python, нам потребуется помощь модуля datetime.
# В нем есть функция datetime.now(), которая отображает текущее время на момент вызова. Первым делом необходимо
# импортировать нужную функцию
#
# from datetime import datetime
# а затем можно ей пользоваться. Полный код, печатающий текущее время, будет выглядеть так
#
# from datetime import datetime
#
# print(datetime.now())
# Вот попробуйте поэкспериментировать с данной программой:

from datetime import datetime

print(datetime.now())

# В следующем примере мы напишем функцию-замыкание timer, которая позволяет определить сколько прошло времени с момента
# создания замыкания. Для того, чтобы работать со временем в python, нам потребуется помощь модуля datetime. В нем есть
# функция datetime.now(), которая отображает текущее время на момент вызова. Первым делом необходимо импортировать нужную функцию
#
# from datetime import datetime
# а затем можно ей пользоваться. Полный код, печатающий текущее время, будет выглядеть так
#
from datetime import datetime
print(datetime.now())

# Данную программу можно переписать с использованием другого встроенного модуля time. В нем также есть функция
# perf_counter, которая определяет текущий момент времени, плюс есть функция sleep, позволяющая делать паузы в выполнении
# программы на определенное количество секунд. Вот как будет выглядеть наша программа

from time import perf_counter, sleep


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


q = timer()
sleep(1)  # делаем паузу в 1 секунду
print(q())
sleep(2)  # делаем паузу в 2 секунды
print(q())
sleep(3)  # делаем паузу в 3 секунды
print(q())

# Несколько функций в замыкании
def create_counter():
    count = 0

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    return increment, decrement


inc_1, dec_1 = create_counter()
print(inc_1())  # увеличиваем на 1
print(inc_1(2))  # увеличиваем на 2
print(inc_1(3))  # увеличиваем на 3
print(dec_1())  # уменьшаем на 1
print(dec_1())  # уменьшаем на 1

print('-' * 15)
print('Создаем новый объект замыкания с другим счетчиком')

inc_2, dec_2 = create_counter()
print(inc_2(10))  # увеличиваем на 10
print(dec_2(5))  # уменьшаем на 5
print(inc_2(100))  # увеличиваем на 100
print(inc_2(50))  # увеличиваем на 50
print(dec_2())  # уменьшаем на 1


def create_counter():
    count = 0
    def inner():
        pass

    def increment(value: int = 1):
        nonlocal count
        count += value
        return count

    def decrement(value: int = 1):
        nonlocal count
        count -= value
        return count

    inner.inc = increment
    inner.dec = decrement
    return inner

ex1 = create_counter()
print(ex1.inc(3))
print(ex1.inc(5))
print(ex1.inc(90))

ex2 = create_counter()
print(ex2.inc(1))
print(ex2.inc(2))
print(ex2.inc(23))

# Ваша задача — создать функцию-замыкание create_dict. Функция create_dict должна сохранять в себе в виде словаря
# все значения, которые ей будут переданы. Ключами данного словаря должны быть натуральные числа, равные номеру
# вызова данной функции. Посмотрите пример ниже:

f_1 = create_dict()
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict() # создаем новое замыкание в f_2
print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}


# Вызывая первый раз f_1 мы создали пару 1: 'hello', вызывая второй раз добавилась пара 2: 100. и т.д.
# При каждом вызове должен возвращаться словарь, хранящийся в замыкании
# Необходимо только определить функцию-замыкание create_dict, остальное мы сделаем за вас

def create_dict():
    values_dict = {}
    call_count = 0

    def inner(value):
        nonlocal call_count
        call_count += 1
        values_dict.setdefault(call_count, value)
        return values_dict

    return inner

f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))

#
# Ваша задача — создать функцию-замыкание create_dict. Функция create_dict должна сохранять в себе в виде словаря
# все значения, которые ей будут переданы. Ключами данного словаря должны быть натуральные числа, равные номеру вызова
# данной функции. Посмотрите пример ниже:

f_1 = create_dict()
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict() # создаем новое замыкание в f_2
print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
#
# Вызывая первый раз f_1 мы создали пару 1: 'hello', вызывая второй раз добавилась пара 2: 100. и т.д.
#
# При каждом вызове должен возвращаться словарь, хранящийся в замыкании
#
# Необходимо только определить функцию-замыкание create_dict, остальное мы сделаем за вас

def create_dict():
    # Создаем пустой словарь для хранения значений
    values_dict = {}
    # Счетчик для номеров вызовов
    call_count = 0

    # Внутренняя функция, которая добавляет новое значение в словарь
    def inner(value):
        nonlocal call_count  # Объявляем, что будем использовать переменную из внешней области видимости
        call_count += 1  # Увеличиваем счетчик вызовов
        values_dict[call_count] = value  # Добавляем новое значение в словарь
        return values_dict  # Возвращаем обновленный словарь

    return inner  # Возвращаем внутреннюю функцию


# Примеры использования
f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))  # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3]))  # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()  # создаем новое замыкание в f_2
print(f_2('PoweR'))  # f_2 возвращает {1: 'PoweR'}

# Атрибуты

def create_dict():
    # Создаем функцию, которая будет обрабатывать вызовы
    def inner(value):
        # Увеличиваем счетчик вызовов и добавляем значение в словарь
        inner.call_count += 1
        inner.values_dict[inner.call_count] = value
        return inner.values_dict

    # Инициализируем атрибуты функции
    inner.call_count = 0  # Счетчик вызовов
    inner.values_dict = {}  # Словарь для хранения значений

    return inner  # Возвращаем внутреннюю функцию

# Примеры использования
f_1 = create_dict()
print(f_1('hello'))  # f_1 возвращает {1: 'hello'}
print(f_1(100))      # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()  # создаем новое замыкание в f_2
print(f_2('PoweR'))  # f_2 возвращает {1: 'PoweR'}

# Функция create_dict: Создает и возвращает внутреннюю функцию inner, которая будет принимать значения.
#
# Атрибуты функции: Мы добавляем два атрибута к функции inner:
#
# call_count: хранит количество вызовов функции.
# values_dict: словарь, в который будут добавляться переданные значения.
# Логика обработки: Каждый раз при вызове inner увеличивается call_count, и новое значение добавляется в values_dict.
# Затем возвращается обновленный словарь.


