# Рекурсия и вложенные объекты
# Представьте, у вас есть функция get_total

def get_total(lst: list[int]) -> int:
    total = 0
    for value in lst:
        total += value
    return total
# которая отлично умеет находить сумму элементов списка. Но данная функция умеет работать только с линейным списком,
# это такой список, в котором отсутствует вложенность. Примером линейного списка является значение [1, 2, 3, 4, 5]
# Если же передать двумерный список (список вложенность, которого равна двум) в функцию get_total,
# то при текущей реализации мы получим ошибку

# Нам придется переписывать реализацию функции get_total так, чтобы она могла работать с двумерными списками. Например так:
def get_total(lst: list[int]) -> int:
    total = 0
    for row in lst:
        for value in row:
            total += value
    return total

print(get_total([[1, 2, 3], [4, 5], [6, 7, 8]]))

# Функция отлично справится с двумерным списком, но перестанет суммировать линейные. Как нам быть в такой ситуации?
# Код, отражающий базовый случай и рекурсивный шаг, будет выглядеть так
def get_total(lst):
    total = 0
    for value in lst:
        # проверяем тип элемента
        if isinstance(value, list):
            # если это список, то
            # вызываем рекурсивный шаг для
            # нахождения суммы его элементов
            sum_nested = get_total(value)
            total += sum_nested
        else:
            # Если это число, то сразу добавляем к total
            total += value

    return total

print(get_total([1, 2, 3, 4, 5]))
print(get_total([[1, 2, 3], [4, [5, 6]], 7]))
print(get_total([1, 2, 3, 4, 5,
                 [6, 7, 8,
                  [9, 1, [2, [3], 4], 5, 6]]]))

# ЗАДАЧИ
# 1. Сумма списка

# Напишите функцию sum_recursive, которая принимает на вход вложенный список, конечными элементами которого являются
# целые числа, и возвращает сумму элементов переданного списка. Уровень вложенности списка произвольный.
#
# Ваша задача только написать определение рекурсивной функции sum_recursive

def sum_recursive(lst: list[int]) ->int:
    total = 0
    for value in lst:
        if isinstance(value, list): # Если элемент — список
            get_sum = sum_recursive(value) # Рекурсивный вызов
            total += get_sum
        else:
            total += value # Если элемент — число
    return total

print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# 36

# 2. Произведение элементов списка
# Напишите функцию multu_recursive, которая принимает на вход вложенный список, конечными элементами которого являются
# целые числа  и строки, и возвращает произведение числовых элементов переданного списка. Уровень вложенности исходного
# списка произвольный.
#
# Произведение пустого списка должно быть равно 1. Также единице должно быть равно произведение списка, в котором нету
# ни одного числового значения.
#
# Ваша задача только написать определение рекурсивной функции multu_recursive

from typing import Union, List


def multu_recursive(lst: List[Union[int, str, list]]) -> int:
    total = 1

    # Если список пустой, возвращаем 1
    if len(lst) == 0:
        return 1

    # Если весь список состоит из строк, возвращаем 1
    if all(isinstance(item, str) for item in lst):
        return 1

    for value in lst:
        if isinstance(value, list):  # Если элемент — вложенный список
            total *= multu_recursive(value)  # Рекурсивно умножаем результат
        elif isinstance(value, int):  # Если элемент — число
            total *= value
        elif isinstance(value, str):  # Если элемент — строка
            continue  # Игнорируем строки

    return total

print(multu_recursive([1, 2, 3, 4, [[5]], [5]]))
# 600

# 3.Нахождение самого большого элемента списка
# Напишите функцию get_max_recursive, которая принимает на вход вложенный список, конечными элементами которого
# являются целые числа, и возвращает самый большой элемент переданного списка. Уровень вложенности исходного списка
# произвольный.
#
# Ваша задача только написать определение рекурсивной функции get_max_recursive

def get_max_recursive(lst: list) -> int:
    max_value = float('-inf')  # Инициализация минимально возможным значением
    for value in lst:
        if isinstance(value, list):
            max_value = max(max_value, get_max_recursive(value))  # Рекурсивный вызов ((float('-inf') работает как
            # стартовое значение, которое гарантирует, что первое число (или результат рекурсии) всегда будет больше
            # этого значения. На каждом шаге рекурсии сравнивается текущее значение с максимальным найденным значением,
            # и, если текущее значение больше, оно обновляет max_value.)
        else:
            max_value = max(max_value, value)  # Сравнение с текущим максимальным (если текущее значение > обновляет max_value)
    return max_value

#def get_max_recursive(lst: int) -> int:
    #total = []
    #for value in lst:
        #if isinstance(value, list):
            #get_max = max(get_max_recursive(value))
            #total.append(get_max)
       # else:
            #total.append(value)
   # return max(total)
