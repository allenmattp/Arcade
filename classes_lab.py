"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import random

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)

# Classes
class Rectange():
    def __init__(self):
        self.x = random.randrange(0, 700)
        self.y = random.randrange(0, 500)
        self.h = random.randrange(20, 70)
        self.w = random.randrange(20, 70)

        self.change_x = random.randrange(-3,4)
        self.change_y = random.randrange(-3,4)

    def draw(self, screen):
        color = (random.randrange(0,256), random.randrange(0, 256), random.randrange(0, 256))
        pygame.draw.rect(screen, color, [self.x, self.y, self.w, self.h])

    def move(self):
        self.x += self.change_x
        if self.x < 0 or self.x > (700 - self.w):
            self.change_x *= -1
        self.y += self.change_y
        if self.y < 0 or self.y > (500 - self.h):
            self.change_y *= -1

class Ellipse(Rectange):
    def __init__(self):
        super().__init__()
    
    def draw(self, screen, color):
        pygame.draw.ellipse(screen, color, [self.x, self.y, self.w, self.h])
        
    def move(self):
        super().move()



def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    my_list = []
    my_list_ellipse = []
    colors = []

    for i in range(100):
        color = (random.randrange(0,256), random.randrange(0, 256), random.randrange(0, 256))
        colors.append(color)

    for i in range(random.randrange(0,100)):
        my_object = Rectange()
        my_list.append(my_object)

    for i in range(random.randrange(0,100)):
        my_ellipse = Ellipse()
        my_list_ellipse.append(my_ellipse)

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        for rect in my_list:
            rect.draw(screen)
            rect.move()

        color_count = 0
        for el in my_list_ellipse:
            el.draw(screen, colors[color_count])
            color_count += 1
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == "__main__":
    main()