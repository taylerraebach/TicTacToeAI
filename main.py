import pygame  # Import Pygame

# Initialize Pygame and the font system
pygame.init()
pygame.font.init()

# Constants
WINDOW_SIZE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (222, 15, 81)
SHAPE_WIDTH = 10
font = pygame.font.Font(None, 200)

# Create a window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("AI TicTacToe")


#-----------------------------------------------------------------------------------------------------------------------
def drawBoard():
    # vertical lines
    pygame.draw.line(screen, BLACK, (WINDOW_SIZE / 3, 0), (WINDOW_SIZE / 3, WINDOW_SIZE), SHAPE_WIDTH)
    pygame.draw.line(screen, BLACK, ((WINDOW_SIZE / 3) * 2, 0), ((WINDOW_SIZE / 3) * 2, WINDOW_SIZE), SHAPE_WIDTH)

    # horizontal lines
    pygame.draw.line(screen, BLACK, (0, WINDOW_SIZE / 3), (WINDOW_SIZE, WINDOW_SIZE / 3), SHAPE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, (WINDOW_SIZE / 3) * 2), (WINDOW_SIZE, (WINDOW_SIZE / 3) * 2), SHAPE_WIDTH)


#-----------------------------------------------------------------------------------------------------------------------
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


#-----------------------------------------------------------------------------------------------------------------------
def decideSquareNum(x, y):
    # deciding based on click position, which square is it in
    # board looks like:
    # 0 1 2
    # 3 4 5
    # 6 7 8

    # if top row
    if(y < (WINDOW_SIZE / 3)):
        # if left column
        if (x < (WINDOW_SIZE / 3) ):
            return 0

        # if middle column
        elif (x < (WINDOW_SIZE / 3) * 2):
            return 1

        # if right column
        else:
            return 2

    # if middle row
    elif(y < ((WINDOW_SIZE / 3))*2):
        # if left column
        if (x < (WINDOW_SIZE / 3)):
            return 3

        # if middle column
        elif (x < (WINDOW_SIZE / 3) * 2):
            return 4

        # if right column
        else:
            return 5

    # if bottom row
    else:
        # if left column
        if (x < (WINDOW_SIZE / 3)):
            return 6

        # if middle column
        elif (x < (WINDOW_SIZE / 3) * 2):
            return 7

        # if right column
        else:
            return 8


#-----------------------------------------------------------------------------------------------------------------------
def drawO(aiMove):
    # Render the text (create a surface with the letter "X")
    text = font.render('O', True, BLACK)

    # Get the rectangle of the text and center it
    x, y = squareLocation(aiMove)
    text_rect = text.get_rect(center=(x, y))

    # Draw the text on the screen
    screen.blit(text, text_rect)


#-----------------------------------------------------------------------------------------------------------------------
def drawX(squareNum):
    # Render the text (create a surface with the letter "X")
    text = font.render('X', True, BLACK)

    # Get the rectangle of the text and center it
    x, y = squareLocation(squareNum)
    text_rect = text.get_rect(center=(x, y))

    # Draw the text on the screen
    screen.blit(text, text_rect)


#-----------------------------------------------------------------------------------------------------------------------
def AImoveDecision(listX, listO):

    allSquares = [0,1,2,3,4,5,6,7,8]
    availableSquares = [item for item in allSquares if item not in (listX + listO)]
    nextMove = 'None'

    # if user has two next to each other anywhere, block the move
    if len(listX) > 1:
        nextMove = checkForTwo(listX, availableSquares)

    if nextMove == 'None':
        nextMove = availableSquares.pop()

    return nextMove


#-----------------------------------------------------------------------------------------------------------------------
def checkForTwo(listX, availableSquares):
    # if user has two next to each other anywhere, block the move
    # board looks like:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    if 0 in availableSquares:
        if 1 and 2 in listX:
            return 0
        elif 3 and 6 in listX:
            return 0
        elif 4 and 8 in listX:
            return 0

    elif 1 in availableSquares:
        if 0 and 2 in listX:
            return 1
        elif 4 and 7 in listX:
            return 1

    elif 2 in availableSquares:
        if 0 and 1 in listX:
            return 2
        elif 5 and 8 in listX:
            return 2
        elif 4 and 6 in listX:
            return 2

    elif 3 in availableSquares:
        if 0 and 6 in listX:
            return 3
        elif 4 and 5 in listX:
            return 3

    elif 4 in availableSquares:
        if 0 and 8 in listX:
            return 4
        elif 2 and 6 in listX:
            return 4
        elif 3 and 5 in listX:
            return 4
        elif 1 and 7 in listX:
            return 4

    elif 5 in availableSquares:
        if 2 and 8 in listX:
            return 5
        elif 3 and 4 in listX:
            return 5

    elif 6 in availableSquares:
        if 0 and 3 in listX:
            return 6
        elif 7 and 8 in listX:
            return 6
        elif 2 and 4 in listX:
            return 6

    elif 7 in availableSquares:
        if 1 and 4 in listX:
            return 7
        if 6 and 8 in listX:
            return 7

    elif 8 in availableSquares:
        if 2 and 5 in listX:
            return 8
        elif 6 and 7 in listX:
            return 8
        elif 0 and 4 in listX:
            return 8


    else:
        return 'None'



