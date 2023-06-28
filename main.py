import pygame
from random import randint
def drawFood():
    food_color = pygame.Color(210,45,60)
    food_rect = pygame.Rect((food[0]*tile_w, food[1]*tile_h),(tile_w,tile_w))
    pygame.draw.rect(wind,food_color,food_rect)

def drawSnake():
    snake_color = pygame.Color(60,215,60)
    for cell in snake:
        cell_rect = pygame.Rect((cell[0]*tile_w, cell[1]*tile_h),(tile_w,tile_w))
        pygame.draw.rect(wind, snake_color,cell_rect)

def updateSnake(direction):
    global food
    dirX, dirY = direction
    head = snake[0].copy()
    head[0] = (head[0]+dirX)
    head[1] = (head[1]+dirY)
    if head[0] >=  tiles_x or head[0] < 0:
        print("Tu as rencontré un mur !")
        return False
    if head[1] >= tiles_y or head[1] < 0:
        print("Tu as rencontré un mur !")
        return False
    if head in snake[1:]:
        print("Tu t'es mordu la queue !")
        return False
    elif head == food:
        food = None
        while food is None:
            newfood = [
            randint(0, tiles_x-1),
            randint(0, tiles_y-1)
            ]
            food = newfood if newfood not in snake else None
    else:
        snake.pop()

    snake.insert(0,head)
    return True

#Init Window
sw = 640
sh = 480
wind = pygame.display.set_mode((sw,sh))

bg_color = pygame.Color(22,41,85)

## Define the tales
tiles_x = 32
tiles_y = 24

tile_w = sw // tiles_x
tile_h = sh // tiles_y

## Define the snake
snake_x, snake_y = tiles_x // 4, tiles_y // 2
snake = [
        [snake_x,snake_y],
        [snake_x-1,snake_y],
        [snake_x-2,snake_y]
]

## Define the food
food = [tiles_x//2, tiles_y//2]

## Game
running = True
direction = [1,0]
while running:
    pygame.time.Clock().tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_d and not direction == [-1,0]: # D key RIGHT
                direction = [1,0]
            if event.key == pygame.K_q and not direction == [1,0]: # Q key LEFT
                direction = [-1,0]
            if event.key == pygame.K_z and not direction == [0,1]: # Z key UP
                direction = [0,-1]
            if event.key == pygame.K_s and not direction == [0,-1]: # S key DOWN
                direction = [0,1]

    # Update
    if(updateSnake(direction)) == False:
        print("Game Over")
        running = False

    wind.fill(bg_color)

    drawFood()
    drawSnake()
    pygame.display.update()

pygame.quit()