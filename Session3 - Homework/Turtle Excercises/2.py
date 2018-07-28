from turtle import *

shape("turtle")
speed(0)

color_list = ["red", "blue","brown", "yellow", "gray"]


for i,colour in enumerate(color_list):
    color(colour)
    begin_fill()
    for i in range(4):
        if (i%2) == 0:
            forward(50)
        else:
            forward(100)
        left(90)
    forward(50)
    end_fill()

mainloop()