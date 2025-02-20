# Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы
# тогда давно купался
# в этих статуэтках).
#
# Ваша задача написать функцию print_best_and_worst_laureate, которая находит информацию, кто из номинантов
# получил наибольшее и наименьшее количество статуэток. Функция print_best_and_worst_laureate принимает на
# вход
# словарь, где указана номинация и имя победителя в ней (название фильма или имя актера). На основании этой
# информации функция print_best_and_worst_laureate должна в отдельных строках вывести лауреатов премии,
# набравших
# наибольшее и наименьшее количество статуэток и через запятую их количество.


def print_best_and_worst_laureate(laureates: dict[str, str]):
    count_laureates = {}
    for k, v in laureates.items():
        if v in count_laureates:
            count_laureates[v] += 1
        else:
            count_laureates[v] = 1

    sort_count_laureates_max = max(count_laureates, key=count_laureates.get)
    sort_count_laureates_min = min(count_laureates, key = count_laureates.get)

    print(f"{sort_count_laureates_max}, {count_laureates[sort_count_laureates_max]}")
    print(f"{sort_count_laureates_min}, {count_laureates[sort_count_laureates_min]}")

    #sort_count_laureates = sorted(count_laureates.items(), key=lambda v: v[1])  # list of tuples()
   

laureates = {'За лучший фильм': 'Оппенгеймер',
             'За лучшую музыку к фильму': 'Оппенгеймер',
             'За лучший звук': 'Зона интересов',
             'За лучшие визуальные эффекты': 'Бедные-несчастные',
             'За лучший дизайн костюмов': 'Бедные-несчастные',
             'За лучшую операторскую работу': 'Бедные-несчастные',
             'За лучший монтаж': 'Оппенгеймер',
             'За лучший оригинальный сценарий': 'Оппенгеймер',
             'За лучший фильм на иностранном языке': 'Зона интересов'}

print_best_and_worst_laureate(laureates)

# Рейтинг таксистов
# Руководитель таксопарка хочет увидеть отчет по всем таксистам, где нужно указать имя таксиста и его среднюю
# оценку. Информацию в отчете нужно расположить по убыванию средней оценки таксиста. Для этого вам нужно
# написать функцию
# print_order_rating, которая принимает на вход список кортежей. Каждый кортеж состоит из двух элементов:
# имя таксиста и оценка за поездку (целое число от 1 до 5).
#
# Функция print_order_rating должна расположить таксистов в порядке убывания их средней оценки и вывести имя
# каждого таксиста и его среднюю оценку в отдельной строке. В случае совпадения средних оценок нужно
# расположить каждую группу таксистов, имеющих одинаковый рейтинг,  по имени в алфавитном порядке без
# учета регистра


def print_order_rating(drivers: list[tuple[str, int]]):
    # Шаг 1: Создаем словарь для хранения оценок таксистов. значение ключа список оценок
    rez_drivers = {}
    for item in range(len(drivers)):
        if drivers[item][0] not in rez_drivers:
            rez_drivers[drivers[item][0]] = [drivers[item][1]]
        else:
            rez_drivers[drivers[item][0]].append(drivers[item][1])

    # Находим среднее значение списка оценок
    mid_drivers = {}
    for k, v in rez_drivers.items():
        mid_drivers[k] = sum(v) / len(v)

    # Сортируем по убванию оценок
    sort_mid_drivers = sorted(mid_drivers.items(), key = lambda x: (- x[1], x[0].lower()))

    for name, middle in sort_mid_drivers:
        print(f"{name} {middle}")

# 2 вариант решения этой задачи
def print_order_rating(drivers):
    # Шаг 1: Создаем словарь для хранения оценок таксистов
    ratings = {}

    for name, rating in drivers:
        # name_lower = name.lower()  # как пример, делала в sorted - Приводим имя к нижнему регистру для корректного сортирования
        if name not in ratings:
            ratings[name] = [rating]  # Если таксиста еще нет, добавляем в словарь имя - ключ и значение список оценок
        else:
            ratings[name].append(rating)  # Добавляем оценку в список, если уже есть имя в стиске

    # Шаг 2: Считаем средние оценки для каждого таксиста через генератор словаря
    average_ratings = {name: sum(scores) / len(scores) for name, scores in ratings.items()}

    # Шаг 3: Сортируем по средней оценке (по убыванию) и по имени (по возрастанию, если оценки одинаковы)
    sorted_ratings = sorted(average_ratings.items(), key=lambda x: (-x[1], x[0].lower()))

    # Шаг 4: Выводим результат
    for name, avg_rating in sorted_ratings:
        print(f"{name} {avg_rating}")

drivers = [
    ('Зина', 5),
    ('Зина', 3),
    ('Гермиона', 4),
    ('Гермиона', 4),
    ('александр', 4),
]
print_order_rating(drivers)

# Социальные сети
# В социальных сетях все как обычно: одни люди выкладывают посты, другие их комментируют. Сервис по сбору
# аналитики
# решил найти у кого из владельцев постов самое большое количество уникальных комментаторов. Ваша задача
# помочь им в этом и собрать нужную информацию. Для это вам потребуется написать функцию print_statistic, которая
# принимает список кортежей. Каждый кортеж состоит из пары значений: автор поста и далее ник пользователя, оставившего
# комментарий к этому посту. Комментаторы могут повторяться и комментировать разных авторов.
#
# Функция print_statistic должна посчитать для каждого автора его уникальное количество комментаторов.
# Исходя из найденного количества  определяется популярность автора. Чем больше уникальных пользователей
# прокомментировало автора, тем он считается популярнее. Затем функция print_statistic должна для каждого
# автора вывести в порядке уменьшения популярности информацию в следующем виде
#
# "Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
# На склонение давайте не будем обращать внимание в этой задаче.
#
# В случае одинаковой популярности у нескольких авторов, необходимо ранжировать по алфавитному порядку
# имени авторов без
# учета регистра
def print_statistic(data: list[tuple[str, str]]):

    # Создаем пустой словарь, с  уникальными значениями set()
    statistic_count = {}
    for author, comment in data:
        if author not in statistic_count:
            statistic_count[author] = set()
        statistic_count[author].add(comment)

   #Подсчитываем количество комментаторов в значение set()
    count_comments = {author: len(comment) for author, comment in statistic_count.items()}

   #Делаем сортировку
    sorted_statistic = sorted(count_comments.items(), key = lambda x: (-x[1], x[0].lower()))

   # Выводим результат
    for author, count in sorted_statistic:
        print(f"Количество уникальных комментаторов у {author} - {count}")


data = [
    ('karl', 'zhanna777'),
    ('karl', 'мама_игоречка_98'),
    ('qwerty03', 'pushka76'),
    ('Billy', 'мама_игоречка_98'),
    ('Billy', 'pushka76'),
    ('qwerty03', 'joebiden'),
    ('karl', 'zhanna777'),
    ('karl', 'joebiden'),
    ('karl', 'pushka76'),
]

print_statistic(data)