#Floppy Burd

#Copy this code into your VS Code and run it. Figure out how it plays
#Read the code below, understand it, add worthwhile and meaningful comments to all functions and anywhere else you deem important (minimum of 10 new comments)
#Change AT LEAST 5 (FIVE) things about the game

import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floppy Burd")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.25
jump_strength = -5

pipe_width = 50
pipe_gap = 150
pipe_velocity = 3
pipes = []

score = 0
font = pygame.font.Font(None, 36)

def draw_bird(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), bird_radius)

def draw_pipe(x, y, height):
    pygame.draw.rect(screen, WHITE, (x, 0, pipe_width, y))
    pygame.draw.rect(screen, WHITE, (x, y + pipe_gap, pipe_width, SCREEN_HEIGHT - y - pipe_gap))

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

def check_collision():
    if bird_y > SCREEN_HEIGHT or bird_y < 0:
        return True
    for pipe in pipes:
        if bird_x + bird_radius > pipe[0] and bird_x - bird_radius < pipe[0] + pipe_width:
            if bird_y - bird_radius < pipe[1] or bird_y + bird_radius > pipe[1] + pipe_gap:
                return True
    return False

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Update bird position
    bird_velocity += gravity
    bird_y += bird_velocity

    # Generate pipes
    if len(pipes) == 0 or pipes[-1][0] < SCREEN_WIDTH - 200:
        pipe_height = random.randint(50, 300)
        pipes.append((SCREEN_WIDTH, pipe_height))

    # Move pipes
    for i, pipe in enumerate(pipes):
        pipes[i] = (pipe[0] - pipe_velocity, pipe[1])

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe[0] + pipe_width > 0]

    # Check for collision
    if check_collision():
        running = False

    # Check for score
    if pipes[0][0] + pipe_width < bird_x - bird_radius:
        score += 1
        pipes.pop(0)

    # Clear screen
    screen.fill(BLACK)

    # Draw pipes
    for pipe in pipes:
        draw_pipe(pipe[0], pipe[1], pipe_gap)

    # Draw bird
    draw_bird(bird_x, int(bird_y))

    # Display score
    display_score(score)

    # Update display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
