from pygame.locals import *
import pygame, random

"""
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("THE GREAT WALL")
dot= [(600, 0)]
dot = pygame.Surface((10, 10))
dot.fill((255,255,255))

wall_x= [(590, 50)]
wall_skin_x = pygame.Surface((10, 10))
wall_skin_x.fill((255,255,255))

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0)) #White


wall_y= [(0, 50)]
wall_skin_y = pygame.Surface((10, 10))
wall_skin_y.fill((255,255,255))



while True:
   
    for pos in wall_x:
        screen.blit(wall_skin_x,pos)

    for pos in wall_y:
        screen.blit(wall_skin_y,pos)

    pygame.display.update()"""



LEFT = 0
DOWN = 1
UP = 2
RIGHT = 3
clock = pygame.time.Clock()
my_direction = LEFT
pygame.init()
screen = pygame.display.set_mode((600, 600))


wall_x= [(590, 200)]
wall_skin_x = pygame.Surface((10, 10))
wall_skin_x.fill((255,255,255))

wall_y= [(0, 200)]
wall_skin_y = pygame.Surface((10, 10))
wall_skin_y.fill((255,255,255))

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #White






while True:
    clock.tick(10)
    

    for i in range(len(snake) - 1, 0, -1):
        if snake[i][0] == 0:
            snake [0] = (590, snake[0][1])
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
            
            


    # Actually make the snake move.
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    
    screen.fill((0,0,0))
 
    


    
    for pos in snake:
        screen.blit(snake_skin,pos)

    for pos in wall_y:
        screen.blit(wall_skin_y,pos)

    for pos in wall_x:
        screen.blit(wall_skin_x,pos)
    pygame.display.update()
