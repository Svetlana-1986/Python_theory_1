###Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел
###в пределах от -100 до 100 включительно, сортировкой подсчетом.
###Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
###Вам необходимо вывести отсортированный список
###P.S. не пользуйтесь встроенной функцией sorted или методом sort

n = int(input())
a = list(map(int, input().split()))
count = [0] * 201

for i in a:
    count[i + 100] += 1 #добавляем [число i+100]

for i in range(201):
    if count[i] > 0:
        print(count[i] * (str(i-100) + ' '), end = '')

