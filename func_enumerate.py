# ЗАДАЧИ
# 1. Перед вами кортеж english_words
#
# При помощи enumerate обойдите слова этой коллекции и для каждого элемента выведите строку вида
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

for number, word in enumerate(english_words, start = 1):
    print(f"Word № {number} = {word}")

# Word № 1 = attack
# Word № 2 = bless
# Word № 3 = look
# Word № 4 = reckless
# Word № 5 = short
# Word № 6 = monster
# Word № 7 = trolley
# Word № 8 = sound
# Word № 9 = ambiguity
# Word № 10 = researcher
# Word № 11 = trunk
# Word № 12 = coat
# Word № 13 = quantity
# Word № 14 = question
# Word № 15 = tenant
# Word № 16 = miner
# Word № 17 = definite
# Word № 18 = kit
# Word № 19 = spectrum
# Word № 20 = satisfied
# Word № 21 = selection
# Word № 22 = carve
# Word № 23 = ask
# Word № 24 = go
# Word № 25 = suggest


# 2. Напишите функцию get_words_with_position , которая принимает на вход строку words, состоящую из слов,
# разделенных пробелом.
#
# Функция get_words_with_position должна создать и вернуть список кортежей, где каждый элемент-кортеж должен
# содержать два значения: само слово и его порядковый номер в исходной строке words.
#
# Порядковый номер слов необходимо считать с единицы.

def get_words_with_position(words: str) -> list[tuple]:
    # words_list = words.split()
    return [(word, index) for index, word  in enumerate(words.split(), start = 1)]

print(get_words_with_position('И тянутся города Я в каждом из них бывал'))


# 3.Напишите функцию find_different_indexes, которая принимает две строки одинаковой длины и возвращает список
# индексов, на позициях которых находятся разные символы в этих строках.

def find_different_indexes(s1: str, s2: str) -> list[int]:
    return [i for i, (ch1, ch2) in enumerate(zip(s1, s2)) if ch1 != ch2]

print(find_different_indexes('abracadabra', 'uzrucuduzru'))

# [0, 1, 3, 5, 7, 8, 10]

# 4. Алгоритм Луна
# Сумма определенных цифр на карте должна проходить условия алгоритма Луна
# Упрощенная версия алгоритма выглядит так:
# Цифры проверяемой последовательности нумеруются справа налево
# Цифры, оказавшиеся на нечётных местах, остаются без изменений;
# Цифры, стоящие на чётных индексах, умножаются на 2. Если в результате такого умножения возникает число больше 9,
# оно уменьшается на значение 9;
# Все полученные в результате преобразования 16 цифр складываются. Если сумма кратна 10, то исходные данные верны.

# Ваша задача  - написать функцию luhn_algorithm, которая проверяет, является ли переданный номер карты валидным
# в соответствии с алгоритмом Луна. Функция luhn_algorithm должна вернуть True, если номер карты валидный,
# в противном случае - False.

def luhn_algorithm(digits) -> bool:
    digits = str(digits)  # Убедимся, что вход — строка
    rez = []

    # Перебираем цифры с конца (справа налево)
    for i, v in enumerate(digits[::-1]):  # Переворачиваем строку
        digit = int(v)  # Преобразуем символ в число

        if i % 2 != 0:  # Нечетные индексы (считаем с 0)
            digit = digit * 2
            if digit > 9:  # Если результат больше 9, уменьшаем на 9
                digit -= 9
        # На четных индексах (считаем с 0) оставляем как есть

        rez.append(digit)

    # Если сумма чисел кратна 10, то строка валидна по алгоритму Луна
    return sum(rez) % 10 == 0

print(luhn_algorithm(1217040151414995))