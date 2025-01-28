import pygame  # Import Pygame

# Initialize Pygame and the font system
pygame.init()
pygame.font.init()

# Constants
WINDOW_SIZE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHAPE_WIDTH = 10
font = pygame.font.Font(None, 200)

# Create a window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI TicTacToe")

# drawing the lines for the tuc tac toe board
def drawBoard():
    # vertical lines
    pygame.draw.line(screen, BLACK, (WINDOW_SIZE / 3, 0), (WINDOW_SIZE / 3, WINDOW_SIZE), SHAPE_WIDTH)
    pygame.draw.line(screen, BLACK, ((WINDOW_SIZE / 3) * 2, 0), ((WINDOW_SIZE / 3) * 2, WINDOW_SIZE), SHAPE_WIDTH)

    # horizontal lines
    pygame.draw.line(screen, BLACK, (0, WINDOW_SIZE / 3), (WINDOW_SIZE, WINDOW_SIZE / 3), SHAPE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, (WINDOW_SIZE / 3) * 2), (WINDOW_SIZE, (WINDOW_SIZE / 3) * 2), SHAPE_WIDTH)


def squareLocation(squareNum):
    # determining based on which square the user/ai selected, where the center of the x/o will be
    # board looks like:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    if squareNum == 0:
        return (WINDOW_SIZE / 6, WINDOW_SIZE / 6)
    elif squareNum == 1:
        return (WINDOW_SIZE / 2, WINDOW_SIZE / 6)
    elif squareNum == 2:
        return ((WINDOW_SIZE / 6) * 5, WINDOW_SIZE / 6)
    elif squareNum == 3:
        return (WINDOW_SIZE / 6, WINDOW_SIZE / 2)
    elif squareNum == 4:
        return (WINDOW_SIZE / 2, WINDOW_SIZE / 2)
    elif squareNum == 5:
        return ((WINDOW_SIZE / 6) * 5, WINDOW_SIZE / 2)
    elif squareNum == 6:
        return (WINDOW_SIZE / 6, (WINDOW_SIZE / 6) * 5)
    elif squareNum == 7:
        return (WINDOW_SIZE / 2, (WINDOW_SIZE / 6) * 5)
    elif squareNum == 8:
        return ((WINDOW_SIZE / 6) * 5, (WINDOW_SIZE / 6) * 5)


def drawO(squareNum):
    # Render the text (create a surface with the letter "X")
    text = font.render('O', True, BLACK)

    # Get the rectangle of the text and center it
    text_rect = text.get_rect(center=(squareLocation(squareNum)))

    # Draw the text on the screen
    screen.blit(text, text_rect)


def drawX(squareNum):
    # Render the text (create a surface with the letter "X")
    text = font.render('X', True, BLACK)

    # Get the rectangle of the text and center it
    text_rect = text.get_rect(center=(squareLocation(squareNum)))

    # Draw the text on the screen
    screen.blit(text, text_rect)


# Game loop
running = True
while running:
    for event in pygame.event.get():  # Get all events
        if event.type == pygame.QUIT:  # Check for window close event
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # drawing game board lines
    drawBoard()
    drawO(4)
    drawX(1)

    pygame.display.update()

# Quit Pygame
pygame.quit()
