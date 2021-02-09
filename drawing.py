"""
Pygame base template for opening a window, done with functions

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (169, 169, 169)

def draw_rect(screen, x, y):
    pygame.draw.rect(screen, BLACK, [x, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x+5, y+5, 40, 40])

def draw_cat(screen, x, y):
    pygame.draw.line(screen, BLACK, [0 + x, 0 + y], [25 + x, 50 + y], 2)
    pygame.draw.line(screen, BLACK, [0 + x, 0 + y], [50 + x, 25 + y], 2)
    pygame.draw.line(screen, BLACK, [100 + x, 0 + y], [25 + x, 50 + y], 2)
    pygame.draw.line(screen, BLACK, [100 + x, 0 + y], [75 + x, 50 + y], 2)
    pygame.draw.circle(screen, GREY, [50 + x, 50 + y], 35)
    pygame.draw.ellipse(screen, GREY, rect=[0 + x, 70 + y, 100, 200])

    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0

    # Current position
    x_coord = 10
    y_coord = 10

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

    # Hide the mouse cursor
    pygame.mouse.set_visible(0)

    # Count the joysticks the computer has
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        # No joysticks!
        print("Error, I didn't find any joysticks.")
    else:
        # Use joystick #0 and initialize it
        my_joystick = pygame.joystick.Joystick(0)
        my_joystick.init()

    # Speed in pixels per frame
    x_speed = 0
    y_speed = 0

    # Current position
    x_coord = 10
    y_coord = 10

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Was it an arrow? If yes adjust speed:
                if event.key == pygame.K_LEFT and x_coord >= 5:
                    x_speed = -3
                elif event.key == pygame.K_RIGHT and x_coord <= 645:
                    x_speed = 3
                elif event.key == pygame.K_UP and y_coord >= 5:
                    y_speed = -3
                elif event.key == pygame.K_DOWN and y_coord <= 445:
                    y_speed = 3
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_speed = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_speed = 0
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        # As long as there is a joystick
        if joystick_count != 0:
            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos = my_joystick.get_axis(0)
            vert_axis_pos = my_joystick.get_axis(1)

            # Move x according to the axis. We multiply by 10 to speed up the movement.
            # Convert to an integer because we can't draw at pixel 3.5, just 3 or 4.
            x_coord = x_coord + int(horiz_axis_pos * 10)
            y_coord = y_coord + int(vert_axis_pos * 10)

        # Move object according to keyboard input
        x_coord += x_speed
        y_coord += y_speed

        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        draw_rect(screen, x, y)
        draw_rect(screen, x_coord, y_coord)

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