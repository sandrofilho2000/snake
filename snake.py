##### 10 - Game over ####
import pygame, random
from pygame.locals import *

# Helper functions
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Macro definition for snake movement.
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
STOP = 4
wall_y= [(300, 300), (300, 220), (300, 160)]
wall_skin_y = pygame.Surface((10, 80))
wall_skin_y.fill((255,255,255))

wall_x= [(330, 260), (250, 260), (190, 260)]
wall_skin_x = pygame.Surface((80, 10))
wall_skin_x.fill((255,255,255))

wall= wall_skin_y, wall_skin_x
print(wall)
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,255,0)) #White


andar = False
    

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = STOP

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0
speed = 10
cont = 0

game_over = False
while not game_over:
 
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            andar = True
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
              
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
                
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
                
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
                

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        score = score + 1
        cont += 1
        if speed <= 26:
            if cont == 4:
                speed += 3
                cont = 0
    if score > 0:
        for i in range(1, len(snake) - 1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                game_over = True
                break

    if snake[0] in wall:
        game_over = True
        break

    if game_over:
        break
 

    for i in range(len(snake) - 1, 0, -1):
        
        if my_direction == RIGHT or my_direction == DOWN:
            if snake[1][0] > 590:
                snake [0] = (0, snake[0][1])
                
            if snake[0][1] > 590:
                snake [0] = (snake[1][0], 10)
      
        if my_direction == LEFT or my_direction == UP: 
            if snake[1][0] == 0:
                snake [0] = (590, snake[0][1])
        
            if snake[0][1] == 0:
                snake [0] = (snake[1][0], 590)

        snake[i] = (snake[i-1][0], snake[i-1][1])
        
        
    # Actually make the snake move.
    if andar:
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    
    for x in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10): # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in snake:
        screen.blit(snake_skin,pos)

    for pos in wall_y:
        screen.blit(wall_skin_y,pos)

    for pos in wall_x:
        screen.blit(wall_skin_x,pos)
    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()














