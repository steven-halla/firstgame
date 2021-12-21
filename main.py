import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('spaceBackGround.jpg')

pygame.display.set_caption("first game")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_Change = 2
enemyY_Change = 40

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 10
bullet_state = "ready"


def draw_player(x, y):
    screen.blit(playerImg, (x, y))


def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -2.9

            if event.key == pygame.K_RIGHT:
                playerX_Change = 2.9

            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    #setting up boundries for enemy and player
    playerX += playerX_Change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_Change

    if enemyX <= 0:
        enemyX_Change = 2
        enemyY += enemyY_Change
    elif enemyX >= 736:
        enemyX_Change = -2
        enemyY += enemyY_Change


    screen.fill((0, 0, 0))



    screen.blit(background, (0, 0))

    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    draw_player(playerX, playerY)
    draw_enemy(enemyX, enemyY)
    pygame.display.update()
