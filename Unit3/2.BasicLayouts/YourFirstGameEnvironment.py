#Your First Game Environment

#In this activity, you will run a Pygame environment where you controll an object with WASD keys on the keyboard
#This code works by default. As you work through the packet for this project, you will manipulate multiple parameters and observe how the game changes

#Below is a list of changes you will experiment with (FOLLOW ALONG IN YOUR PACKET)
#Screen Size
#Custom Colors
#Object Size
#Object Speed
#Object Shape
#Game Inputs (controls)


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Game")

# Colors
#Colors are defined by RGB (literally red, green, blue). Use the link below to learn RGB for any color
#https://htmlcolorcodes.com/color-picker/
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 5

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the ball
    if keys[pygame.K_w] and ball_y - ball_speed > 0:  # Check top boundary
        ball_y -= ball_speed
    if keys[pygame.K_s] and ball_y + ball_speed < HEIGHT:  # Check bottom boundary
        ball_y += ball_speed
    if keys[pygame.K_a] and ball_x - ball_speed > 0:  # Check left boundary
        ball_x -= ball_speed
    if keys[pygame.K_d] and ball_x + ball_speed < WIDTH:  # Check right boundary
        ball_x += ball_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
