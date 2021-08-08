# Using the turtle module, write a program to draw a house.
# The house should at least have a roof, a door and some windows.
# Feel free to play around with the design of your house.

import turtle

def square(side_length, line_colour, fill_colour):
    turtle.color(line_colour, fill_colour)
    turtle.begin_fill()

    for number in range(4):
        turtle.right(90)
        turtle.forward(side_length)

    turtle.end_fill()

def rectangle(width, line_colour, fill_colour):
    turtle.color(line_colour, fill_colour)
    turtle.begin_fill()

    for number in range(2):
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(width*2)

    turtle.end_fill()

def roof(side_length, line_colour, fill_colour):
    turtle.color(line_colour, fill_colour)
    turtle.begin_fill()

    turtle.left(120)
    turtle.forward(side_length/4)
    turtle.left(60)
    turtle.forward(side_length/1.35)
    turtle.left(60)
    turtle.forward(side_length/4)
    turtle.left(120)
    turtle.forward(side_length)

    turtle.end_fill()

def window(side_length, line_colour, fill_colour):

    for number in range(4):
        square(side_length, line_colour, fill_colour)
        turtle.right(270)

def location(x,y):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()


turtle.speed(6)
location(60, 0)
rectangle(100, 'orange', 'orange')
location(60,0)
roof(200, 'grey', 'grey')
location(5,5)
window(25, 'black', 'white')
location(-120,5)
window(25, 'black', 'white')
location(-120, -110)
window(25, 'black', 'white')
location(5, -110)
window(25, 'black', 'white')
location(-30, -60)
rectangle(100, 'black', 'red')

turtle.done()