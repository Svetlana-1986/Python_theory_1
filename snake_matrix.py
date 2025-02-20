# Заполнение змейкой по строкам
# Даны числа n и m.
# Создайте массив A[n][m] и заполните его змейкой (см. пример).
#
# Входные данные
# Программа получает на вход два числа n и m.
#
# Выходные данные
# Программа должна вывести  полученный массив,
# при этом между числами может быть любое количество пробелов.

n, m = map(int, input().split())
matrix = []
count = 0  # счетчик индексов
a = 0  # счетчик чисел

for i in range(n):
    matrix.append([0] * m)  # заполняем матрицу 0

for i in range(n):
    if count % 2 == 0:
        for j in range(m):
            matrix[i][j] = a
            a += 1
    elif count % 2 != 0:
        for j in range(m - 1, -1, -1):
            matrix[i][j] = a
            a += 1
    count += 1

for row in matrix:
    print(*row)


# ЗМЕЙКА по столбцам сверху вниз, снизу вверх и т. д.


n, m = map(int, input().split())
a = []

for i in range(n):
    a.append([0] * m)

d = 0  # числа
for j in range(m): #заполняем свеху вниз
    if j % 2 == 0:
        for i in range(n):
            d += 1
            a[i][j] = d

    if j % 2 != 0:
        for i in range(n - 1, -1, -1): #заполнение начинается снизу вверх сосоеднего столбца
            d += 1
            a[i][j] = d

for i in a:
    print('\t'.join(map(str, i)))

#СПИРАЛЬ n на n с левого верхнего угла

n = int(input())
mas = [[0] * n for i in range(n)]
i = 1 # заполнение первой ячейки [0][0] с 1
x = 0 #строка индекс (тек. положение ячейки)
y = -1 # индекс колонки, начинаем с не существующей левой ячейки
d_row = 0 # движение по ряду (-1 это вверх, 0 в том жя ряду, 1 это вниз)
d_column = 1 #движение по колонкам (-1 это вверх, 0 в том жя ряду, 1 это вниз)
length = len(str(n**2)) # для итогового вывода в принте

while i <= n ** 2:
    if 0 <= x + d_row < n and 0 <= y + d_column < n and mas[x + d_row][y + d_column] == 0: # последним действием проверяем свободнв ли ячейка
        x += d_row
        y += d_column
        mas[x][y] = i #записываем в ячейку значение
        i += 1
    else: #когда в ячейку шагнуть не можем, выщли за массив, либо там цифра > 0
        if d_column == 1: # идем вправо, опускаемся вниз
            d_column = 0
            d_row = 1
        elif d_row == 1: # идем влево
            d_row = 0
            d_column = -1
        elif d_column == -1: # идем вверх и влево
            d_column = 0
            d_row = -1
        elif d_row == -1:  # идем вправо
            d_row = 0
            d_column = 1

for row in mas:
    for elem in row:
        print(str(elem.rjust(length)), end = ' ')
    print()





