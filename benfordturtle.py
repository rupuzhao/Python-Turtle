import turtle
import os
import re

#set screen and turtle
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('frequency')

t = turtle.Turtle()
t.color('white', 'red')
t.pensize(3)
t.shape('turtle')
t.speed(0)

#create a draw_bar method
def draw_bar(t, height):
    t.begin_fill()
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.write("%5d, %0.2f%s" % (j + 1, result, "%"), font=("Arial", 20, "normal"))
    t.right(90)
    t.forward(height)
    t.penup()
    t.left(90)
    t.forward(20)
    t.pendown()
    t.left(90)
    t.end_fill()

#open files and read numbers from files
file = raw_input("Enter the name of file(includes path and suffix): ")
f = open(os.path.expanduser(file))

numberStore = [0,0,0,0,0,0,0,0,0]
number = [1,2,3,4,5,6,7,8,9]

for line in f:
    a = re.findall(r'\d+', line)
    for line in a:
        value = int(line[0])
        for i in range(0, 9):
            if value == number[i]:
                numberStore[i] = float(numberStore[i] + 1)

#start to draw bar
t.penup()
t.setpos(-380, 280)
t.pendown()

for j in range(0, 9):
    result = (numberStore[j] / sum(numberStore)) * 100
    printResult = result * 8
    draw_bar(t, printResult)

wn.exitonclick()