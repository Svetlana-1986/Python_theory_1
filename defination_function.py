# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность
# и печатает на экран результат проверки.
#
# Сложным паролем будет считаться комбинация символов, в которой :
#
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password",
# в противном случае - "Easy peasy"
#
# Вам необходимо написать только определение функции check_password

def check_password(password):
    digit = 0
    up_letter = 0
    symbol = 0

    symbols = "!@#$%*"

    for i in password:
        if i.isdigit():
            digit += 1

    for i in password:
        if i.isalpha() and i.isupper():
            up_letter += 1

    for i in password:
        if i in symbols:
            symbol += 1

    if len(password) >= 10 and digit >= 3 and up_letter >= 1 and symbol >= 1:
        print("Perfect password")
    else:
        print("Easy peasy")


# Напишите функцию get_body_mass_index, которая принимает массу тела человека в кг и рост в см и рассчитывает индекс
# массы тела человека по формуле index= weight/height**2
# Рост указывается в формуле в метрах, а не в сантиметрах
#
# Функция и должна вывести на экран информацию о массе человека, отталкиваясь от найденного
# индекса:
#
# если индекс < 18.5 программа должна вывести Недостаточная масса тела
# если 18.5 <= индекс <= 25 программа должна вывести Норма
# если индекс > 25 программа должна вывести Избыточная масса тела
# Вам необходимо написать только определение функции get_body_mass_index.

def get_body_mass_index(weight, height):
    index = weight/((height/100)**2) # переводим рост в метры из см
    if index < 18.5:
        print("Недостаточная масса тела")
    elif index <= 25 and index >=18.5:
        print("Норма")
    else:
        print("Избыточная масса тела")

# Считаем буквы
# Напишите функцию count_letter(text, letter), которая принимает два параметра:
#
# text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая
# регистр буквы;
# letter – буква, количество которой мы должны посчитать в text.
# Функция count_letter должна выводить на экран найденное количество букв  letter в тексте text
#
# Ваша задача дописать только тело функции count_letter

# объявление функции
def count_letter(text, letter):
    count_let = text.count(letter)
    print(count_let)
    pass

# считываем данные
text = input()
symbol = input()
# вызываем функцию
count_letter(text, symbol)

# Инициалы
# Напишите функцию print_initials(name, surname, middlename), которая принимает три параметра:
#
# name – имя человека;
# surname – фамилия человека;
# middlename– отчество человека;
# а затем выводит на печать фамилию и инициалы в определенном формате
# (первая буква фамилии должна стать заглавной, все остальные строчные; в имени и отчестве
# остаются только по одной букве в верхнем регистре).
#
# Ваша задача дописать только тело функции print_initials

# объявление функции
def print_initials(name, surname, middlename):
    print(f"{surname.title()} {name[0].upper()}.{middlename[0].upper()}.")
    pass

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)

# Напишите функцию first_unique_char, которая принимает строку символов и возвращает
# целое число: позицию первого уникального символа в строке. В случае, если уникальных
# символов в переданной строке нет, верните -1. Регистр символов не учитывайте.
#
# Ваша задача написать только определение функции first_unique_char

def first_unique_char(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1


s = input()
print(first_unique_char(s))

# Fizz Buzz  список
# Напишите функцию generate_fizz_buzz_list, которая принимает одно целое число n - размер списка.
# Функция generate_fizz_buzz_list должна
#
# обойти числа от 1 до n включительно и для каждого такого числа выполнить последовательно
# проверки с пункта 2 по пункт 5
# Если число кратно и трем, и пяти, то в список заносим строку FizzBuzz
# Если число кратно трем, то в список заносим строку Fizz
# Если число кратно пяти, то в список заносим строку Buzz
# Если число не кратно ни трем ни пяти, то в список заносим само это число
# В итоге функция generate_fizz_buzz_list должна вернуть сформированный список из n элементов.
# Ниже показаны примеры вызова:
#
# generate_fizz_buzz_list(3)  => [1, 2, 'Fizz']
# generate_fizz_buzz_list(7)  => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7]
# generate_fizz_buzz_list(15) => [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
# Ваша задача написать только определение функции generate_fizz_buzz_list

def generate_fizz_buzz_list(n):
    mas = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            mas.append("FizzBuzz")
        elif i % 3 == 0:
            mas.append("Fizz")
        elif i % 5 == 0:
            mas.append("Buzz")
        else:
            mas.append(int(i))
    return mas

# Напишите функцию factorial, которая принимает на вход одно неотрицательное число, и возвращает
# значение факториала данного числа.
#
# Нужно написать только определение функции factorial
#
# factorial(3) => 6
# factorial(1) => 1
# factorial(0) => 1
# factorial(5) => 120

# знак => обозначает return

def factorial(n):
    digit = 1
    for i in range(2, n+1):
        digit = digit*i
    return digit

n=int(input())
print(factorial(n))


# Ваша задача написать функцию format_name_list, которая принимает список словарей,
# у каждого словаря в этом списке есть только ключ name.
#
# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются
# запятой кроме последних двух имен, они должны быть разделены союзом "и". Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:
#
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) =>
# 'Bart, Lisa и Maggie'
#
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'
#
# format_name_list([{'name': 'Bart'}]) => 'Bart'
#
# format_name_list([]) => ''
# Ваша задача написать только определение функции format_name_list

