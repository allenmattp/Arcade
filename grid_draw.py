import pygame
import math
# Initialize the game engine
pygame.init()

PI = math.pi

# Set colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE     = (   0,   0, 255)

# Open window
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sir Niles' Fuzzy Adventure")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

    # --- Game logic should go here


    # --- Drawing code should go here
    screen.fill(BLACK)

    from_left = 2.5
    width = 5
    from_top = 2.5
    height = 5

    for i in range(0, 500, 5):
        for j in range(0, 500, 5):
            pygame.draw.rect(screen, GREEN, [from_left+j*2, from_top, width, height])
        from_top += 10

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()