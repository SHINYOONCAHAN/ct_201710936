import turtle

def drawSquare(size):
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
        
win = turtle.Screen()
t1 = turtle.Turtle()

def drawSquareAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawSquare(size)

drawSquareAt(100,100,100)
    
win.exitonclick()