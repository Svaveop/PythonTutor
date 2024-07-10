import turtle

tur = turtle.Turtle()
screen = tur.getscreen()
tur.shape("turtle")
# tur.speed(8)
tur.pensize(3)

def square(a, b, colors):
    tur.penup()
    tur.goto(a, b)
    tur.pendown()
    tur.color(colors)
    for i in range(3):
        tur.forward(100)
        tur.left(120)

square(0, 0, "cyan")
square(120, 0, "green")
square(240, 0, "purple")

screen.mainloop()
