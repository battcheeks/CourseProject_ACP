import turtle
from time import sleep
ANGLES = [60, -120, 60, 0]
SIZE_OF_SNOWFLAKE = 340
def get_input_depth():
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer!')
        value_as_string = input(message)
    return int(value_as_string)
def setup_screen(title, background='white', screen_size_x=640, screen_size_y=320, tracer_size=800):
    turtle.title(title)
    turtle.setup(screen_size_x, screen_size_y)
    turtle.hideturtle()
    turtle.penup()
    turtle.backward(240)
    turtle.tracer(tracer_size)
    turtle.bgcolor(background)

def draw_koch(size, depth):
    if depth > 0:
        for angle in ANGLES:
            draw_koch(size / 3, depth - 1)
            turtle.left(angle)
    else: turtle.forward(size)
depth = 7
setup_screen('Start Up Sequence', background='black', screen_size_x=410, screen_size_y=400)
turtle.color('yellow')
turtle.pensize(0)
turtle.penup()
turtle.setposition(-190,0)
turtle.left(30)
turtle.pendown()
for i in range(0,6):
    draw_koch(SIZE_OF_SNOWFLAKE, depth)
    turtle.right(120)
    turtle.color('red')
    turtle.pensize(3)
    turtle.speed('fastest')


turtle.color('yellow')
turtle.pensize(10)
style = ('Calibri', 23,'bold')
turtle.write('     Advanced Course Project', font=style, align='left')
sleep(1.5)
turtle.bye()
exec(open("acp.py").read())