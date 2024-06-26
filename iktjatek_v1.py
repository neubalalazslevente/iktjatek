import pygame
import random

pygame.init()

#functions
def getBiggestScore():
    try:
        with open("./score.txt", "r") as file:
            content = file.read()
            return int(content)
    except FileNotFoundError:
        print("A fájl nem található.")
    except IOError:
        print("Hiba történt a fájl olvasása közben.")

def changeBiggestScore(newScore):
    try:
        with open("./score.txt", "w", encoding="utf-8") as file:
            print(newScore, file=file)
    except FileNotFoundError:
        print("A fájl nem található.")
    except IOError:
        print("Hiba történt a fájl olvasása közben.")      

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
enemy_max_size = 110
enemy_size_multipier = 1.1
enemy_velocity_multipier = 1.03
enemy_velocity = 4
spawn = False

startmsg_display = True

loosemsg_display = False

score = 0
score_display = True

biggest_score = getBiggestScore()
biggest_score_display = True

player_biggest_score = 0
player_biggest_score_display = False

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
    enemy = pygame.draw.rect(screen, "red", [enemy_posX, enemy_posY, int(enemy_size), int(enemy_size)])
    #messages
    startmsg = font.render("A játék indításához használd a SPACE gombot!", True, "white")
    startmsg_rect = startmsg.get_rect()
    startmsg_rect.center = (WIDTH // 2, HEIGHT // 2)
    if startmsg_display == True:
        screen.blit(startmsg, startmsg_rect)

    loosemsg = font.render("Vesztettél!", True, "red")
    loosemsg_rect = loosemsg.get_rect()
    loosemsg_rect.center = (WIDTH // 2, HEIGHT // 2)

    score_message = font.render(f"Pontszámod: {str(score)}", True, "white")
    score_message_rect = score_message.get_rect()
    score_message_rect.inflate_ip(-20, -20)
    screen.blit(score_message, score_message_rect)

    biggest_score_message = font.render(f"Legnagyobb pontszám: {str(biggest_score)}", True, "white")
    biggest_score_rect = biggest_score_message.get_rect()
    biggest_score_rect.inflate_ip(-1000, -20)
    screen.blit(biggest_score_message, biggest_score_rect)

    # EVENTS
    # billentyűzet
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

    # sebesség
    if spawn == True:
        startmsg_display = False
        enemy_posX -= enemy_velocity
    
    # enemy újra teleportál
    if enemy_posX < -enemy_size:
        enemy_posX = 800
        score += 1
        enemy_velocity = enemy_velocity * enemy_velocity_multipier
        if enemy_size < enemy_max_size:
            enemy_size = enemy_size * enemy_size_multipier
        enemy_posY = random.randint(60, 350 - int(enemy_size))

    # player halál
    if (enemy_posX < player_posX + 20 and enemy_posX + enemy_size > player_posX and enemy_posY < player_posY + 20 and enemy_posY + enemy_size > player_posY):
        spawn = False
        loosemsg_display = True
        pygame.event.set_blocked(pygame.KEYDOWN)
        player_biggest_score = score

        if player_biggest_score > biggest_score:
            changeBiggestScore(player_biggest_score)

    if loosemsg_display:
        screen.blit(loosemsg, loosemsg_rect)
    
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
