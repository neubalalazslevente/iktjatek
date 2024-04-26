import pygame
import random

pygame.init()

# constants
white = (0,0,0)
black = (255, 255, 255)
green = (0,255,0)
WIDTH = 750
HEIGHT = 400

# game variables
score = 0
player_posX = 50
player_posY = 190
enemy_posX = 800
enemy_posY = 200
enemy_size = 50
spawn = False
loosemsg_display = False

# setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ikt game")
background = black
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)

running = True


# game
while running:
    timer.tick(fps)
    screen.fill("black")
    border_top = pygame.draw.rect(screen, "white", [0, 55, WIDTH, 5])
    border_bottom = pygame.draw.rect(screen, "white", [0, 350, WIDTH, 5])
    player = pygame.draw.rect(screen, "green", [player_posX, player_posY, 20, 20])
    enemy = pygame.draw.rect(screen, "red", [enemy_posX, enemy_posY, enemy_size, enemy_size])
    loosemsg = font.render("You Loose!", True, "red")
    loosemsg_rect = loosemsg.get_rect()
    loosemsg_rect.center = (WIDTH // 2, HEIGHT // 2)


    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spawn = True
            if event.key == pygame.K_UP and player_posY > 60:
                player_posY -= 10
            if event.key == pygame.K_DOWN and player_posY < 325:
                player_posY += 10

    if spawn == True:
        enemy_posX -= 4
    
    if enemy_posX < -enemy_size:
        enemy_posY = random.randint(55, 350 - enemy_size)
        enemy_posX = 800

    if (enemy_posX < player_posX + 20 and enemy_posX + enemy_size > player_posX and enemy_posY < player_posY + 20 and enemy_posY + enemy_size > player_posY):
        spawn = False
        loosemsg_display = True
        pygame.event.set_blocked(pygame.KEYDOWN)

    if loosemsg_display:
        screen.blit(loosemsg, loosemsg_rect)
    
    pygame.display.flip()
    pygame.display.update()
pygame.quit()