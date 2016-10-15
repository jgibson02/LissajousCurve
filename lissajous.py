from TkInter import *
from math import sin, cos
width = 640
height = 480
w = Canvas(Tk(), width=width, height=height)
w.pack()
t = 0
while 1:
    t += 0.1
    x = width/2 + (width * sin(1.0 / 60 * t)) * 0.49
    y = height/2 + (height * cos(1.0 / 44 * t)) * 0.49
    w.create_rectangle(x, y, x + 1, y + 1, fill = "black")
    w.update()