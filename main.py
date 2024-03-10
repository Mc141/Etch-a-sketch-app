import turtle as Turtle

t = Turtle.Turtle()


def forward():
    t.forward(10)

def backwards():
    t.backward(10)

def left():
    t.left(10)

def right():
    t.right(10)

def clear():
    t.home()
    t.clear()


Turtle.listen()

Turtle.onkey(forward, "w")
Turtle.onkey(backwards, "s")
Turtle.onkey(left, "a")
Turtle.onkey(right, "d")
Turtle.onkey(clear, "c")


Turtle.mainloop()