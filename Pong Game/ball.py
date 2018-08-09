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

    def coliision_check(self,other,moveX,moveY):
        # Horizontal check
        hor_check_box = BoxCollider(self,self.image.get_width(),self.image.get_height())
        hor_check_box.x += moveX
        if hor_check_box.collide_with(other.boxcollider):
            while not self.box_collider.collide_with(other.boxcollider):
                self.x += 1
                self.box_collider.x += 1
            moveX = 0
        # Vertical check
        ver_check_box = BoxCollider(self,self.image.get_width(),self.image.get_height())
        ver_check_box.x += moveY
        if ver_check_box.collide_with(other.boxcollider):
            while not self.box_collider.collide_with(other.boxcollider):
                self.y += 1
                self.box_collider.y += 1
            moveY = 0
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
            if obj.active:
                if self.box_collider.collide_with(obj.boxcollider):
                    ver = self.box_collider.collide_with_vertical(obj.boxcollider)
                    hor = self.box_collider.collide_with_horizon(obj.boxcollider)
                    print (self.direction)
                    top = (obj.y + obj.boxcollider.height/2) - (self.y - self.image.get_height()/2)
                    bot = (self.y + self.image.get_height()/2) - (obj.y - obj.boxcollider.height/2)
                    left = (obj.x + obj.boxcollider.width/2) - (self.x - self.image.get_width()/2) 
                    right = (self.x + self.image.get_width()/2) - (obj.x - obj.boxcollider.width/2)
                    if ver:
                        if top < left or bot < left or top < right or bot < right :
                            print ("hihi")
                            print(abs(self.y - obj.y))
                            print((self.y - self.image.get_height()/2),(obj.y + obj.boxcollider.height/2))#top
                            print((self.y + self.image.get_height()/2),(obj.y - obj.boxcollider.height/2))#bot
                            print((self.x - self.image.get_width()/2),(obj.x + obj.boxcollider.width/2))#left
                            print((self.x + self.image.get_width()/2),(obj.x - obj.boxcollider.width/2))
                            self.direction[1] *= -1
                        else:
                            print("haha")
                            self.direction[0] *= -1
                    elif ver:
                         self.direction[1] *= -1
                         print("hehe")
                    elif hor:
                        self.direction[0] *= -1
                        print("hoho")
                    print (self.direction)
                    for paddle in other:
                        paddle.active = True
                    obj.active = False
        # Change direction if collide with window
        if self.x >= 785 or self.x <= 15:
            self.direction[0] *= -1
            for obj in other:
                obj.active = True
        if self.y >= 585 or self.y <= 15:
            self.direction[1] *= -1
            for obj in other:
                obj.active = True
        
        
        # Apply movements
        moveX = (self.direction[0] * self.speed)
        moveY = (self.direction[1] * self.speed)
        self.x += moveX
        self.y += moveY
    
    def update(self,other,canvas):
        self.move(other)
        self.box_collider.x = self.x
        self.box_collider.y = self.y
        width = self.image.get_width()
        height = self.image.get_height()
        render_pos = (self.x - width/2, self.y - height/2)
        canvas.blit(self.image,render_pos)
        self.box_collider.render(canvas)

        