import pygame




pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("first game")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player(x,y):
    screen.blit(playerImg, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB
    screen.fill((0, 0, 0))

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("left arrow is pressed")

        if event.key == pygame.K_RIGHT:
            print("right arrow is pressed")

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("key is no longer being pressed")


    player(playerX, playerY)
    pygame.display.update()