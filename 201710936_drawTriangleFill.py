import turtle

def drawTriangle(size):
    for i in range(0,3):
        t1.fd(size)
        t1.right(120)

def drawTriangleFill(size, color):
    t1.fillcolor(color)
    t1.begin_fill()
    drawTriangle(size)
    t1.end_fill()
    
win = turtle.Screen()
t1 = turtle.Turtle()

def drawTriangleAt(x,y,size):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    drawTriangle(size)
    
def drawTriangleAtFill(x,y,size,color):
    t1.fillcolor(color)
    t1.begin_fill()
    drawTriangleAt(x,y,size)
    t1.end_fill()
    
drawTriangleAtFill(0,0,100,"Red")
    
win.exitonclick()