import pygame

# position (x, y)
# velocity (x, y)
# acceleration (x, y)

# max_velocity_walk = 16
# max_velocity_run = 32
# acceleration_walk = 4
# acceleration_run = 8


# is_walking = is_key_pressed(DPAD_LEFT) || is_key_pressed(DPAD_RIGHT)
# is_running = is_key_pressed(RUN_BUTTON) && is_walking


# set acceleration based on walking vs running
# if is_running:
#     acceleration.x = acceleration_run
# elif is_walking:
#     acceleration.x = acceleration_walk
# else:
#     acceleration.x = 0


# finally add acceleration to velocity.
# velocity.x = velocity.x + acceleration.x


# we've added the acceleration to velocity, now lets make sure velocity stays
# within range of -max velocity and max velocity. different based on walking vs run
# if is_running:
#     if velocity.x > max_velocity_run:
#         velocity.x = max_velocity_run
#     elif velocity.x < -max_velocity_run:
#         velocity.x = -max_velocity_run
# elif is_walking:
#     if velocity.x > max_velocity_walk:
#         velocity.x = max_velocity_walk
#     elif velocity.x < -max_velocity_walk:
#         velocity.x = -max_velocity_walk

# position.x = position.x + velocity.x


pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("first game")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #RGB
    screen.fill((0, 0, 0))

    player()
    pygame.display.update()