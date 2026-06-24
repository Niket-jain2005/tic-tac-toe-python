import random

# Game variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


# Print the board
def printBoard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Player input
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a position (1-9): "))

            if 1 <= inp <= 9 and board[inp - 1] == "-":
                board[inp - 1] = currentPlayer
                break
            else:
                print("Invalid move! Try again.")

        except ValueError:
            print("Please enter a valid number between 1 and 9.")


# Check rows
def checkRow(board):
    global winner

    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True

    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True

    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

    return False


# Check columns
def checkColumn(board):
    global winner

    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True

    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True

    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

    return False


# Check diagonals
def checkDiagonal(board):
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

    return False


# Check for winner
def checkWin():
    global gameRunning

    if checkRow(board) or checkColumn(board) or checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


# Check for tie
def checkTie(board):
    global gameRunning

    if "-" not in board and gameRunning:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False


# Switch player
def switchPlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# Computer move
def computer(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == "-"]

    if empty_spots:
        position = random.choice(empty_spots)
        board[position] = "O"
        print(f"Computer chose position {position + 1}")


# Position guide
print("Welcome to Tic-Tac-Toe!")
print("\nBoard positions:")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")


# Main game loop
while gameRunning:

    if currentPlayer == "X":
        printBoard(board)
        playerInput(board)

        checkWin()
        if not gameRunning:
            break

        checkTie(board)
        if not gameRunning:
            break

        switchPlayer()

    else:
        computer(board)

        checkWin()
        if not gameRunning:
            break

        checkTie(board)
        if not gameRunning:
            break

        switchPlayer()