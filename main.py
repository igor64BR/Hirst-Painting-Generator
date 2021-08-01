import turtle as t
import random as rand
color_palette = [
    (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157),
    (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55),
    (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110),
    (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)
]
t.colormode(255)
# Screen DATA
display = t.Screen()
print(display.canvwidth)
print(display.canvheight)

# Turtle DATA
crush = t.Turtle()
crush.shape('turtle')
crush.color('green')
crush.speed('fastest')
crush.hideturtle()
dot_size = 20
dot_space = 50
x_position = -400
y_position = -300

crush.penup()
crush.goto(x_position, y_position)
crush.goto(x_position, y_position)

next_y = y_position
for y in range(13):
    next_x = x_position
    crush.goto(next_x, next_y)
    for x in range(17):
        crush.goto(next_x, next_y)
        crush.pd()
        crush.dot(dot_size, rand.choice(color_palette))
        next_x += 50
        crush.pu()
    next_y += 50

crush.fd(50)
display.exitonclick()
