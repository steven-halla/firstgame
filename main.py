import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

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


def draw_player(x, y):
    screen.blit(playerImg, (x, y))


def draw_enemy(x, y):
    screen.blit(enemyImg, (x, y))


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
    draw_player(playerX, playerY)
    draw_enemy(enemyX, enemyY)
    pygame.display.update()