def format_name_list(names):
    n = []
    for i in range(len(names)):
        n.append(names[i]["name"])

    if len(n) == 0:
        return ''
    if len(n) == 1:
        return n[0]
    if len(n) == 2:
        return f"{n[0]} и {n[1]}"
    if len(n) >= 3:
        return ', '.join(n[:-2]) + ', ' + n[-2] + ' и ' + n[-1]


# код ниже не стоит удалять, он нужен для проверки
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'},
                         {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'

assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'

assert format_name_list([{'name': 'Bart'}]) == 'Bart'

assert format_name_list([]) == ''

assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'},
                         {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'

assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'

assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'

print('Проверки пройдены')

# Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает
# из нее доменное имя и возвращает его в качестве строки
#
# get_domain_name("http://google.com") => "google"
# get_domain_name("http://google.co.jp") => "google"
# get_domain_name("www.xakep.ru") => "xakep"
# get_domain_name("https://youtube.com") => "youtube"
# get_domain_name("https://www.asos.com") => "asos"
# get_domain_name("http://www.lenovo.com") => "lenovo"
# Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://  https://, могут также содержать www.
#
# Ваша задача написать только определение функции get_domain_name


def get_domain_name(url):
    protocols = ["http://", "https://", "www.", "http://www.", "https://www."]
    for i in protocols:
        if url.startswith(i):
            url = url.replace(i, '', 1)

    finish_domen = []
    for s in url:
        if s != '.':
            finish_domen.append(s)
        else:
            break
    return ''.join(finish_domen)


# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") == 'github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')

# Сколько нулей на конце факториала N!
# В этой задаче вам необходимо воспользоваться уже готовой функцией factorial, которая
# принимает неотрицательное число, и возвращает значение факториала данного числа.
#
# Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное число,
# находит его факториал и возвращает сколько нулей на конце этого факториала .
#
# trailing_zeros(6) =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# trailing_zeros(10) => 2, потому что 10! = 3 628 800
# trailing_zeros(20) => 4, потому что 20! = 2 432 902 008 176 640 000
#
# Нужно написать только определение функций trailing_zeros и factorial

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def trailing_zeros(n):
    m = factorial(n)
    if m == 0:  # проверка, если factorial(n) = 0, т.е. одно число
        return 0

    count = 0
    for i in str(m)[::-1]:  # переворачиваем число, т.к. нам нужно посчитать 0 только в конце
        if int(i) == 0:
            count += 1
        else:
            break
    return count


# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2
print('Проверки пройдены')

# Снова НОД
# В этой задаче вам необходимо воспользоваться уже готовой функцией gcd(a, b), которая принимает
# два числа и находит наибольший общий делитель для них.
#
# Ваша задача при помощи функции gcd определить НОД произвольного количества чисел.
#
# Входные данные
# На первой строке вводится натуральное число n – количество чисел. Далее идут n строк,
# в каждой из которых натуральное число.
#
# Выходные данные
# НОД введенных чисел.

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

nod = []
for i in range(len(s)-1):
    fin = gcd(s[i], s[i+1])
    nod.append(fin)

finisn_nod = []
for i in range(len(nod)-1):
    fin_nod = gcd(nod[i], nod[i+1])
    finisn_nod.append(fin_nod)
print(max(finisn_nod))

#  шифр Цезаря
# Напишите функцию shift_letter , которая принимает два аргумента:
#
# letter одна английская буква в нижнем регистре
# shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
# Функция shift_letter  сдвигает символ letter вперед или назад на заданное значение shift .
# Сдвиг может быть цикличным в пределах от a до z. Ниже примеры:
#
# shift_letter('b', 2)=> 'd'
# shift_letter('d', 1) => 'e'
# shift_letter('z', 1) => 'a'
# shift_letter('d', -2) => 'b'
# shift_letter('d', 26) => 'd'
# shift_letter('b', -3) => 'y'
# Не забудьте проаннотировать аргументы и также добавьте doc-строку «Функция сдвигает
# символ letter на shift позиций»
#
# Функция shift_letter  должна вернуть новый символ. Вот вам в помощь ascii коды
# английских буквы, вам нужны только символы в нижнем регистре

def shift_letter(letter: str, shift: int) -> str:
    """Функция сдвигает символ letter на shift позиций"""

    num = chr((ord(letter) - ord('a') + shift) % 26 + 97) # шифр Цезаря (26 букв в англ алфавитеб 97 это щкв буквы а
    # берем остаток от деления на 26б чтобы понять ск раз по 26 пройдет круг буква и этот остаток прибавляем к 97, т.к.
    # так как алфавит начинается с а, а ord("a") = 97
    return num

letter = input()
shift = int(input())
print(shift_letter(letter, shift))


# Ваша задача создать функцию create_matrix, которая принимает
#
# необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает
# значение 3;
# необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше
# главной диагонали. По умолчанию равен 0;
# необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже
# главной диагонали. По умолчанию равен 0;
# Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали
# которой располагаются числа от 1 до size. Все остальные элементы заполнены согласно параметрам
# up_fill и down_fill.

def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    """Функция create_matrix должна возвращать квадратную матрицу размером size х size,
    на диагонали которой располагаются числа от 1 до size. Все остальные элементы заполнены
    согласно параметрам up_fill и down_fill."""
    a = []
    for i in range(size):  # заполняем матрицу 0
        a.append([0] * size)

    for i in range(size):
        for j in range(size):
            if i == j:  # диагональ (индексы равны)
                a[i][j] = i + 1
            elif i > j:  # ниже диагонали
                a[i][j] = down_fill
            else:
                a[i][j] = up_fill  # выше диагонали
    return a

# print(create_matrix(size = 3, up_fill = 7, down_fill = 9))

# # Давайте теперь создадим функцию print_goods, которая печатает список покупок.
# На вход она будет принимать произвольное количество значений, а товаром мы будем считать
# любые непустые строки. То есть числа, списки, словари и другие нестроковые объекты вам нужно
# будет проигнорировать. Функция print_goods должна печатать список товаров в виде:
# <Порядковый номер товара>. <Название товара> (см. пример ниже).
# В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать
# текст "Нет товаров"

def print_goods(*args):
    """должна печатать список товаров в виде: <Порядковый номер товара>. <Название товара> (см. пример ниже). В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать текст "Нет товаров"""
    s = [] #можно сделать через счетчик вместо списка c = 1
    for i in args:
        if isinstance(i, str) == True and len(i) > 0:
            s.append(i)
        else:
            pass
    if len(s) == 0:
        print("Нет товаров")
    else:
        for i, v in enumerate(s, start=1):
            print(f"{i}. {v}")


# Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
# Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде
# пары <Ключ> = <Значения>,
# причем ключи должны следовать в алфавитном порядке. Пример работы смотрите ниже

def info_kwargs(**kwargs):
    """Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде пары
    <Ключ> = <Значения>, причем ключи должны следовать в алфавитном порядке.
    Пример работы смотрите ниже"""
    for k, v in sorted(kwargs.items()):
        print(f"{k} = {v}")

#Условные операторы внутри функции if, for, while:
def get_numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        numbers.append(i)
        i = i + 1
    print(numbers)

    #Давайте попробуем сохранить результат вызова данной функции
    # в переменную и узнаем, что она возвращает
    def print_square(number):
        print(f'Квадрат числа {number} равен {number ** 2}')

    result = print_square(9)
    print(f'Возвращаемое значение = {result}')


#Внутри get_square мы сперва находим квадрат, затем возвращаем полученный результат.
# При этом функция get_square
# теперь ничего не выводит на экран, она только высчитывает и возвращает квадрат числа
def get_square(number):
    square = number ** 2
    return square


result = get_square(9)
print(f'Возвращаемое значение = {result}')



