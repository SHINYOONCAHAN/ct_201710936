import turtle

def drawSquare(size):
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)

def drawTriangle(size):
    for i in range(0,3):
        t1.fd(size)
        t1.right(120)

def drawStar(size):
    for i in range(0,5):
        t1.fd(size)
        t1.right(144)

win = turtle.Screen()
t1 = turtle.Turtle()

def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawSquare(size)

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawTriangle(size)

def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawStar(size)
    
drawSquareAt(100,0,100)

drawTriangleAt(300,0,100)

drawStarAt(500,0,100)
win.exitonclick()