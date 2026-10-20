
import turtle

screen = turtle.Screen()
screen.title("Task 1 - Turtle Graphics")
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# Draw the square body
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("black", "orange")
t.begin_fill()

for i in range(4):
    t.forward(200)
    t.left(90)

t.end_fill()

# Draw the triangular roof
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("black", "red")
t.begin_fill()

for i in range(3):
    t.forward(200)
    t.left(120)

t.end_fill()

# Draw the door
t.penup()
t.goto(-30, -100)
t.pendown()
t.color("black", "brown")
t.begin_fill()

for i in range(2):
    t.forward(60)
    t.left(90)
    t.forward(100)
    t.left(90)

t.end_fill()

t.hideturtle()
turtle.done()
