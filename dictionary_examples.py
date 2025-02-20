# Система регистрации
# В скором времени в Берляндии откроется новая почтовая служба "Берляндеск".
# Администрация сайта хочет запустить свой проект как можно быстрее, поэтому они попросили
# Вас о помощи. Вам предлагается реализовать прототип системы регистрации сайта.
#
# Система должна работать по следующему принципу. Каждый раз, когда новый пользователь хочет
# зарегистрироваться, он посылает системе запрос name со своим именем. Если данное имя не
# содержится в базе данных системы, то оно заносится туда и пользователю возвращается ответ OK,
# подтверждающий успешную регистрацию. Если же на сайте уже присутствует пользователь с именем name,
# то система формирует новое имя и выдает его пользователю в качестве подсказки, при этом подсказка
# также добавляется в базу данных. Новое имя формируется по следующему правилу.
# К name последовательно приписываются числа, начиная с единицы (name1, name2, ...), и среди них
# находят такое наименьшее i, что namei не содержится в базе данных сайта.
#
# Входные данные
# В первой строке входных данных задано число n (1 ≤ n ≤ 105).
# Следующие n строк содержат запросы к системе. Каждый запрос представляет собой непустую
# строку длиной не более 32 символов, состоящую только из строчных букв латинского алфавита.
#
# Выходные данные
# В выходных данных должно содержаться n строк — ответы системы на запросы: OK в случае
# успешной регистрации, или подсказку с новым именем, если запрашиваемое уже занято.

n = int(input())
database = {}

for i in range(n):
    login = input()
    if login in database:
        database[login] += 1 # увеличиваем значение ключа каждый раз когда встречается токой же логин
        database[f"{login}{database[login]}"] = 0 # добавляем в словарь ключ с новым логином, формируем его конкетинацией логина + значением ключа из позиции выше
        print(f"{login}{database[login]}") # печатаем новый логин
    else:
        database[login] = 0
        print(f'OK')

# Переменные countries соединяют ряд стран с тремя крупнейшими городами каждой страны.
#
# Программе на вход будет поступать название города в переменную city.
# И ваша задача найти какой стране принадлежит введенный город. Если страна успешно найдена,
# необходимо вывести сообщение:
#
# INFO: <City> is a city in <Country>
# в противном случае
#
# ERROR: Country for {City} not found
# Учитывайте, что регистр букв имеет значение

countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()

for key, values in countries.items():
    if city in values:
        print(f"INFO: {city} is a city in {key}")
        break
else:
    print(f"ERROR: Country for {city} not found")

# Перед вами словарь user
# При помощи метода pop переименуйте в нем следующие ключи:
# ключ password в ключ secret
# ключ last_name в ключ surname
# Выводить ничего не нужно, только изменить ключи словаря

user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17"
}
user['secret'] = user.pop('password')
user['surname'] = user.pop('last_name')

#Вложенные словари
# Напишите код для преобразования списка из целых чисел произвольной длины в словарь,
# вложенность которого зависит от длины списка.
#
# Например, если перед вами был бы такой список
#
# [100, 55, 77, 55, 89]
# то он должен превратиться в такой словарь
#
# {100: {55: {77: {55: 89}}}}
# На вход программе поступают числа для списка в одну строку, гарантируется, что в
# списке будет как минимум два элемента.
#
# Ваша задача вывести полученный словарь

a = list(map(int,input().split()))
d = a[-1]

for i in a[-2::-1]:
    d = {i:d}
print(d)