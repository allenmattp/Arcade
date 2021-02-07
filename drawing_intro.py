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
    screen.fill(WHITE)
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x, y], [x + 5, y], 5)

    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, BLACK, [x_offset, 100], [x_offset - 10, 90], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset - 10, 100], 2)

    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    pygame.draw.arc(screen, GREEN, [100, 100, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLACK, [100, 100, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, RED, [100, 100, 250, 200], 3 * PI / 2, 2 * PI, 2)
    pygame.draw.arc(screen, BLUE, [100, 100, 250, 200], PI, 3 * PI / 2, 2)

    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = font.render("My text", True, BLACK)

    # Put the image of the text on the screen at 250x250
    screen.blit(text, [250, 250])

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()