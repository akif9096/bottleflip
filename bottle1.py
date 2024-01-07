import pygame
import random
import sys
import os
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BOTTLE_WIDTH, BOTTLE_HEIGHT = 50, 100
FPS = 60
GRAVITY = 0.5

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Bottle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.color = GREEN  # Initial color
        self.image = pygame.Surface((BOTTLE_WIDTH, BOTTLE_HEIGHT))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 0
        self.flipped = False

    def update(self):
        if not self.flipped:
            self.velocity += GRAVITY
            self.rect.y += self.velocity

            if self.rect.y > HEIGHT - BOTTLE_HEIGHT:
                self.rect.y = HEIGHT - BOTTLE_HEIGHT
                self.velocity = 0
        else:
            # Randomly set the color to RED or GREEN
            self.color = random.choice([RED, GREEN])
            self.image.fill(self.color)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bottle Flip Game")
clock = pygame.time.Clock()

# Create a group for sprites
all_sprites = pygame.sprite.Group()

# Create a bottle
bottle = Bottle(WIDTH // 2 - BOTTLE_WIDTH // 2, HEIGHT - BOTTLE_HEIGHT)
all_sprites.add(bottle)

# Create a retry button at the top
retry_button = pygame.Rect(300, 20, 200, 50)
retry_color = (150, 150, 150)

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not bottle.flipped:
            # Flip the bottle on space key press
            bottle.velocity = -15
            bottle.flipped = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the retry button is clicked
            if retry_button.collidepoint(event.pos):
                bottle.flipped = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Draw retry button
    pygame.draw.rect(screen, retry_color, retry_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Retry", True, WHITE)
    screen.blit(text, (retry_button.x + 70, retry_button.y + 15))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
