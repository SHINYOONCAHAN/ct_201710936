import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

width= wn.window_width()

x1=0.0 - (width-40)/3
x2=0.0
x3=0.0+ (width-40)/3

w3=(width-40)/3
x1=0.0-w3
x2=0.0
x3=0.0+w3

def triangle(size):
    t1.right(60)
    t1.fd(size)
    t1.right(120)
    t1.fd(size)
    t1.right(120)
    t1.fd(size)

def drawTriangleAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    triangle(size)    

drawTriangleAt(100,x1)

def pentagon(size):
    t1.right(36)
    t1.fd(size)
    t1.right(72)
    t1.fd(size)
    t1.right(72)
    t1.fd(size)
    t1.right(72)
    t1.fd(size)
    t1.right(72)
    t1.fd(size)    

def drawPentagonAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    pentagon(size)  

drawPentagonAt(100,x2)

def star(size):
    t1.right(72)
    t1.fd(size)
    t1.right(144)
    t1.fd(size)
    t1.right(144)
    t1.fd(size)
    t1.right(144)
    t1.fd(size)
    t1.right(144)
    t1.fd(size)

def drawStarAt(size,at):
    t1.penup()
    t1.goto(at,0)
    t1.setheading(0)
    t1.pendown()
    t1.write(t1.pos())
    star(size)  

drawStarAt(100,x3)

wn.exitonclick()