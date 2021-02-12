import pygame
import random

# Color List
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):
    """
    Class for ball.
    Derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor: pass in color and x/y position
        """

        # Call the parent class
        super().__init__()

        # Create an image of the block and fill with a color
        # Can also be an image
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch rect that has dimensions of the image

        # Update position of this object by setting values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def reset_pos(self):
        """ Reset position to the top of the screen at random x location.
        Called by update() or main program loop if collision.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(0, screen_width)

    def update(self):
        """ Called each frame."""

        # Move block down one pixel
        self.rect.y += 1
        if self.rect.y > screen_height:
            self.reset_pos()

# Initialize Pygame
pygame.init()

# Set height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# List of Sprites.
# Each block in program is added to this list.
# List is managed by class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite:
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)

# Loop until user closes window
done = False

# Manage how fast screen updates
clock = pygame.time.Clock()

# Hide mouse cursor
pygame.mouse.set_visible(0)

score = 0

# -------- Main Program Loop ---------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(WHITE)

    # Get current position of mouse
    pos = pygame.mouse.get_pos()

    # Fetch the x/y coordinates
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # Call update() method for all blocks in block_list
    block_list.update()

    # Check if player blocks has collided with other blocks
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    # Check the list of collisions
    for block in blocks_hit_list:
        score += 1
        print(score)

        block.reset_pos()
        if score == 100:
            print("C O N G R A T U L A T I O N S")
            done = True

    # Draw all sprites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Update screen
    pygame.display.flip()

pygame.quit()