#-----------------------------------------------------------------------------------------------------------------------
def checkWin(listX, listO):
    # deciding if a player has won
    # board looks like:
    # 0 1 2
    # 3 4 5
    # 6 7 8

    if all(x in listX for x in [0, 1, 2]):
        return ['win', 'x', 'top']
    elif all(x in listX for x in [3, 4, 5]):
        return ['win', 'x', 'middle']
    elif all(x in listX for x in [6, 7, 8]):
        return ['win', 'x', 'bottom']
    elif all(x in listX for x in [0, 3, 6]):
        return ['win', 'x', 'left']
    elif all(x in listX for x in [1, 4, 7]):
        return ['win', 'x', 'center']
    elif all(x in listX for x in [2, 5, 8]):
        return ['win', 'x', 'right']
    elif all(x in listX for x in [0, 4, 8]):
        return ['win', 'x', 'leftToRight']
    elif all(x in listX for x in [2, 4, 6]):
        return ['win', 'x', 'rightToLeft']

    if all(o in listO for o in [0, 1, 2]):
        return ['win', 'o', 'top']
    elif all(o in listO for o in [3, 4, 5]):
        return ['win', 'o', 'middle']
    elif all(o in listO for o in [6, 7, 8]):
        return ['win', 'o', 'bottom']
    elif all(o in listO for o in [0, 3, 6]):
        return ['win', 'o', 'left']
    elif all(o in listO for o in [1, 4, 7]):
        return ['win', 'o', 'center']
    elif all(o in listO for o in [2, 5, 8]):
        return ['win', 'o', 'right']
    elif all(o in listO for o in [0, 4, 8]):
        return ['win', 'o', 'leftToRight']
    elif all(o in listO for o in [2, 4, 6]):
        return ['win', 'o', 'rightToLeft']

    return ['noWin']


#-----------------------------------------------------------------------------------------------------------------------
def drawWinLine(winningLine):

    if winningLine == 'top':
        pygame.draw.line(screen, RED, (0, WINDOW_SIZE / 6), (WINDOW_SIZE, WINDOW_SIZE / 6), SHAPE_WIDTH)

    elif winningLine == 'middle':
        pygame.draw.line(screen, RED, (0, WINDOW_SIZE / 2), (WINDOW_SIZE, WINDOW_SIZE / 2), SHAPE_WIDTH)

    elif winningLine == 'bottom':
        pygame.draw.line(screen, RED, (0, (WINDOW_SIZE / 6) * 5), (WINDOW_SIZE, (WINDOW_SIZE / 6) * 5), SHAPE_WIDTH)

    elif winningLine == 'left':
        pygame.draw.line(screen, RED, (WINDOW_SIZE / 6, 0), (WINDOW_SIZE / 6, WINDOW_SIZE), SHAPE_WIDTH)

    elif winningLine == 'center':
        pygame.draw.line(screen, RED, (WINDOW_SIZE / 2, 0), (WINDOW_SIZE / 2, WINDOW_SIZE), SHAPE_WIDTH)

    elif winningLine == 'right':
        pygame.draw.line(screen, RED, ((WINDOW_SIZE / 6) * 5, 0), ((WINDOW_SIZE / 6) * 5, WINDOW_SIZE), SHAPE_WIDTH)

    elif winningLine == 'leftToRight':
        pygame.draw.line(screen, RED, (0, 0), (WINDOW_SIZE, WINDOW_SIZE), SHAPE_WIDTH)

    elif winningLine == 'rightToLeft':
        pygame.draw.line(screen, RED, (0, WINDOW_SIZE), (WINDOW_SIZE, 0), SHAPE_WIDTH)


#-----------------------------------------------------------------------------------------------------------------------


# so the board is not created every loop
boardCreated = False

# decides who's turn it is
playerTurn = True
AITurn = False

# arrays that keep track of plays, entries are the squareNum
listX = []
listO = []

# Game loop
running = True
while running:
    for event in pygame.event.get():  # Get all events
        if event.type == pygame.QUIT:  # Check for window close event
            running = False

        if (boardCreated == False):
            # Fill the screen with white
            screen.fill(WHITE)
            # drawing game board lines
            drawBoard()
            boardCreated = True

        if (playerTurn):
            # Detect mouse button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos  # Get the position of the mouse

                drawX(decideSquareNum(x, y))
                listX.append(decideSquareNum(x, y))
                playerTurn = False
                AITurn = True

        elif (AITurn):
            # decide move
            aiMove = AImoveDecision(listX, listO)
            drawO(aiMove)
            listO.append(aiMove)
            AITurn = False
            playerTurn = True

        winResult = checkWin(listX, listO)
        winOrLose = winResult[0]
        if (winOrLose == 'win'):
            winningPlayer = winResult[1]
            winningLine = winResult[2]
            drawWinLine(winningLine)
            playerTurn = False
            AITurn = False

        # see if board is full
        if (len(listO) + len(listX) == 9):
            playerTurn = False
            AITurn = False

        pygame.display.update()

# Quit Pygame
pygame.quit()
