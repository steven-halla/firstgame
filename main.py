import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("first game")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_Change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))


running = True

# RGB
screen.fill((0, 0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_Change = -.05

            if event.key == pygame.K_RIGHT:
                playerX_Change = .05

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change
    player(playerX, playerY)
    pygame.display.update()