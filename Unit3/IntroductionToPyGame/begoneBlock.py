#BEGONE BLOCK!

#Copy this code into your VS Code and run it. Figure out how it playes
#Read the code below, understand it, add worthwhile and meaningful comments to all classes, functions, and anywhere else you deem important (minimum of 10 new comments)
#Change AT LEAST 5 (FIVE) things about the game

import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
PADDLE_SPEED = 10
BALL_RADIUS = 10
BALL_SPEED = 5
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_COLOR = (255, 0, 0)
PADDLE_COLOR = (0, 255, 0)
BALL_COLOR = (0, 0, 255)
BG_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BEGONE BLOCK!")

clock = pygame.time.Clock()

# Define the paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(PADDLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PADDLE_SPEED
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = -BALL_SPEED

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1

# Define the brick
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(BRICK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Create groups
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# Create paddle
paddle = Paddle()
all_sprites.add(paddle)

# Create ball
ball = Ball()
all_sprites.add(ball)

# Create bricks
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = Brick(col * (BRICK_WIDTH + 2), row * (BRICK_HEIGHT + 2))
        bricks.add(brick)
        all_sprites.add(brick)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for collisions
    collisions = pygame.sprite.spritecollide(ball, bricks, True)
    if collisions:
        ball.dy *= -1

    # Check for collisions with paddle
    if pygame.sprite.collide_rect(ball, paddle):
        ball.dy *= -1

    # Ball out of bounds
    if ball.rect.bottom >= HEIGHT:
        # Game over condition
        running = False

    # Update sprites
    all_sprites.update()

    # Clear screen
    screen.fill(BG_COLOR)

    # Draw sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
