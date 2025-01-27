"""
 Animating multiple objects using a list.
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/Gkhz3FuhGoI
"""

# Import a library of functions called 'pygame'
import pygame
import random
import math

clock = pygame.time.Clock()
# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GGRAY = [120, 163, 119]
BGREY = [119, 136, 163]
RGReY = [163, 119, 119]
RED = [255, 0, 0]
LNC = [207, 101, 1]
NC = [178, 88, 4]
BG = [227, 160, 27]

font = pygame.font.Font(None, 25)

# Set the height and width of the screen
SIZE = [400, 500]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("imke's game")

# Create an empty array
note_list = []

# Loop 50 times and add a snow flake in a random x,y position
for i in range(75):
    x = random.randrange(0, 400)
    y = random.randrange(0, 500)
    pygame.draw.square(screen, GGREY, [x, y], 4)
    pygame.draw.square(screen, BGREY, [x, y], 4)
    pygame.draw.square(screen, RGREY, [x, y], 4)
    #note_list.append([x, y])

clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False
while not done:

    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(BG)

    # Process each snow flake in the list
    for i in range(len(note_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, NC, note_list[i], 15)
        pygame.draw.circle(screen, LNC, note_list[i], 10)
        pygame.draw.line(screen, WHITE, [0,400], [400,400], 8)

        # Move the snow flake down one pixel
        note_list[i][1] += 9

        # If the snow flake has moved off the bottom of the screen
        if note_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            note_list[i][1] = y
            # Give it a new x position
            x = random.randrange(100, 350)
            note_list[i][0] = x
    #timer
    frame_count = 0
    frame_rate = 60
    start_time = 90
    total_seconds = frame_count // frame_rate

    # Divide by 60 to get total minutes
    minutes = total_seconds // 60

    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

    # Blit to the screen
    text = font.render(output_string, True, WHITE)
    screen.blit(text, [0, 25])

    # --- Timer going down ---
    # --- Timer going up ---
    # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 1


    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
del font
pygame.quit()
