import turtle


def move(size):
    turtle.forward(size)
    turtle.left(90)


def draw_square(size):
    for i in range(4):
        move(size)


def draw_color_square(size, name_color):
    turtle.color(name_color)
    turtle.begin_fill()
    draw_square(size) # вызываем функцию draw_square
    turtle.end_fill()


turtle.speed(1)
turtle.goto(0, -150)
draw_color_square(50, 'red')
turtle.goto(0, 0)
draw_color_square(100, 'green')
turtle.goto(0, 150)
draw_color_square(150, 'blue')