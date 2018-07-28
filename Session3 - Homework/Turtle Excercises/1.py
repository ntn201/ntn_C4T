from turtle import *

speed("fastest")
shape("turtle")

color_list = ["red", "blue","brown", "yellow", "gray"]

n_angle = 3

for color in color_list:
    pencolor(color)
    for j in range(n_angle):
        left(360/n_angle)
        forward(150)
    n_angle += 1

mainloop()