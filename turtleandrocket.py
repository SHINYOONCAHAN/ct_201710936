Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> wn = turtle.Screen()
>>> t1 = turtle.Turtle()
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> t1.left(90)
>>> t1.forward(100)
>>> wn
<turtle._Screen object at 0x00C36CB0>
>>> type(wn)
<class 'turtle._Screen'>
>>> print type(wn)
SyntaxError: invalid syntax
>>> print type(wn)
SyntaxError: invalid syntax
>>> print(type(wn))
<class 'turtle._Screen'>
>>> type(t1)
<class 'turtle.Turtle'>
>>> wn.setup(500,500)
>>> wn.setup(500,100)
>>> wn.setup(500,500)
>>> wn.setup(500,100)
>>> wn.setup(500,500,0,0\)
	 
SyntaxError: unexpected character after line continuation character
>>> wn.setup(500,500,0,0)
>>> wn.setup(500,500,0,0)
>>> wb,setyo(500,500,0,0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    wb,setyo(500,500,0,0)
NameError: name 'wb' is not defined
>>> t1.fd(100)
>>> t1.fd()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    t1.fd()
TypeError: forward() missing 1 required positional argument: 'distance'
>>> t1.lt()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t1.lt()
TypeError: left() missing 1 required positional argument: 'angle'
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.rt(90)
>>> t1.lt(90)
>>> t1.fd(100)
>>> tq.fd(100)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tq.fd(100)
NameError: name 'tq' is not defined
>>> t1.lt(90)
>>> t1.fd(200)
>>> t1.rt(90)
>>> t1.fd(100)
>>> t1.rt(90)
>>> t1.fd(100)
>>> t1.rt(90)
>>> t1.fd(200)
>>> t1.lt(90)
>>> t1.fd(200)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.pencolor("Red")
>>> t1.fd(50)
>>> wn.colormode(255)
>>> t1.pencolor((0,100,200))
>>> t1.fd(50)
>>> t1.colormode("Gray")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    t1.colormode("Gray")
AttributeError: 'Turtle' object has no attribute 'colormode'
>>> t1.pencolor("Gray")
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(200)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.rt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> t1.lt(90)
>>> t1.fd(100)
>>> wn.colormode(255)
>>> t1.pencolor((0,100,200))
>>> t1.shape("turtle")
>>> wn.addshape("C:\Users\400T6B\Downloads\rocketship.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wnaddshape("C:\Users\400T6B\Downloads\rocketship.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape("C:\Users\400T6B\Downloads\rocketship.gif")0
SyntaxError: invalid syntax
>>> wn.addshape("C:\Users\400T6B\Downloads\rocketship.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape(("C:\Users\400T6B\Downloads\rocketship.gif"))
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape("C:\Users\400T6B\Downloads\rocketship.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> t1.shape("C:\Users\400T6B\Downloads\rocketship.gif")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> wn.addshape("C:\\Users\400T6B\Downloads\\rocketship.gif")
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    wn.addshape("C:\\Users\400T6B\Downloads\\rocketship.gif")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3539, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3495, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "C:\UsersĀT6B\Downloads\rocketship.gif": no such file or directory
>>> wn.addshape("C:\\Users\400T6B\\Downloads\\rocketship.gif")
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    wn.addshape("C:\\Users\400T6B\\Downloads\\rocketship.gif")
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 1133, in register_shape
    shape = Shape("image", self._image(name))
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\turtle.py", line 479, in _image
    return TK.PhotoImage(file=filename)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3539, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\400T6B\AppData\Local\Programs\Python\Python36-32\lib\tkinter\__init__.py", line 3495, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "C:\UsersĀT6B\Downloads\rocketship.gif": no such file or directory
>>> wn.addshape("C:\\Users\\400T6B\\Downloads\\rocketship.gif")
>>> t1.shape("C:\\Users\\400T6B\\Downloads\\rocketship.gif")
>>> 
