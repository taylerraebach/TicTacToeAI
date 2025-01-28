import pygame  # Import Pygame

# Constants
WINDOW_SIZE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI TicTacToe")

# drawing the lines for the tuc tac toe board
def drawBoard():
    # vertical lines
    pygame.draw.line(screen, BLACK, (WINDOW_SIZE / 3, 0), (WINDOW_SIZE / 3, WINDOW_SIZE), 5)
    pygame.draw.line(screen, BLACK, ((WINDOW_SIZE / 3) * 2, 0), ((WINDOW_SIZE / 3) * 2, WINDOW_SIZE), 5)

    # horizontal lines
    pygame.draw.line(screen, BLACK, (0, WINDOW_SIZE / 3), (WINDOW_SIZE, WINDOW_SIZE / 3), 5)
    pygame.draw.line(screen, BLACK, (0, (WINDOW_SIZE / 3) * 2), (WINDOW_SIZE, (WINDOW_SIZE / 3) * 2), 5)


# Game loop
running = True
while running:
    for event in pygame.event.get():  # Get all events
        if event.type == pygame.QUIT:  # Check for window close event
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # drawing tic tac toe lines
    drawBoard()

    pygame.display.update()

# Quit Pygame
pygame.quit()
