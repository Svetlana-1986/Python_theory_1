# Перед вами имеется список words
#
# Ваша задача на основании создать список кортежей words_with_position, каждый элемент-кортеж
# должен содержать два значения: само слово и его порядковый номер в списке words
#
# Порядковый номер слов необходимо считать с единицы. Вот к примеру, если бы список words был таким:
#
# words = ['variation', 'random', 'electronics', 'competence', 'collapse']
# то на выходите вы должны были получить такой ответ
#
# words_with_position = [('variation', 1),
#                        ('random', 2),
#                        ('electronics', 3),
#                        ('competence', 4),
#                        ('collapse', 5)]
# В качестве ответа необходимо вывести words_with_position

words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']

words_with_position = []

for word in enumerate(words, start=1):
    words_with_position.append(word[::-1])

print(words_with_position)


# Перед вами кортеж english_words
#
# При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите
# строку вида
#
# Word № {number} = {word}
# Например, для кортежа english_words = ('hi', 'World') ответ был бы таким:
#
# Word № 1 = hi
# Word № 2 = World
# Обратите внимание, что нумерация слов начинается с единицы

english_words = ('attack', 'bless', 'look', 'reckless', 'short', 'monster', 'trolley', 'sound',
                 'ambiguity', 'researcher', 'trunk', 'coat', 'quantity', 'question', 'tenant',
                 'miner', 'definite', 'kit', 'spectrum', 'satisfied', 'selection', 'carve',
                 'ask', 'go', 'suggest')

for value, index in enumerate(english_words, start = 1):
    print(f"Word № {value} = {index}")

# Алгоритм Луна (А вы знали, что цифры на банковской карте выбираются
# не просто случайным образом?)
# Упрощенная версия алгоритма выглядит так:
#
# Цифры проверяемой последовательности нумеруются справа налево.
# Цифры, оказавшиеся на нечётных местах, остаются без изменений.
# Цифры, стоящие на чётных местах, умножаются на 2.
# Если в результате такого умножения возникает число больше 9,
# оно уменьшается на значение 9
# Все полученные в результате преобразования 16 цифр складываются.
# Если сумма кратна 10, то исходные данные верны.

numbers = list(map(int, input()[::-1])) #так как заполнение справа налево, переворачиваме список
right_numder = []

for index, value in enumerate(numbers, start=1):
    if index % 2 == 0: 
        if value * 2 > 9:
            value = value * 2 - 9
            right_numder.append(value)
        else:
            value *= 2
            right_numder.append(value)

    else:
        right_numder.append(value)

if sum(right_numder) % 10 == 0:
    print("True")
else:
    print("False")