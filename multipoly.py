import turtle
import random
wn = turtle.Screen()
wn.colormode(255)

number_sides = int(turtle.numinput("poly", "Enter the number of sides : ", "3"))
length = int(turtle.numinput("poly", "Enter the length of sides : ", "100"))
number_petals = int(turtle.numinput("poly", "Enter number of polygons: ", "3"))
fillcolor = turtle.textinput("poly", "do you want to fill these polygons? (yes or no)")

p = turtle.Turtle()
p.setpos (0, 0)
p.shape("turtle")
p.speed(50)
p.pensize(3)

angle1 = 360 / number_sides
angle2 = 360 / (number_petals)

if fillcolor == "yes":
    for y in range (number_petals):
        p.left(angle2)
        p.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        p.begin_fill()
        for x in range(number_sides):
            p.forward (length)
            p.left (angle1)
        p.end_fill()

if fillcolor == "no":
    for y in range (number_petals):
        p.left(angle2)
        for x in range(number_sides):
            p.forward (length)
            p.left (angle1)

wn.exitonclick()
turtle.done()