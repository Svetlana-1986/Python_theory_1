# На вход программе подается натуральное число n (n<=1000). При помощи list comprehension создайте список,
# состоящий из делителей введенного числа и выведите его на экран

n = int(input())
a = [i for i in range(1, n+1) if n % i == 0]
print(a)

# Вывести список, содержащий нечетные натуральные числа в интервале
n = int(input())
a = [i for i in range(n, (n ** 2) + 1) if i % 2 != 0]
print(a)


# Программа принимает на вход два целых числа a и b.
#
# Если a<=b необходимо сформировать список квадратов целых чисел на интервале от а до b
# включительно и вывести его на экран.
#
# Если же a>b, необходимо сформировать список кубов целых чисел на интервале от a до b
# включительно, двигаясь в порядке убывания, и затем вывести его.
#
# Не забывайте пользоваться генератором списков

# 1 вариант решения
a, b = map(int, input().split())
if a <= b:
    result = [i**2 for i in range(a, b+1)]
else:
    result = [i**3 for i in range(a, b-1, -1)]
print(result)

#2 вариант решения
a, b = map(int, input().split())
result = [i ** 2 for i in range(a, b + 1)] if a <= b else [i ** 3 for i in range(a, b - 1, -1)]
print(result)

#Создайте список первых букв каждого слова из строки st и выведите его на экран

st = 'Create a list of the first letters of every word in this string'
st = st.split() # делаем из строки список
rezult = [i[0] for i in st]
print(rezult)

#При помощи list comprehension создайте список, состоящий из первых n заглавных
# букв английского алфавита ['A', 'B', 'C', 'D', ...]. Получить все заглавные буквы английского
# алфавита можно следующим образом:

# from string import ascii_uppercase
# print(ascii_uppercase) # выведет строку ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Входные данные
# На вход программе подается натуральное число n, n≤26.
#
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита

from string import ascii_uppercase
n = int(input())
alphabet = [ascii_uppercase[i] for i in range(n)]
print(alphabet)

# Давайте усовершенствуем предыдущую задачу так, чтобы получался следующий список букв:
#
# ['A', 'BB', 'CCC', 'DDDD', 'EEEEE', 'FFFFFF', ...]
# Входные данные
# На вход программе подается натуральное число n, n ≤ 26.
#
# Формат выходных данных
# Программа должна вывести список из первых n заглавных букв английского алфавита,
# причем каждая буква должна быть продублирована в зависимости от своего порядкового номера

from string import ascii_uppercase
n = int(input())
alphabet = [ascii_uppercase[i]*(i+1) for i in range(n)]
print(alphabet)
