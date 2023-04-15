import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the player
player_width = 50
player_height = 50
player_x = (screen_width - player_width) / 2
player_y = (screen_height - player_height) / 2
player_speed = 5

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(0, screen_height - enemy_height)
enemy_speed = 1

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    elif keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    elif keys[pygame.K_DOWN] and player_y < screen_height - player_height:
        player_y += player_speed

    # Handle enemy movement
    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed

    # Handle collisions
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x \
            and player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        game_over = True

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, BLUE, (enemy_x, enemy_y, enemy_width, enemy_height))
    pygame.display.update()

    # Wait for the next frame
    clock.tick(60)

# Clean up and quit
pygame.quit()
