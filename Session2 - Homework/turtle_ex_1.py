from turtle import *

shape("turtle")
speed("fastest")
color("red")

for i in range(4):
    right(30)
    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    right(120)

mainloop()