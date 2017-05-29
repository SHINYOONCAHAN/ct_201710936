import turtle

def drawTriangle(size):
    for i in range(0,3):
        t1.fd(size)
        t1.right(120)

win = turtle.Screen()
t1 = turtle.Turtle()

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawTriangle(size)
    
drawTriangleAt(100,100,100)

win.exitonclick()