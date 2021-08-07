import pygame 
import time
import random
#Trying to pacakge the .py as a .exe
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.init()

eat_sound_url = resource_path("Assets\Sounds\Eat_Sound.wav")

well_done_sound_url = resource_path("Assets\Sounds\Well_Done_Sound.wav")

eat_sound = pygame.mixer.Sound(eat_sound_url)
well_done_sound = pygame.mixer.Sound(well_done_sound_url)


basic_url = resource_path("Assets\Images\Food\Test-Basic pellet.png")
apple_url = resource_path("Assets\Images\Food\Apple.png")
orange_url = resource_path("Assets\Images\Food\Orange.png")

basic = pygame.image.load(basic_url)
apple = pygame.image.load(apple_url)
orange = pygame.image.load(orange_url)

food = [basic,apple,orange]

colours = {
    "white" : (255,255,255),
    "black" : (0,0,0),
    "cyan" : (100,255,255),
    "red" : (200,50,50),
    "gold" : (255,240,0)
}

dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Python')
 
clock = pygame.time.Clock()

snake_block = 10 
 
font_style = pygame.font.SysFont("bahnschrift", 25) 
score_font = pygame.font.SysFont("century", 35)
Hscore_font = pygame.font.SysFont("century", 15)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, colours["white"])
    dis.blit(value, [0, 0])


Hscore = 0
def High_score(score):
    value = Hscore_font.render("Your High-Score: " + str(score), True, colours["gold"])
    dis.blit(value, [450, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, colours["white"], [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = font_style.render(msg,True, color) 
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) 

def gameLoop():
    global Hscore

    game_close = False
    game_over = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []

    Length_of_snake = 1
    snake_speed = 10

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0


    while not game_close:

        while game_over == True:
            message("You Lost! Press R-Retry or Q-Quit", colours["red"])

            pygame.display.update() 
 
            for event in pygame.event.get():                 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        game_close = True
                        game_over = False                    
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_close = True
                elif event.key == pygame.K_r:
                    gameLoop()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if x1_change == snake_block and Length_of_snake !=1:
                        pass
                    else:
                        x1_change = -snake_block
                        y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if x1_change == -snake_block and Length_of_snake !=1:
                        pass
                    else:
                        x1_change = snake_block
                        y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if y1_change == snake_block and Length_of_snake !=1:
                        pass
                    else:
                        y1_change = -snake_block
                        x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if y1_change == -snake_block and Length_of_snake !=1:
                        pass
                    else:
                        y1_change = snake_block
                        x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
  
        x1 += x1_change
        y1 += y1_change

        dis.fill(colours["black"])

        if (Length_of_snake - 1) < 10:
            dis.blit(food[0],[foodx,foody,snake_block,snake_block])
        elif (Length_of_snake - 1) < 20:
            dis.blit(food[1],[foodx,foody,snake_block,snake_block]) 
        elif (Length_of_snake - 1) <= 30:
            dis.blit(food[2],[foodx,foody,snake_block,snake_block]) 

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]: 
            if x == snake_Head:
                game_over = True
 
        our_snake(snake_block, snake_List)
        score = Length_of_snake - 1
        Your_score(score)
        if score > Hscore:
            Hscore = score
        else:
            pass
        High_score(Hscore)

 
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            snake_speed += 0.5
            Length_of_snake += 1

            if (Length_of_snake - 1) % 10 == 0 and (Length_of_snake - 1) != 0:
                well_done_sound.play()
            elif (Length_of_snake - 1) >= 30:
                well_done_sound.play()
            else:
                eat_sound.play()

        clock.tick(snake_speed)
        
    pygame.quit()
 
 
gameLoop()