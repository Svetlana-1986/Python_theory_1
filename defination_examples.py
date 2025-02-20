# Напишите функцию rotate , которая имеет следующие параметры
# lst - список чисел (целых или вещественных)
# shift - целое число, обозначающее сдвиг. По умолчанию равен 1
#
# Функция rotate должна выполнить циклический сдвиг элементов списка на shift позиций и вернуть в качестве ответа новый
# список со смещенными значениями. Если значение shift положительно, сдвиг необходимо производить вправо,
# если отрицательно — влево.

# Дополнительные условия для задания:
# Функция rotate  должна быть чистой
# необходимо проаннотировать параметры функции rotate  и ее возврат без использования модуля typing.
# Для тестов важен порядок следования типов
# добавьте док-строку с содержанием «Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0)
# или влево(shift<0)»

def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    """Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"""

    rez = []
    if shift > 0:
        start = shift % len(lst)
        for i in range(len(lst) - start, len(lst)):
            rez.append(lst[i])
        for i in range(len(lst) - start):
            rez.append(lst[i])

    if shift < 0:
        start = abs(shift) % len(lst)
        for i in range(start, len(lst)):
            rez.append(lst[i])
        for i in range(start):
            rez.append(lst[i])

    return rez

print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate([1, 2, 3, 4, 5, 6], 2))

# Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)
# {'lst': list[int | float], 'shift': <class 'int'>, 'return': list[int | float]}
# [5, 6, 1, 2, 3, 4]

#


# Рефакторинг rotate
# Перепишите функцию rotate так, чтобы она стала работать не со списками, а с кортежами.
# Для этого выполните следующие шаги:
# 1. переименовать параметр lst - в tpl. Теперь функция будет принимать не список, а кортеж целых
# или вещественных чисел
# 2.изменится тип возвращаемого значения. Вместо списка функция rotate теперь должна возвращать кортеж.
# Остальная логика программы не меняется
# 3. док строку изменить на «Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0)
# или влево (shift<0)»

def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    """Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)"""

    rez = []
    if shift > 0:
        start = shift % len(tpl)
        for i in range(len(tpl) - start, len(tpl)):
            rez.append(tpl[i])
        for i in range(len(tpl) - start):
            rez.append(tpl[i])

    if shift < 0:
        start = abs(shift) % len(tpl)
        for i in range(start, len(tpl)):
            rez.append(tpl[i])
        for i in range(start):
            rez.append(tpl[i])

    return tuple(rez)

print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate((1, 2, 3, 4, 5, 6, 7), 2))

# Сдвиг букв
# Напишите функцию rotate_letter, которая принимает два аргумента:
# 1. letter - одна английская буква в нижнем регистре
# 2. shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
# Функция rotate_letter по переданному значению сдвига shift находит новую букву относительно текущей позиции буквы
# letter в алфавите. Сдвиг может быть цикличным в пределах от a до z как в вправо (при положительном значении shift),
# так и влево (при отрицательном значении shift). Ниже представлены примеры работы функции rotate_letter:
# rotate_letter('b', 2)=> 'd'
# rotate_letter('d', 1) => 'e'
# rotate_letter('z', 1) => 'a'
# rotate_letter('d', -2) => 'b'
# rotate_letter('d', 26) => 'd'
# rotate_letter('b', -3) => 'y'
#
# Требования к функции rotate_letter:
# должна вернуть новый символ;
# параметры и возвращаемое значение должны быть проаннотированы
# добавьте doc-строку «Функция сдвигает символ letter на shift позиций»
# Для решения вам поможет таблица ascii кодов английских букв. В ней обратите внимание только на символы
# в нижнем регистре:

def rotate_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""
    if shift > 0:
        rez = ord(letter) + shift % 26
        if rez > ord('z'):
            rez_1 = rez - ord('z')
            return chr(ord('a') + rez_1 - 1)
        else:
            return chr(rez)

    if shift < 0:
        rez_a = ord(letter) - ord('a')  # ord(a) = 97 ск букв до первой буквы алфавита, разница
        rez_shift = (shift + rez_a) % 26  # опред остаток шагов, т.к. число < 0, поэтому +rez_a
        rez = rez_shift + ord('a')
        if rez > ord('z'):
            rez_1 = rez - ord('z')
            return chr(ord('a') + rez_1)
        else:
            return chr(rez)

print(rotate_letter.__doc__)
print(rotate_letter.__annotations__)
print(rotate_letter('a', 3))





