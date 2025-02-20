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
        elif d_row == -1:  # если поднимались вверх, то идем вправо
            d_row = 0
            d_column = 1

for row in mas:
    for elem in row:
        print(str(elem).rjust(length), end = ' ')
    print()

# СПИРАЛЬ N х M

n, m = map(int, input().split())
tmp = ([[0] * m for i in range(n)])
x, y = 0, 0 # индексы
d_x, d_y = 0, 1 # движение по строке, столбцу
tmp[0][0] = 1 # присваеваем первой ячейке 1
count = 2 # след значение числа по 1

while count <= n * m:
    if 0 <= x + d_x <= n - 1 and 0 <= y + d_y <= m - 1 and tmp[x + d_x][y + d_y] == 0:
        tmp[x + d_x][y + d_y] = count
        count += 1
        x += d_x
        y += d_y
    else:
        if d_y == 1:
            d_y = 0
            d_x = 1
        elif d_x == 1:
            d_x = 0
            d_y = -1
        elif d_y == -1:
            d_y = 0
            d_x = -1
        elif d_x == -1:
            d_x = 0
            d_y = 1
for row in range(n):
    for column in range(m):
        print(str(tmp[row][column]).ljust(3), end = ' ')
    print()






