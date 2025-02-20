# Функция map
# Функция map имеет следующие параметры
#
#    ➖  объект функции func;
#
#    ➖  произвольное количество итерируемых объектов iterables. Как правило, с функцией map будут применять только
# один итерируемый объект, поэтому большинство примеров будет про эту ситуацию. Несколько шагов данного урока будут
# посвящены примерам использования map с несколькими итерируемыми объектами.
#
# Функция map возвращает итератор map object, который будет выдавать следующие элементы: он будет поочередно брать по
# одному элементу из iterables и применять к нему функцию func.

# Результатом работы map(abs, a), будет являться итератор map object, к которому можно применять функцию next для
# получения элементов. Map поочередно берет элементы из списка a и применяет к ним функцию abs.
a = [-1, 2, -3, 4, -5]
result = map(abs, a)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Когда вы передаете имя функции в map, не нужно указывать оператор вызова (). Иначе это приведет к ошибке.
# Сама функция map будет вызывать вашу функцию и передавать в нее аргументы.

a = [-1, 2, -3, 4, -5]
b = list(map(abs, a))
print(b)

# через list_comprehension
b = [abs(i) for i in a]

# Итератор map object можно обойти только один раз
def get_square(value: int) -> int:
    return value ** 2

#1
my_list = [32, 43, 2, 90, 2]
new_list = list(map(get_square, my_list))
print(new_list)

str_nums = ['-1', '4232', '-33', '312', '12']
nums = list(map(int, str_nums))
print(nums)


#2
a = ['hello', 'hi', 'good morning']
b = list(map(len, a))
print(b)

def get_square_and_cube(num: int) -> tuple[int, int]:
    return num ** 2, num ** 3


a = [-1, 2, -3, 4, -5]
b = list(map(get_square_and_cube, a))
print(b)

#3
a = ['hello', 'hi', 'good morning']
b = list(map(str.upper, a))
print(b)

#4
list_strings = ['hello', 'hi', 'good morning']
b = list(map(lambda x: x+'!', list_strings))
print(b)

# Примеры
# Перед вами имеется список кортежей names. Каждый кортеж состоит из двух элементов: имени и фамилии. Ваша задача на
# основании списка names создать новый список new_names, где каждый кортеж должен замениться на строку конкатенации
# имени и фамилии, между которыми стоит пробел . Вот пример на других данных:

names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
         ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
         ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
         ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
         ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
         ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
         ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
         ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
         ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
         ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
         ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
         ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
         ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
         ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
         ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]

new_names = list(map(lambda x: f"{x[0]} {x[1]}", names))
print(new_names)

# Пример
# В базовом курсе по python есть задача RGB , в которой необходимо по трем целым числам получить цвет в формате RGB.
# Сейчас вам предстоит выполнить обратное преобразование
#
# Ваша задача создать функцию from_hex_to_rgb, которая принимает на вход строку - закодированный код цвета в формате
# RGB и возвращает кортеж из трех значений (оттенок_красного, оттенок_зеленого, оттенок_синего).
# Как только функция будет готова, ее необходимо использовать внутри функции convert_to_rgb, которая принимает список
# строк, содержащих информацию о цветах в формате RGB. Функция convert_to_rgb должна расшифровать каждый цвет и вернуть
# список кортежей.

def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    # Убираем символ '#' в начале строки, если он есть
    color = color.lstrip('#')

    # Преобразуем каждую пару символов в целое число по системе счисления 16 (HEX)
    r = int(color[0:2], 16)  # Красный компонент
    g = int(color[2:4], 16)  # Зеленый компонент
    b = int(color[4:6], 16)  # Синий компонент

    # Возвращаем кортеж с компонентами RGB
    return (r, g, b)


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    # Для каждого цвета из списка вызываем from_hex_to_rgb и собираем результаты в новый список
    return list(map(from_hex_to_rgb, values))
    # return [from_hex_to_rgb(color) for color in colors_list]

colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50']
print(convert_to_rgb(colors))

print(from_hex_to_rgb('#B22222'))
print(from_hex_to_rgb('#FFFFFF'))
print(from_hex_to_rgb('#000000'))
print(from_hex_to_rgb('#87CEEB'))
print(from_hex_to_rgb('#191970'))

# Функция map и несколько последовательностей
# функция map может принимать произвольное количество итерируемых объектов. В таком случае будут браться по порядку
# элементы, стоящие на одинаковых местах из всех коллекций, и по очереди передаваться на вход функции func.
# Количество параметров функции func должно обязательно совпадать с количеством итерируемых объектов.

def power(base: int, exp: int) -> int:
    return base ** exp


bases = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exponents = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(power, bases, exponents)) # возведение в степень числе из первого списка в степень из чисел второго
print(result)

# Логика получения итогового результата следующая: берется первое значение списка bases и первое значение списка
# exponents, передается функции power, получается результат. То же самое делается потом со вторыми, третьими и
# остальными элементами списков.
#
# Если в одном из списков будет меньше значений, то вычисления будут производиться только для тех элементов,
# у которых есть соответствующие пары.

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
print(list(result))
# [12, 15, 18]

# Имеются три списка из 50 элементов: list_x, list_y и list_w
#
# Ваша задача — произвести научные расчеты для соответствующих значений этих списков. Нужно подставить в формулу
# поочередно первые значения из списков list_x, list_y и list_w, потом вторые, затем третьи и т.д.  Значения из списка
# list_x должны подставляться в переменную x, из списка list_y - в переменную y и из списка list_w - в переменную w.
#
# Всего должно получиться 50 вычисленных значений. Их необходимо сложить в список и вывести на экран.

list_x = [25, 48, 23, 13, -18, -10, -3, 16, 2, -12, 20, -14, 14, 45, 41, 6, 11, 15, 22,
          -14, -11, 41, 15, 48, 47, 41, -8, 1, 4, 1, 40, 27, -11, -2, -14, -15, 35, 4,
          49, 4, 5, 13, 50, 35, -3, 3, 30, -11, 7, 12]

list_y = [-9, 17, 41, 47, -5, -10, -5, 13, 31, -11, 37, 9, 46, 27, -1, 36, 32, 23, -12,
          38, 8, 9, 17, 16, 29, -4, 4, 2, 1, 46, 6, 49, -16, 21, -19, -10, 15, -13, 20,
          13, -18, 21, -17, 21, 10, 5, 38, -1, 18, 22]

list_w = [9, -26, 3, 21, 48, -14, 43, -4, -16, 16, 41, 43, -27, -9, 10, -10, 4, -2, 1,
          7, 30, -29, 11, 17, 31, 31, -26, 38, 38, -17, 35, 17, 35, 10, -25, 42, -30,
          -10, -20, 20, 15, 0, 29, -30, -21, -13, -27, -21, -18, -26]

rezult = list(map(lambda x, y, w: x ** 2 - x * y * w + w ** 4, list_x, list_y, list_w))
print(rezult)



