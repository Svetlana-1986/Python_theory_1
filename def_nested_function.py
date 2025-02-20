# Внутренняя функция (Inner function), также известная как вложенная (nested function), — это функция, которая определена
# внутри другой функций.

def print_colors() -> None:
    def print_red() -> None:
        print('red')

    def print_blue() -> None:
        print('blue')

    print_red()
    print_blue()


print_colors()

# Мы имеем функцию print_colors, внутри которой определены две вложенные функции print_red и print_blue. После определения
# внутренних функций, мы можем начинать ими пользоваться. В примере выше мы вызвали сперва print_red, затем print_blue.

# Функции print_red и print_blue находятся внутри функции print_colors, а значит являются вложенными. Это также
# означает, что они будут находиться внутри локальной области видимости функции print_colors и за пределами области
# видимости print_colors эти функции будут не доступны. Вызвать их не получится, но если вы попытаетесь, произойдет ошибка
#
# NameError: name 'print_red' is not defined

# Доступ к переменным внешней функции
# У вложенных функций есть потрясающее качество: они имеют прямой доступ к переменным, определенным во внешней
# функции.

# Поэтому вы можете создать новую переменную y в функции print_colors и она будет доступна сразу в трех областях:
# в самой print_colors, во внутренних функциях  print_red и print_blue:

def print_colors():
    y = 'yellow'

    def print_red() -> None:
        r = 'red'
        print(r, y)

    def print_blue() -> None:
        b = 'blue'
        print(b, y)

    print_red()
    print_blue()

print_colors()

# Можно также создать глобальную переменную, вне функции print_colors, и эту переменную мы также сможем использовать
# внутри наших вложенных функций:

g = 'grey'

def print_colors() -> None:
    y = 'yellow'

    def print_red() -> None:
        r = 'red'
        print(r, y, g)

    def print_blue() -> None:
        b = 'blue'
        print(b, y, g)

    print_red()
    print_blue()

print_colors()

# На примере функции print_red рассмотрим, как происходит поиск имени переменной g:
#
# внутри данной функции переменной g нет, поэтому поднимаемся на уровень выше к функции print_colors.
# Внутри области видимости функции print_colors также нету переменной g, поэтому поднимаемся на ещё один уровень выше
# в глобальной области видимости мы находим эту переменную и используем её значение.
# Теперь рассмотрим пример, где помимо глобальной переменной g = 'grey' мы добавим внутри функции print_colors
# локальную g = 'green':.

g = 'grey' # глобальная переменная

def print_colors() -> None:
    y = 'yellow'
    g = 'green' # локальная переменная

    def print_red() -> None:
        r = 'red'
        print(r, y, g) # для g возмется значение из локальной переменной

    def print_blue() -> None:
        b = 'blue'
        print(b, y, g) # для g возмется значение из локальной переменной

    print_red()
    print_blue()

print_colors()

# По правилу LEGB приоритет в поиске имени отдаётся локальной области, но в нашем случае g не нашлась
# в print_red, поэтому поиск поднялся на уровень выше – в функцию print_colors и здесь была найдена такая
# переменная и взялось это значение, в то время, как значение глобальной переменной g было проигнорировано.
#
# Также есть возможность изменить переменную при помощи nonlocal:

g = 'grey'

def print_colors() -> None:
    y = 'yellow'
    g = 'green'

    def print_red() -> None:
        nonlocal y
        r = 'red'
        print(r, y, g)
        y = 'Not yellow anymore'

    def print_blue() -> None:
        b = 'blue'
        print(b, y, g)

    print_red()
    print_blue()

print_colors()

# В print_red мы вывели переменную y, а при помощи nonlocal мы изменили дальнейшее её значение, что мы и видим
# по результату вывода print_blue.

# Доступ к параметрам внешней функции

# Вложенные функции также имеют прямой доступ к параметрам внешней функции.

# Параметры внешней функции являются ее локальными переменными, а значит внутренние функции имеют к ним доступ.
# Вот взгляните на пример

def greeting(firstname, lastname):
    def concatenate():
        return f'{firstname} {lastname}'

    print("Добрый день, " + concatenate() + "!")


greeting('Олег', 'Барсук')

# В следующем примере мы в зависимости от значения параметра param , поступающего внутрь функции, вызываем либо одну
# внутреннюю функцию, либо другую. По умолчанию сделаем значение param равное r, что будет отвечать за вызов функции,
# печатающей красный цвет.

def print_colors(param = 'r') -> None:

    def print_red() -> None:
        r = 'red'
        print(r)

    def print_blue() -> None:
        b = 'blue'
        print(b)

    if param == 'r':
        print_red()
    elif param == 'b':
        print_blue()
    else:
        print('I do not know this color')

print_colors()
print_colors('b')
print_colors('y')

# Если вызвать функцию print_colors без аргументов, то параметр param  примет значение по умолчанию «r» и будет вызвана
# внутренняя функция print_red, которая распечатает текст «red» . Если вызвать print_colors('b'), то получим текст «blue»,
# так как сработает внутренняя функция print_blue. При остальных значениях параметра param, к примеру print_colors('y'),
# получим сообщение  «I do not know this color».
#
# ЗАДАЧИ
# Имеется функция wrap_increment, которая должна принимать значение и увеличивать его на 1. Увеличение на один должно
# выполняться за счет вложенной функции _inc.
#
# Ваша задача дописать в теле wrap_increment определение функции _inc, которая принимает значение и увеличивает
# его.

def wrap_increment(value):
    # определите вложенную функцию _inc
    def _inc(value):
        return value + 1

    return _inc(value)

print(wrap_increment(41))

# Перед вами вполне работающая функция get_extensions, которая принимает список названий файлов.
# Функция get_extensions находит расширение у названий файлов и составляет из них список, который возвращает
# в качестве ответа. Если у файла нет расширения, то для такого файла get_extensions подставляет пустую строку.
#
# Ваша задача — произвести рефакторинг данного кода для создания внутренней вспомогательной функции, которая
# выполняет всю работу по поиску расширения. Вы можете, к примеру, назвать ее _get_extension и тогда, определив
# такую функцию, ей можно пользоваться следующим образом:
#
# for i in file_list:
#     results.append(_get_extension(i))
# или даже сразу так
#
# return [_get_extension(i) for i in file_list]
# Перепишите функцию get_extensions с учетом описанных пожеланий по созданию внутренней функции.

def get_extensions(file_list):
    results = []

    def _get_extension(i):
        if "." in i:
            return i.split(".")[-1]
        else:
            return ""

    for i in file_list:
        results.append(_get_extension(i))

    return results

print(get_extensions(["foo.txt", "bar.mp4", "python3"]))

# Перед вами частично реализованная функция double_odd_numbers, которая принимает список чисел и возвращает в качестве
# результата новый список, составленный из нечетных чисел, увеличенных в два раза.
#
# Внутри себя double_odd_numbers использует две функции:
# double, увеличивающая число в два раза;
# is_odd, проверяющая на нечетность
#
# Ваша задача реализовать эти функции внутри  double_odd_numbers

def double_odd_numbers(numbers):
    def is_odd(num):
        if num % 2 != 0:
            return num

    def double(num):
        return num * 2

    return [double(num) for num in numbers if is_odd(num)]

print(double_odd_numbers([1, 2, 3, 4, 5]))
