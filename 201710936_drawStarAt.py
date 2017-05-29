import turtle

def drawStar(size):
    for i in range(0,5):
        t1.fd(size)
        t1.right(144)
        
win = turtle.Screen()
t1 = turtle.Turtle()

def drawStarAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawStar(size)

drawStarAt(100,100,100)

win.exitonclick()