# Обход элементов матрицы - 2
# Задана целочисленная квадратная матрица размером N x N.
# Необходимо обойти элементы этой матрицы снизу вверх справа налево и
# вывести элементы именно в таком порядке в виде таблицы.
#
# Программа принимает на вход натуральное число N – количество строк и
# столбцов матрицы. В каждой из последующих N строк записаны N целых чисел – элементы матрицы.
# Ввод
# 5
# # 3 4 9 6 2
# # 8 2 0 5 1
# # 4 7 4 8 7
# # 7 1 3 3 8
# # 5 6 3 7 0
# Вывод
# 0 8 7 1 2
# 7 3 8 5 6
# 3 3 4 0 9
# 6 1 7 2 4
# 5 7 4 8 3

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
for column in range(n - 1, -1, -1):
    for row in range(n - 1, -1, -1):
        print(a[row][column], end = ' ')
    print()
