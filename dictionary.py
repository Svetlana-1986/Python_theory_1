# Создайте словарь, у которого должны быть следующие пары ключ-значения

p = [['name', 'Vasya'], ['surname', 'Petrov'], ['age', 25]]
person = dict(p)
print(person)


# Перед вами имеется словарь sweet
# В отдельных строках распечатайте сперва значение ключа name, потом calories и напоследок id

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

print(sweet["name"])
print(sweet["calories"])
print(sweet["id"])

# В вашем распоряжении имеется словарь days, в котором в качестве ключей хранится номера месяца,
# а в качестве значения - количество дней в соответствующем месяце
# (будем исключать високосные года и полагать, что в феврале всегда 28 дней)
# Ваша программа получает на вход номер месяца, гарантируется что это будет число в пределах
# от 1 до 12.
# Ваша задача по введеному номеру месяца вывести количество дней

# мое решение
days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
month = int(input())
if month > 0 and month < 13:
    print(days[month])

# Перед вами имеется словарь sweet
#
# Ваша задача:
#
# создать строковый ключ weight с целым значением 230
# создать строковый ключ have_topping c булевым значением True
# изменить значение ключа name на строку SuperCake
# изменить значение ключа calories на целое число 350
# В качестве ответа распечатайте в конце словарь sweet

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
sweet["weight"] = 230
sweet["have_topping"] = True
sweet["name"] = "SuperCake"
sweet["calories"] = 350
print(sweet)

# Перед вами имеется словарь sweet
# Удалите из него ключи ppu и type
# Затем выведите словарь sweet в качестве ответа

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
del sweet["ppu"]
del sweet["type"]
print(sweet)

# На вход программе поступает целое число n. Вам необходимо создать словарь, который будет
# # включать в себя ключи от 1 до n, а значениями соответствующего ключа будет значение ключа
# # в квадрате.
# # В качестве ответа выведите полученный словарь

digits = {}
n = int(input())

for digit in range(1, n+1):
    digits.setdefault(digit, digit**2)
print(digits)

# Напишите программу, которая печатает словарь alphabet, где ключи  - строчные английские
# символы, а значения - порядковые номера букв в алфавите начиная с 1.
#
# Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }
#
# В качестве ответа распечатайте полученный словарь alphabet
#
# Весь английский алфавит можно взять в переменной ascii_lowercase из модуля string:
#
# from string import ascii_lowercase
# print(ascii_lowercase)

from string import ascii_lowercase
alphabet = {}
n = 26

for key in range(n):
    alphabet.setdefault(ascii_lowercase[key], key + 1)
print(alphabet)

#второй вариант
from string import ascii_lowercase
alphabet = {}

for key in range(len(ascii_lowercase)):
    alphabet.setdefault(ascii_lowercase[key], key + 1)
print(alphabet)

# У нас есть словарь currencies, в котором хранятся валюты и их курсы.
# В словаре представлены далеко не все валюты.
#
# Ваша программа принимает на вход название валюты, проверяет
# присутствует ли данная валюта в словаре.

# Если валюта присутствует необходимо вывести ее курс, если отсутствует - строку
# Нет данных по <валюта>

currencies = {
    'Argentine Peso': 118362.205708,
    'Australian Dollar': 1586.232315,
    'Bahraini Dinar': 423.780164,
    'Botswana Pula': 13168.450636,
    'Brazilian Real': 5954.781483,
    'British Pound': 834.954104,
    'Bruneian Dollar': 1520.451015,
    'Bulgarian Lev': 1955.83,
    'Canadian Dollar': 1430.54405,
    'Chilean Peso': 898463.818465,
    'Chinese Yuan Renminbi': 7171.445692,
    'Colombian Peso': 4447741.922165,
    'Croatian Kuna': 7527.744707,
    'Czech Koruna': 24313.797041,
    'Danish Krone': 7440.613895,
    'Emirati Dirham': 4139.182587,
    'Hong Kong Dollar': 8786.255952,
    'Hungarian Forint': 355958.035747,
    'Icelandic Krona': 143603.932438,
    'Indian Rupee': 84241.767127,
    'Indonesian Rupiah': 16187150.010697,
    'Iranian Rial': 47534006.535121,
    'Israeli Shekel': 3569.191411,
    'Japanese Yen': 129149.364679,
    'Kazakhstani Tenge': 489292.515538,
    'Kuwaiti Dinar': 340.959682,
    'Libyan Dinar': 5196.539901,
    'Malaysian Ringgit': 4717.485104,
    'Mauritian Rupee': 49212.933037,
    'Mexican Peso': 23130.471272,
    'Nepalese Rupee': 134850.008728,
    'New Zealand Dollar': 1703.649473,
    'Norwegian Krone': 9953.078431,
    'Omani Rial': 433.360301,
    'Pakistani Rupee': 198900.635421,
    'Philippine Peso': 57574.278782,
    'Polish Zloty': 4579.273862,
    'Qatari Riyal': 4102.552652,
    'Romanian New Leu': 4946.638369,
    'Russian Ruble': 86197.012666,
    'Saudi Arabian Riyal': 4226.530892,
    'Singapore Dollar': 1520.451015,
    'South African Rand': 17159.831129,
    'South Korean Won': 1355490.097163,
    'Sri Lankan Rupee': 228245.645722,
    'Swedish Krona': 10439.125427,
    'Swiss Franc': 1037.792217,
    'Taiwan New Dollar': 31334.286611,
    'Thai Baht': 37436.518169,
    'Trinidadian Dollar': 7636.35428,
    'Turkish Lira': 15078.75981,
    'US Dollar': 1127.074905,
    'Venezuelan Bolivar': 511082584.868731
}
n = input()

print(currencies.get(n, f"Нет данных по {n}"))