print(get_max_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# 8

# 4. Превращаем вложенный список в плоский
# Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из списков,
# внутри которых также могут быть списки. Задача функции flatten вернуть новый линейный список, составленный из
# элементов входного списка, в котором уже отсутствует какая-либо вложенность. Элементы в плоском списке должны
# располагаться в том же порядке, как они следовали в исходном списке.

def flatten(lst: list) -> list:
    total = []
    for value in lst:
        if isinstance(value, list):
            total.extend(flatten(value))  # Распаковываем элементы вложенного списка с помощью extend()
        else:
            total.append(value)  # Просто добавляем число
    return total

print(flatten([[[[9]]], [1, 2], [[8]]]))
# [9, 1, 2, 8]

# 5. Поиск во вложенном списке
# Ранее мы уже делали проверку на вхождение элемента в линейный список. Теперь ваша задача переписать функцию is_member
# так, чтобы она могла искать элемент в списке с произвольной вложенностью.
#
# Функция принимает некое значение value и список значений lst.
#
# Функция is_member должна вернуть True, если значение value присутствует в списке lst на любом уровне, и False в
# противном случае.

def is_member(value: int, lst: list) -> bool:
    for i in lst:
        if i == value:
            return True
        if isinstance(i, list) and is_member(value, i):
            return True
    return False

print(is_member(8, [[1, 2, 3], [4, [5, 6]], 7]))
# False

# 6.Поиск уровня
# Создайте рекурсивную функцию find_level_element, которая определяет на каком уровне вложенности располагается
# интересующий нас элемент. Нумерация уровней вложенности начинается с единицы.
#
# Функция find_level_element принимает некое значение value и список значений lst.
#
# Функция find_level_element должна вернуть номер уровня, где встречается первое найденное значение value в списке lst
# на любом уровне. Если же в lst отсутствует значение value, функция find_level_element должна вернуть -1.

def find_level_element(value: int, lst: list, level: int = 1) -> int:
    # Проходим по каждому элементу списка
    for i in lst:
        # Если элемент равен искомому, возвращаем текущий уровень
        if i == value:
            return level

        # Если элемент является вложенным списком, рекурсивно ищем в нем
        elif isinstance(i, list):
            result = find_level_element(value, i, level + 1)
            if result != -1:  # Если нашли элемент в вложенном списке, возвращаем уровень
                return result

    # Если элемент не найден на текущем уровне, возвращаем -1
    return -1

print(find_level_element(9, [1, 2, 3, 4, [[5]], [5]]))
# -1

# 7. Рекурсивный разворот списка
# Встроенная функция reversed позволяет расположить элементы упорядоченной коллекции в обратном порядке. Но работает
# данная функция только на первый уровень вложенности. Это значит, что результатом следующей инструкции
#
# print(list(reversed([[1, 2, 3], [4, 5], [6, 7, 8]])))
# будет следующий список
#
# [[6, 7, 8], [4, 5], [1, 2, 3]]
# Порядок элементов на втором уровне не поменялся.
#
# Ваша задача написать рекурсивную функцию reversed_recursive, которая принимает на вход вложенный список произвольной
# вложенности и располагает все элементы на каждом уровне в обратном направлении

def reversed_recursive(lst: list[int]) -> list[int]:
    reversed_lst = lst[::-1]
    for i in reversed_lst:
        if isinstance(i, list):
            return reversed_recursive(reversed(i))
    return reversed_lst

def reversed_recursive(lst: list) -> list:
    # Реверс текущего списка
    reversed_lst = lst[::-1]
    # Обработка вложенных списков
    for i in range(len(reversed_lst)):
        if isinstance(reversed_lst[i], list): # ecли список, то вызываем рекурсию
            reversed_lst[i] = reversed_recursive(reversed_lst[i]) # Возвращенный перевернутый список заменяет текущий элемент reversed_lst[i]
    return reversed_lst

print(reversed_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# [[8, 7, 6], [5, 4], [3, 2, 1]]


# 8. Превращаем вложенный словарь в плоский
# Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен. Ключами словаря на любом
# уровне могут быть только строки, значениями - только числа.
#
# Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский
# (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, соединенных знаком _
#
# Для этого необходимо определить рекурсивную функцию flatten_dict. Она должна принимать вложенный словарь и возвращать
# плоский

def flatten_dict(d: dict, parent_key: str = '') -> dict:
    flat_dict = {}
    for key, value in d.items():
        # Создаем полный ключ, соединяя parent_key и текущий ключ
        new_key = f"{parent_key}_{key}" if parent_key else key
        if isinstance(value, dict):
            # Если значение - словарь, вызываем рекурсию
            flat_dict.update(flatten_dict(value, new_key))
        else:
            # Если значение - число, добавляем его в итоговый словарь
            flat_dict[new_key] = value
    return flat_dict

print(flatten_dict({'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}))
# {'Q_w_E_r_T_y': 123}