
import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Task 2 - Colorful Star Pattern")
screen.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# Function to draw a star
def draw_star(size, color):
    t.color(color)

    for i in range(5):
        t.forward(size)
        t.right(144)

# List of star colors
colors = ["red", "yellow", "cyan", "magenta", "lime", "orange"]

# Draw six stars
for i in range(6):
    t.penup()
    t.goto(-250 + i * 100, 0)
    t.pendown()

    draw_star(70, colors[i])

# Finish
t.hideturtle()
turtle.done()

