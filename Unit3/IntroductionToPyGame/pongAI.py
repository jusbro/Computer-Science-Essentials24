import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong AI")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game constants
BALL_SPEED = 5
PADDLE_SPEED = 7
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Define the paddles
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, HEIGHT // 2)

    def move_up(self):
        self.rect.y -= PADDLE_SPEED
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.y += PADDLE_SPEED
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Define the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, BLACK, (BALL_SIZE // 2, BALL_SIZE // 2), BALL_SIZE // 2)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = BALL_SPEED * random.choice([1, -1])
        self.dy = BALL_SPEED * random.choice([1, -1])

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

# Create sprites
all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()

player_paddle = Paddle(50)
ai_paddle = Paddle(WIDTH - 50)
ball = Ball()

all_sprites.add(player_paddle, ai_paddle, ball)
paddles.add(player_paddle, ai_paddle)
ball_sprites.add(ball)

clock = pygame.time.Clock()

# Score counters
player_score = 0
ai_score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.move_up()
    if keys[pygame.K_s]:
        player_paddle.move_down()

    # AI controls
    if ball.rect.centery < ai_paddle.rect.centery:
        ai_paddle.move_up()
    elif ball.rect.centery > ai_paddle.rect.centery:
        ai_paddle.move_down()

    # Ball and paddle collision
    if pygame.sprite.spritecollide(player_paddle, ball_sprites, False):
        ball.dx *= -1
        player_score += 1
    elif pygame.sprite.spritecollide(ai_paddle, ball_sprites, False):
        ball.dx *= -1
        ai_score += 1

    # Ball goes out of bounds
    if ball.rect.left <= 0:
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        ball.dx *= random.choice([1, -1])
        ai_score += 1
    elif ball.rect.right >= WIDTH:
        ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        ball.dx *= random.choice([1, -1])
        player_score += 1

    # Update sprites
    all_sprites.update()

    # Clear the screen
    SCREEN.fill(BLACK)

    # Draw sprites
    all_sprites.draw(SCREEN)

    # Display scores
    player_text = font.render("Player: " + str(player_score), True, WHITE)
    ai_text = font.render("AI: " + str(ai_score), True, WHITE)
    SCREEN.blit(player_text, (20, 20))
    SCREEN.blit(ai_text, (WIDTH - ai_text.get_width() - 20, 20))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
