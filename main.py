import pygame
from player import Player

W_WIDTH = 800
W_HEIGHT = 600

pygame.init()

race_font = pygame.font.Font("fonts/BebasNeue-Regular.ttf",32)

DISPLAY = pygame.display.set_mode((W_WIDTH,W_HEIGHT))
pygame.display.set_caption("Racing Game!")

player = Player(DISPLAY,6,1,"images/f1car.png",(30,25))



is_running = True
has_fastest_time = False
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            has_fastest_time = True
            fastest_time = pygame.time.get_ticks()/1000
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.turn(True)
            elif event.key == pygame.K_d:
                player.turn(False)
    DISPLAY.fill((25,255,25))

    player.update()

    time = race_font.render(f"Time:{pygame.time.get_ticks()/1000}",False,(255,255,255),None)
    DISPLAY.blit(time,(0,50))

    if has_fastest_time:
        fastest_text = race_font.render(f"Fastest Time:{fastest_time}",False,(255,0,0),(0,0,0))
        DISPLAY.blit(fastest_text,(0,100))
 

    pygame.display.update()