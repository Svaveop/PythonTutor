import turtle
import random

t = turtle.Turtle()
s = t.getscreen()
t.shape("turtle")
t.speed(0)
s.bgcolor("black")
t.pencolor("white")
colors = ("red", "green", "yellow", "blue", "cyan", "purple","orange", "white", "brown")


for i in range(36):
    t.circle(100)
    t.left(10)
    t.pencolor(colors[random.randint(0, 6)])
s.mainloop()
