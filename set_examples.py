#Перед вами вновь представлено множество  my_set
# Ваша задача вновь провести удаление элементов, указанных ниже:
# noble
# offend
# error
# eagle
# sail
# Отличие этой задачи от предыдущей в том, что некоторых элементов в множестве нет.
# Не упадите с ошибкой при удалении
# Выводить ничего не нужно, только удалить элементы выше

my_set = {
    'mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',
    'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'preference',
    'fascinate', 'earthflax', 'meadow', 'bitter', 'march', 'feel', 'wind', 'location',
    'need', 'adviser', 'error', 'pneumonia', 'concert', 'value', 'value', 'disclose',
    'glasses', 'tank', 'national', 'soup', 'feel', 'few', 'concert', 'wrestle',
    'proposal', 'soup', 'sail', 'brown', 'service', 'proposal', 'winter', 'jacket',
    'mention', 'tradition', 'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal',
    'government', 'control', 'value', 'few', 'generation', 'service', 'national', 'tradition',
    'government', 'mention', 'proposal', 'sunrise', 'refund', 'formulate', 'despise', 'hobby',
    'noble', 'parameter', 'update', 'serious', 'potential', 'entry', 'week',
    'tenant', 'debut', 'dentist', 'explode', 'default', 'slam'
}

remove_set = {'noble', 'offend', 'error', 'eagle', 'sail'}
for i in remove_set:
    if i in my_set:
        my_set.discard(i)



# Вашей программе будут поступать на вход N списков, содержащих целые числа
# Ваша задача определить сколько всего встречалось различных чисел во всех этих списках
# Входные данные
# Сперва поступает натуральное число N - количество списков
# В следующих N строк вводятся значения каждого списка, разделенные через пробел
# Выходные данные
# Вывести одно число - количество различных чисел во всех этих списках

#1 вариант решения мой
n = int(input())
count = n
list_new = set()

while count > 0:
    list_my = map(int, input().split())
    list_new.update(list_my)
    count -= 1

print(len(list_new))

#2 вариант решения
b = set()
for i in range(int(input())):
    c = set(map(int, input().split()))
    b.update(c)
print(len(b))

# Ваша программа получает на вход последовательность фраз, указанных через запятую.
# Для каждой фразы выведите слово ДА (в отдельной строке), если эта фраза ранее встречалось
# в последовательности или НЕТ, если не встречалось.
# Символы во фразах нужно рассматривать без учета регистра, это значит что фраза
# Hasta la vista BAby эквивалентна фразе hasta La Vista baby

phrases = list(map(str, input().lower().split(",")))
new_phrases = set()

for phrase in phrases:
    if phrase not in new_phrases:
        print("НЕТ")
        new_phrases.add(phrase)
    else:
        print("ДА")

# Даны два списка чисел.
# Выведите все числа, которые входят как в первый,
# так и во второй список в порядке возрастания.

a = set(map(int, input().split()))
b = set(map(int, input().split()))

c = a.intersection(b)
print(*sorted(c))


# Напишите программу, которая выводит все цифры, встречающиеся в символьной строке больше
# одного раза.
#
# Входные данные
# Входная строка может содержать цифры, пробелы и латинские буквы.
#
# Выходные данные
# Программа должна вывести в одну строчку в порядке возрастания все цифры, встречающиеся
# во входной строке больше одного раза. Если таких цифр нет, нужно вывести слово 'NO'.


a = input()
s = set()

for i in a:
    if a.count(i) > 1 and i.isdigit():
        s.add(i)

if len(s) > 0:
    print(*sorted(s))
else:
    print("NO")

# print(*sorted(s) if len(s) > 0 else ["NO"])


#Напишите программу, которая удаляет из строки все повторяющиеся символы, при этом
# регистр букв необходимо учитывать.

# Входные данные
# Программа получает на вход строку, состоящую из заглавных и строчных символов, цифр и знаков
# препинания.
#
# Выходные данные
# Программа должна вывести исходную строку, из которой удалены все повторяющиеся символы.

repeat = input()
repeat_not = []

for r in repeat:
    if r not in repeat_not:
        repeat_not.append(r)

print(*repeat_not, sep = '')
