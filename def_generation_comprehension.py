a = "123456789101112131415161718192021"
a = list(a)
print(*a, end = ' ')

# Выражение-генератор — это высокопроизводительное, эффективное с точки зрения памяти обобщение генераторов списков
# (list comprehension) и генераторов. По сути, выражение-генератор представляет собой способ создания генератора
# с использованием синтаксиса, очень похожего на синтаксис генератора списка. Разница лишь в том, что нужно указывать круглые скобки () вместо квадратных [].
# Вот взгляните как мы ранее создавали список квадратов при помощи list comprehension
# (expression for item in collection)


lst_of_squares = [num**2 for num in range(5)]
print(lst_of_squares) # [0, 1, 4, 9, 16]

# Стоит нам только заменить в этом выражении квадратные скобки на круглые, мы сразу получим в результате объект
# генератор-итератор, который может взаимодействовать с функцией next
gn_of_squares = (num ** 2 for num in range(5))
print(gn_of_squares)

print(next(gn_of_squares)) # 0
print(next(gn_of_squares)) # 1
print(next(gn_of_squares)) # 4

# Вот пример такого генератора, который берет только четные числа из range
gen = (i for i in range(1, 10) if i % 2 == 0)

print(next(gen))
print(next(gen))
print(next(gen))

# Можно использовать тернарный оператор
gen = ((i, 'Even') if i % 2 == 0 else (i, 'Odd') for i in range(1, 10))

print(next(gen))
print(next(gen))
print(next(gen))

# Вложенность в выражениях-генераторах
# В list comprehension можно было использовать вложенные циклы. При помощи вложенности можно заменять программы,
# в которых идет заполнение списка определенными значениями. В примере ниже как раз код, заполняющий список кортежами
# из пары значений

matrix = []

for i in range(3):
    for j in range(4):
        matrix.append((i, j))
print(matrix)

# Через list comprehension блок кода  из двух циклов можно заменить всего одной строчкой

matrix = [(i, j) for i in range(3) for j in range(4)]
print(matrix)
# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1),
#  (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

# Данный пример можно переписать из list comprehension в генераторное выражение. Синтаксис такой же, только
# вместо квадратных скобок указываем круглые
gen = ((i, j) for i in range(3) for j in range(4))

for value in gen:
    print(value)

# Выражения-генераторы не хранят в себе всю коллекцию элементов, они выполняют "ленивые" вычисления с целью выдачи
# одного значения по запросу. List comprehension, напротив, сохраняет в один список сразу все элементы.
# Отсюда сразу возникает разница в объеме занимаемой памяти. Взгляните на этот пример

import sys

nums_lst = [num ** 2 for num in range(100000)]
nums_gen = (num ** 2 for num in range(100000))

print(sys.getsizeof(nums_lst))  # 800984

print(sys.getsizeof(nums_gen))  # 104

# Выражения-генераторы как замена map и/или filter
def get_square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

numbers = [4, 2, 1, 5, 7, 9, 6, 18]
squares = map(get_square, filter(is_even, numbers))
print(next(squares))  # 16
print(next(squares))  # 4

# Эту же задачу можно выполнить, используя выражение-генератор. Вот пример реализации:
(get_square(n) for n in numbers if is_even(n))
# Результатом будет объект генератор, который также лениво по запросу будет выдавать одно значение
def get_square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

numbers = [4, 2, 1, 5, 7, 9, 6, 18]
squares = (get_square(n) for n in numbers if is_even(n))
print(next(squares))  # 16
print(next(squares))  # 4

# Операции, которые выражения-генераторы не поддерживают len, операцию индексирования, Выражения-генераторы можно
# обходить только один раз. Если вам нужно вновь пройтись по элементам, создавайте новый объект генератора
# При преобразовании выражения-генератора к типам list, tuple, set также будет произведена итерация по всем элементам
# генератора. Повторная попытка преобразовать ошибкой не закончится, но и элементов в коллекции уже не будет
# Выражения-генераторы не поддерживают работу с функцией reversed

# Задача:
# Давайте напишем выражение-генератор, который будет генерировать кортеж состоящий из двух элементов: номера дня в году и названия дня недели.
#
# За начало отсчета возьмем наш «любимый» 2022 год. Он начался в субботу, потом воскресенье, понедельник, вторник, ..., пятница, суббота и далее по кругу
#
# Результат выражения-генератора сохраните в переменную days
#
# Названия дней недели должны совпадать с этими значениями:
#
# ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Значит при первой итерации генератор должен вернуть кортеж
#
# (1, 'Saturday')
# При второй итерации вернется значение
#
# (2, 'Sunday')
# Ваша задача распечатать на удачу первые 77 дней 2022 года.

days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = ((i + 1, days_week[(5 + i) % 7]) for i in range(365)) # i + 1,т.к. индексация списка начинается с 0,
                                                             #(5 + i) % 7  - 5 т.к. это индекс "Saturday" в                                                                 списке
for i in range(77):
    print(next(days))



