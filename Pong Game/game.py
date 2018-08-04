import pygame
from ball import ball
from paddle import paddle



# Initilize
pygame.init()
pygame.display.set_caption("Pong game")
loop = True
clock = pygame.time.Clock()
BG_COLOR = (47,62,63)

# Set up game window
SIZE = (800,600)
canvas = pygame.display.set_mode(SIZE)


# Create object
ball = ball(400,300)
paddle1 = paddle(100,300)
paddle2 = paddle(685,300)
paddle_list = [paddle1,paddle2]

while loop:
    # Pooling
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
           loop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1.up_press = True
            if event.key == pygame.K_s:
                paddle1.down_press = True
            if event.key == pygame.K_UP:
                paddle2.up_press = True
            if event.key == pygame.K_DOWN:
                paddle2.down_press = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1.up_press = False
            if event.key == pygame.K_s:
                paddle1.down_press = False
            if event.key == pygame.K_UP:
                paddle2.up_press = False
            if event.key == pygame.K_DOWN:
                paddle2.down_press = False
   
    canvas.fill(BG_COLOR)         
    paddle1.update(canvas)
    paddle2.update(canvas)
    ball.update(paddle_list,canvas)
        
    clock.tick(60)
    pygame.display.flip()
    