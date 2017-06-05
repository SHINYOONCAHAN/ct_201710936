import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
win.bgpic("mymaze.gif")

def islnTrap(x,y,x1,y1,x2,y2):
 minx=min(x1,x2)
 maxx=max(x1,x2)
 miny=min(y1,y2)
 maxy=max(y1,y2)
 if ((minx<x and x<maxx) and (miny<y and y<maxy)):
  return True
 else:
  return False

def drawRectWithFill(x1,y1,x2,y2,color):
 t1.goto(x1,y1)
 t1.fillcolor(color)
 t1.begin_fill()
 t1.goto(x2,y1)
 t1.goto(x2,y2)
 t1.goto(x1,y2)
 t1.goto(x1,y1)
 t1.end_fill()

def checkTrap(x,y):
 p = t1.pos()
 if isInTrap(x,y,-200,-200,200,200):
  drawRectWithFill(-200,-200,200,200,"red")

def keyup():
 p = t1.pos()
 t1.goto(p[0], p[1] + movepixel)
 checkTrap(p[0], p[1])

def keyup():
 pt = t1.pos()
 print("up", pt)
 t1.write(pt)
 t1.forward(45)
 if islnTrap(pt[0],pt[1],-200,-200,200,200):
  drawRectWithFill(0,0,20,20,"RED")

def keyleft():
 t1.left(45)

def keyright():
 t1.right(45)

def keydown():
 pt = t1.pos()
 print("down",pt)
 t1.write(pt)
 t1.back(45)

def addKeys():
 win.onkey(keyup, "Up")
 win.onkey(keyleft, "Left")
 win.onkey(keyright, "Right")
 win.onkey(keydown, "Down")
 win.onkey(win.bye, "q")

def mousegoto(x,y):
 msg = "mouse clicked {0} {1}".format(x,y)
 win.title(msg)
 t1.goto(x,y)

def addMouse():
 win.onclick(mousegoto)

def gamePlay():
 addKeys()
 addMouse()
 win.listen()
 turtle.mainloop()

gamePlay()