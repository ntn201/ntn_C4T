from random import randint
import pygame
from boxcollider import BoxCollider

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = [0,0]
        self.speed = 6
        self.image = pygame.image.load("Assets/ball.png")
        self.box_collider = BoxCollider(self,self.image.get_width(),self.image.get_height())

    def move(self,other):
        # Pick a random direction when game start
        if self.direction == [0,0]:
            rnd = randint(0,4)
            if rnd == 0:
                self.direction = [1,1] # Right down
            elif rnd == 1:
                self.direction = [-1,1] # Left down 
            elif rnd == 2:
                self.direction = [1,-1] # Right up
            elif rnd == 4:
                self.direction = [-1,-1] # Left up
        
        # Move slower if speed is fast
        if abs(self.direction[0]) > 1:
                self.direction[0] -= 0.1* sign(self.direction[0])
        if abs(self.direction[1]) > 1:
                self.direction[1] -= 0.1* sign(self.direction[1])

        #Change direction if collide with paddle
        for obj in other:
            if self.box_collider.collide_with(obj.boxcollider):
                if self.box_collider.collide_with_top(obj.boxcollider):
                    self.direction[0] += 0
                    self.direction[1] += -2
                if self.box_collider.collide_with_bottom(obj.boxcollider):
                    self.direction[0] += 0
                    self.direction[0] += 2
                if self.box_collider.collide_with_left(obj.boxcollider):
                    self.direction[0] += -2
                    self.direction[0] += 0
                if self.box_collider.collide_with_right(obj.boxcollider):
                    self.direction[0] += 2
                    self.direction[0] += 0
                # if obj.up_press or obj.down_press:
                #     self.direction[0] *= 1.5
                #     self.direction[1] *= 1.5
        # Change direction if collide with window
        if self.x >= 785 or self.x <= 15:
            self.direction[0] *= -1
        if self.y >= 585 or self.y <= 15:
            self.direction[1] *= -1
        
        print (self.direction)
        
        # Apply movements
        self.x += (self.direction[0] * self.speed)
        self.y += (self.direction[1] * self.speed)
    
    def update(self,other,canvas):
        self.move(other)
        self.box_collider.x = self.x
        self.box_collider.y = self.y
        width = self.image.get_width()
        height = self.image.get_height()
        render_pos = (self.x - width/2, self.y - height/2)
        canvas.blit(self.image,render_pos)
        self.box_collider.render(canvas)

        