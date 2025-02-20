# Морской бой - 2
# «Морской бой» - игра для двух участников, в которой игроки по очереди называют координаты на
# неизвестной им карте соперника. Если у соперника по этим координатам имеется корабль,
# о корабль или его часть «топится», а попавший получает право сделать еще один ход. Цель игрока - первым поразить все корабли противника.
#
# «Морской бой» очень популярен среди учеников одной физико-математической школы. Ребята очень
# любят в него играть на переменах. Вот и сейчас ученики Иннокентий и Емельян начали новую партию.
#
# Правила, по которым ребята расставляют корабли перед началом партии, несколько отличаются от
# классических. Во-первых, игра происходит на поле размером N×M, а не 10×10. Во-вторых,
# число кораблей, их размер и форма выбираются ребятами перед партией - так играть намного интереснее.
#
# Емельян уже расставил все свои корабли, кроме одного однопалубного.
# Такой корабль занимает ровно одну клетку.
#
# Задана расстановка кораблей Емельяна. Найдите число способов поставить оставшийся однопалубный
# корабль. При этом учитывайте, что по правилам его можно ставить только в ту клетку, все соседние
# с которой не заняты. В этой задаче соседними считаются клетки, имеющие общую сторону.
#
# Программа считывает два числа: N и M (1 ≤ N, M ≤ 100). Последующие N строк описывают игровое
# поле - каждая из них содержит M символов. Символом «.» (точка) обозначена свободная клетка,
# символом «*» (звездочка) - занятая кораблем.
#
# Необходимо вывести на экран ответ на задачу

n, m = map(int, input().split())
mas = []
mas.append('.' * (m +2)) #верхний барьерный ряд

for i in range(n):
    row = '.' + input() + '.' # 2боковых барьерных рядя
    mas.append(row)
mas.append('.' * (m +2)) #нижний барьерный ряд

k = 0
for i in range(1, n + 1): #начинаем с 1 не берем барьерный ряд
    for j in range(1, m + 1):
        if mas[i-1][j] == '.' and mas[i][j+1] == '.' and mas[i+1][j] == '.' and mas[i][j-1] == '.' and mas[i][j] == '.':
            k += 1
print(k)