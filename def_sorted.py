# Параметры функции sorted
# Сигнатура функции sorted выглядит следующим образом
# sorted(iterable, key=None, reverse=False)
# Функция sorted имеет следующие параметры:
# обязательный параметр iterable - итерируемый объект,
# необязательный параметр reverse. Если передать в него значение True, отсортированный список переворачивается
# (или сортируется в порядке убывания). По умолчанию принимает False
# необязательный параметр key. В данный параметр можно передать функцию, которая будет служить ключом для сравнения
# элементов во время сортировки. По умолчанию — None.

# Результаты экзаменов
# Напишите функцию print_results, которая принимает список кортежей. Каждый элемент вложенного кортежа состоит из
# названия предмета и оценки по нему.
#
# Функция print_results должна вывести информацию по экзаменам, отсортированную по возрастанию оценок. Название
# каждой пары предмета и оценки печатается на отдельной строке через пробел.
#
# В случае равенства оценок предметы должны выводиться на экран в том же порядке, в котором они следовали во входном
# списке

def print_results(marks):
    sort_marks = sorted(marks, key = lambda s: s[1])
    for i in range(len(sort_marks)):
        print(f"{sort_marks[i][0]} {sort_marks[i][1]}")

marks = [('English', 88), ('Science', 100), ('Maths', 81),
         ('Physics', 100), ('History', 82), ('Music', 100)]
print_results(marks)

# Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок, а в случае их равенства предметы
# должны выводиться в алфавитном порядке без учета регистра

def print_results(marks: list[tuple[str, int]]):
    sort_marks = sorted(marks, key = lambda s:(- s[1], s[0].lower()))
    for i in range(len(sort_marks)):
        print(f"{sort_marks[i][0]} {sort_marks[i][1]}")

marks = [('English', 88), ('Science', 90), ('Maths', 88),
         ('Physics', 93), ('History', 78), ('French', 78),
         ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
print_results(marks)

# Перепишите функцию print_results так, чтобы информация выводилась по убыванию оценок, а в случае их равенства предметы
# должны выводиться в обратном алфавитном порядке без учета регистра

def print_results(marks: list[tuple[str, int]]):
    sort_marks = sorted(marks, key =lambda s: s[0].lower(), reverse = True)
    sort_marks_new = sorted(sort_marks, key = lambda s: s[1], reverse = True)
    for i in range(len(sort_marks_new)):
        print(f"{sort_marks_new[i][0]} {sort_marks_new[i][1]}")

marks = [('English', 88), ('Science', 90), ('Maths', 88),
         ('Physics', 93), ('History', 78), ('French', 78),
         ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
print_results(marks)

# Сортировка отрезков
# Напишите функцию get_sort_lines, которая принимает список кортежей, в котором хранится информация о координатах двух
# точек на координатной прямой. Функция get_sort_lines должна вернуть новый список, в котором элементы расположены
# в порядке возрастания расстояния между точками, хранящимися в одном элементе.

# В случае равенства расстояний необходимо сортировать по возрастанию значения координаты первой точки, затем
# по возрастанию значения второй точки

def get_sort_lines(lines: list[tuple[int,int]]) -> list[tuple[int,int]]:
    lines_one = sorted(lines, key = lambda x: ((abs(x[0] - x[1]), x[0], x[1])))
    return lines_one

lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
print(get_sort_lines(lines))