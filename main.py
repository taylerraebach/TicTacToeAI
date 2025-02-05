import pygame  # Import Pygame
import copy

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
def clickedSquare(x, y):
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
def drawO(squareNum):
    # Render the text (create a surface with the letter "X")
    text = font.render('O', True, BLACK)

    # Get the rectangle of the text and center it
    x, y = squareLocation(squareNum)
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
def AImoveDecision(gameBoard):

    # checking if any ai move will lead to a win, and then blocking that move
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == 'e':
                testGameBoard = copy.deepcopy(gameBoard)
                testGameBoard[i][j] = 'o'
                testWin = checkWin(testGameBoard)
                if testWin[0] == 'win':
                    row = i
                    column = j
                    squareNum = aiMoveNumber(row, column)
                    return squareNum

    # checking if any user move will lead to a win, and then blocking that move
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == 'e':
                testGameBoard = copy.deepcopy(gameBoard)
                testGameBoard[i][j] = 'x'
                testWin = checkWin(testGameBoard)
                if testWin[0] == 'win':
                    row = i
                    column = j
                    squareNum = aiMoveNumber(row, column)
                    return squareNum


    # if no move will lead to blocking a win, randomly place an o
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == 'e':
                row = i
                column = j
                squareNum = aiMoveNumber(row, column)
                return squareNum


#-----------------------------------------------------------------------------------------------------------------------
def aiMoveNumber(row, column):

    if row == 0:
        if column == 0:
            return 0
        elif column == 1:
            return 1
        elif column == 2:
            return 2

    elif row == 1:
        if column == 0:
            return 3
        elif column == 1:
            return 4
        elif column == 2:
            return 5

    elif row == 2:
        if column == 0:
            return 6
        elif column == 1:
            return 7
        elif column == 2:
            return 8


#-----------------------------------------------------------------------------------------------------------------------
def checkWin(gameBoard):
    # deciding if a player has won

    if (gameBoard[0][0] == 'x' and gameBoard[0][1] == 'x' and gameBoard[0][2]) == 'x':
        return ['win', 'x', 'top']
    elif (gameBoard[1][0] == 'x' and gameBoard[1][1] == 'x' and gameBoard[1][2]) == 'x':
        return ['win', 'x', 'middle']
    elif (gameBoard[2][0] == 'x' and gameBoard[2][1] == 'x' and gameBoard[2][2]) == 'x':
        return ['win', 'x', 'bottom']
    elif (gameBoard[0][0] == 'x' and gameBoard[1][0] == 'x' and gameBoard[2][0]) == 'x':
        return ['win', 'x', 'left']
    elif (gameBoard[0][1] == 'x' and gameBoard[1][1] == 'x' and gameBoard[2][1]) == 'x':
        return ['win', 'x', 'center']
    elif (gameBoard[0][2] == 'x' and gameBoard[1][2] == 'x' and gameBoard[2][2]) == 'x':
        return ['win', 'x', 'right']
    elif (gameBoard[0][0] == 'x' and gameBoard[1][1] == 'x' and gameBoard[2][2]) == 'x':
        return ['win', 'x', 'leftToRight']
    elif (gameBoard[0][2] == 'x' and gameBoard[1][1] == 'x' and gameBoard[2][0]) == 'x':
        return ['win', 'x', 'rightToLeft']

    if (gameBoard[0][0] == 'o' and gameBoard[0][1] == 'o' and gameBoard[0][2]) == 'o':
        return ['win', 'o', 'top']
    elif (gameBoard[1][0] == 'o' and gameBoard[1][1] == 'o' and gameBoard[1][2]) == 'o':
        return ['win', 'o', 'middle']
    elif (gameBoard[2][0] == 'o' and gameBoard[2][1] == 'o' and gameBoard[2][2]) == 'o':
        return ['win', 'o', 'bottom']
    elif (gameBoard[0][0] == 'o' and gameBoard[1][0] == 'o' and gameBoard[2][0]) == 'o':
        return ['win', 'o', 'left']
    elif (gameBoard[0][1] == 'o' and gameBoard[1][1] == 'o' and gameBoard[2][1]) == 'o':
        return ['win', 'o', 'center']
    elif (gameBoard[0][2] == 'o' and gameBoard[1][2] == 'o' and gameBoard[2][2]) == 'o':
        return ['win', 'o', 'right']
    elif (gameBoard[0][0] == 'o' and gameBoard[1][1] == 'o' and gameBoard[2][2]) == 'o':
        return ['win', 'o', 'leftToRight']
    elif (gameBoard[0][2] == 'o' and gameBoard[1][1] == 'o' and gameBoard[2][0]) == 'o':
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
def adjustBoard(gameBoard, squareNum, moveLetter):

    if squareNum == 0:
        gameBoard[0][0] = moveLetter
    elif squareNum == 1:
        gameBoard[0][1] = moveLetter
    elif squareNum == 2:
        gameBoard[0][2] = moveLetter
    elif squareNum == 3:
        gameBoard[1][0] = moveLetter
    elif squareNum == 4:
        gameBoard[1][1] = moveLetter
    elif squareNum == 5:
        gameBoard[1][2] = moveLetter
    elif squareNum == 6:
        gameBoard[2][0] = moveLetter
    elif squareNum == 7:
        gameBoard[2][1] = moveLetter
    elif squareNum == 8:
        gameBoard[2][2] = moveLetter


#-----------------------------------------------------------------------------------------------------------------------

# so the board is not created every loop
boardCreated = False

# decides who's turn it is
playerTurn = True
AITurn = False

# array for game board that stores moves
gameBoard = [
    ['e', 'e', 'e'],
    ['e', 'e', 'e'],
    ['e', 'e', 'e']
]

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

                moveLetter = 'x'
                squareNum = clickedSquare(x, y)
                drawX(squareNum)
                adjustBoard(gameBoard, squareNum, moveLetter)
                playerTurn = False
                AITurn = True

        elif (AITurn):
            # decide move
            moveLetter = 'o'
            squareNum = AImoveDecision(gameBoard)
            drawO(squareNum)
            adjustBoard(gameBoard, squareNum, moveLetter)
            AITurn = False
            playerTurn = True

        winResult = checkWin(gameBoard)
        winOrLose = winResult[0]
        if (winOrLose == 'win'):
            winningPlayer = winResult[1]
            winningLine = winResult[2]
            drawWinLine(winningLine)
            playerTurn = False
            AITurn = False

        # see if board is full
        emptySquares = 0
        for i in range(3):
            for j in range(3):
                if gameBoard[i][j] == 'e':
                    emptySquares += 1
        if emptySquares == 0:
            playerTurn = False
            AITurn = False

        pygame.display.update()

# Quit Pygame
pygame.quit()
