import turtle
wn = turtle.Screen()

number_sides = int(turtle.numinput("poly", "Enter the number of sides : "))
length = int(turtle.numinput("poly", "Enter the length of sides : "))
color = turtle.textinput("poly", "Enter the color : ")

p = turtle.Turtle()
p.color(color)
p.shape("turtle")

angle = 360 / number_sides
p.setpos (0, 0)

for x in range(number_sides):
    p.forward (length)
    p.left (angle)

wn.exitonclick()
turtle.done()