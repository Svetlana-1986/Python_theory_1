# Объединить элементы из нескольких коллекций

ids = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
countries = ['Australia', 'USA', 'USA', 'China']
records = zip(ids, leaders, countries)

print(list(records))

# В данном случае длины всех коллекций совпали. Но иногда приходится иметь дело с неравными по длине итерируемыми
# объектами. По умолчанию результат функции zip берётся по длине самой короткой коллекции
#
# Если не хотите отбрасывать элементы, можете воспользоваться zip_longest из модуля itertools.
from itertools import zip_longest

ids = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
countries = ('Australia', 'USA')
records = zip_longest(ids, leaders, countries)

print(list(records))

records_2 = zip_longest(ids, leaders, countries, fillvalue='Unknown')
print(list(records_2))

# Разъединение (распаковка) двух или нескольких коллекций
# Здесь мы продемонстрируем обратную операцию, когда из одной большой коллекции мы получим несколько

record = [(1, 'Elon Mask', 'Australia'),
          (2, 'Tim Cook', 'USA'),
          (3, 'Bill Gates', 'USA'),
          (4, 'Yang Zhou', 'China')]
ids, leaders, countries = zip(*record)
print(ids)
print(leaders)
print(countries)
# С помощью оператора звёздочки выполнена операция распаковки: распакованы все четыре кортежа из списка records

# Итерация двух или нескольких коллекций

# Итерация двух или нескольких коллекций, когда важно брать элементы, стоящие на одинаковых позициях

employee_numbers = [2, 9, 18, 28]
employee_names = ["Valentin", "Leonti", "Andrew", "Sasha"]
salaries = (100, 200, 3000, 450)

for name, number, salary in zip(employee_names, employee_numbers, salaries):
	print(name, number, salary)

# Можно обходить и словари при помощи zip:

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)

# Создание  и обновление словарей

# Еще одним применением объекта zip является создание словарей при помощи двух коллекций. Значения первой
# коллекции будут помещаться в качестве ключа новой пары, а значением будут выступать элементы из второй коллекции.
# Также можно и обновлять пары существующего словаря

employee_numbers = [2, 9, 18]
employee_names = ["Valentin", "Leonti", "Andrew"]

numbers = dict(zip(employee_numbers, employee_names))
employees = dict(zip(employee_names, employee_numbers))

print(numbers)
print('------')
print(employees)
# Допускается и обновление уже существующего словаря новыми значениями

other_num = [50, 63, 2]
other_names = ['Misha', 'Sergey', 'Ivan']
numbers.update(zip(other_num, other_names))
# Обратите внимание на операцию обновления: ключи 50 и 63, так как их не было до начала операции в исходном словаре,
# добавились, а вот ключ 2 был обновлен новым значением.

# В различных comprehension
# Функцию zip, а точнее ее результат можно сразу использовать для обхода. Значит, она является подходящей для
# использования в различных выражениях-comprehension (list comprehension, dict comprehension , set comprehension  и т.д.):

employee_numbers = [2, 9, 18]
employee_names = ["Valentin", "Leonti", "Andrew"]

numbers = {num: name for num, name in zip(employee_numbers, employee_names)}
names = [name[0]*num for num, name in zip(employee_numbers, employee_names)]
print(numbers)
print(names)

# Транспонирование матрицы
# Транспонирование матрицы - это процесс изменения ориентации матрицы путем перестановки строк и столбцов так ,
# что строки становятся столбцами, а столбцы — строками.
#
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

matrix_trans = [list(i) for i in zip(*matrix)]

print(matrix_trans)
# [[1, 5], [2, 6], [3, 7], [4, 8]]
# В этом примере из матрицы размером 2х4 получили матрицу размером 4х2. Элементы, которые располагались в первой строке,
# стали располагаться в первом столбце, вторая строка - во втором столбце.


# # ЗАДАЧИ

# Перед вами два списка одинаковой длины keys и values
#
# Ваша задача — создать словарь, в котором пара ключ-значение берется из значений списков, стоящих на одинаковых индексах.
# В качестве ответа выведите полученный словарь

keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'One hundred']
values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

dict_keys_values ={k: v for k, v in zip(keys, values)}
print(dict_keys_values)
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50, 'Sixty': 60, 'Seventy': 70, 'Eighty': 80,
# 'Ninety': 90, 'One hundred': 100}




# За все время обучения студенты сдают массу экзаменов и получают за них оценки. Университет решил собрать информацию
# о лучшей оценке у каждого студента. Ваша задача написать программу, которая проанализирует результаты всех экзаменов
# и найдет для каждого студента лучший балл
#
# Напишите функцию get_info_marks, которая имеет следующие параметры:
#
#     —  students содержит имена студентов в виде списка (можете переименовать параметр по своему усмотрению). Это
# обязательный параметр;
#
#     —  marks - произвольное количество списков, в которых содержатся оценки (можете переименовать параметр по своему
# усмотрению).
#
# Функция get_info_marks должна найти лучшую оценку для каждого студента и составить из этих данных словарь, где ключ -
# имя студента, значение - лучшая оценка.
#
# Что касается оценок, это представляет собой несколько списков из целых чисел. Каждый список содержит оценки для
# студентов за один конкретный экзамен. По месту оценки в списке определяется, к какому студенту она относится.

def get_info_marks(students: list[str], *marks: list[int]) -> dict[str, int]:
    """ найти лучшую оценку для каждого студента и составить из этих данных словарь """
     # Мы используем zip для объединения студентов и их оценок по всем предметам
    rez = zip(students, zip(*marks))
     # Для каждого студента выбираем максимальную оценку
    return {student: max(mark) for student, mark in rez}

math = [90, 76, 94]
history = [78, 79, 90]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, history))


# Усовершенствуйте функцию get_info_marks из предыдущего урока так, чтобы она возвращала словарь, в котором для
# каждого студента формируется словарь, хранящий информацию как о лучшей оценке студента(ключ «best»), так и худшей
# (ключ «worst»)
#
# Параметры функции остаются неизменными.

def get_info_marks(students: list[str], *marks: list[int]) -> dict:
    """ найти лучшую и худшую оценку для каждого студента и составить из этих данных словарь в словаре """
    # Мы используем zip для объединения их оценок по всем предметам
    rez = list(zip(*marks))
    # Для каждого студента создаем словарь в словаре с наилучшей и наихудшей оценкой
    dict_marks = {}
    for i in range(len(students)):
        dict_marks[students[i]] = {'best': max(rez[i]), 'worst': min(rez[i])}
    return dict_marks


math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
music = [93, 98, 100]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history, music))

