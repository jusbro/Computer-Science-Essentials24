#Imperialist Invaders From Not This Planet

#Copy this code into your VS Code and run it. Figure out how it playes
#Read the code below, understand it, add worthwhile and meaningful comments to all functions, and anywhere else you deem important (minimum of 10 new comments)
#Change AT LEAST 5 (FIVE) things about the game

import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Imperialist Invaders From Not This Planet")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player variables
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Enemy variables
enemy_width = 50
enemy_height = 50
enemy_radius = 25
enemy_speed = 3
enemies = []

# Bullet variables
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Create enemies
def create_enemies():
    for row in range(5):
        for col in range(10):
            enemy_x = col * 70 + 50
            enemy_y = row * 50 + 50
            enemies.append([enemy_x, enemy_y])

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

def draw_enemy(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), enemy_radius)

def draw_bullet(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, bullet_width, bullet_height))

# Game loop
running = True
clock = pygame.time.Clock()

create_enemies()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Move enemies
    for enemy in enemies:
        enemy[0] += enemy_speed
        if enemy[0] >= SCREEN_WIDTH - enemy_width or enemy[0] <= 0:
            enemy_speed *= -1
            for e in enemies:
                e[1] += 10
        if enemy[1] >= SCREEN_HEIGHT:  # Check if any enemy has reached the bottom of the screen
            running = False

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Check for collisions
    bullets_copy = bullets[:]  # Create a copy of the bullets list
    for bullet in bullets_copy:  # Iterate over the copy
        for enemy in enemies:
            if bullet[1] <= enemy[1] + enemy_height and bullet[0] >= enemy[0] and bullet[0] <= enemy[0] + enemy_width:
                bullets.remove(bullet)  # Remove from original list
                enemies.remove(enemy)
                break  # Break the inner loop since the bullet has already been removed

    # Draw player, enemies, and bullets
    draw_player(player_x, player_y)
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
