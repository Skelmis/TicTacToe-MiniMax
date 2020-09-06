"""
Lets make a simple as fuck game, for learning purpose

0 - Empty space
1 - X
2 - O
"""
import random
import time


def OutputGame(game):
    """
    Takes the game list and prints to console accordingly
    """
    options = {0: " ", 1: "X", 2: "O"}
    for rowIndex in range(len(game)):
        for columnIndex in range(len(game[rowIndex])):
            currentMove = options[game[rowIndex][columnIndex]]

            if rowIndex == 0 and columnIndex == 0:
                print("  0|1|2")
                print(f"0|{currentMove}", end="")
            elif rowIndex == 1 and columnIndex == 0:
                print(f"1|{currentMove}", end="")
            elif rowIndex == 2 and columnIndex == 0:
                print(f"2|{currentMove}", end="")
            else:
                print(f"|{currentMove}", end="")

        print()


def ParseUserInput(userInput):
    """
    Given an input, return the row and column selected
    """
    if len(userInput) != 3:
        return False, False

    try:
        row, column = userInput.split(" ")
    except ValueError:
        return False, False

    row = int(row)
    column = int(column)
    return row, column


def GetValidAIMoves(game):
    """
    Iterate over the entire board and create a nested list of valid moves
    """
    validMoves = []
    for rowIndex in range(len(game)):
        for columnIndex in range(len(game[rowIndex])):
            if game[rowIndex][columnIndex] == 0:
                validMoves.append([rowIndex, columnIndex])

    return validMoves


def IsBoardFull(game):
    """
    Given the game board, figure out if the board is full and thus end the game
    """
    for rowIndex in range(len(game)):
        for columnIndex in range(len(game[rowIndex])):
            if game[rowIndex][columnIndex] == 0:
                return False

    return True


def HasSomeoneWon(game):
    """
    Given the current game state, figure out if someone has won
    """
    # First, check all rows
    for row in game:
        if all(x == row[0] for x in row):
            if row[0] == 0:
                continue
            return True, row[0]

    # Now lets check all columns
    currentVerticals = [
        [game[0][0], game[1][0], game[2][0]],
        [game[0][1], game[1][1], game[2][1]],
        [game[0][2], game[1][2], game[2][2]],
    ]
    for vertical in currentVerticals:
        if all(x == vertical[0] for x in vertical):
            if vertical[0] == 0:
                continue
            return True, vertical[0]

    # Lets check diagonals
    currentDiagonals = [
        [game[0][0], game[1][1], game[2][2]],
        [game[0][2], game[1][1], game[2][0]],
    ]
    for diagonal in currentDiagonals:
        if all(x == diagonal[0] for x in diagonal):
            if diagonal[0] == 0:
                continue
            return True, diagonal[0]

    return False, False


def IsGameOver(game):
    boardFull = IsBoardFull(game)
    isWinner = HasSomeoneWon(game)

    if isWinner[0] is True:
        return isWinner
    elif boardFull and isWinner[0] is False:
        return True, False

    return False, False


def main():
    game = [[0 for x in range(3)] for y in range(3)]
    gameOver = False
    gameWinner = None
    userTurn = True

    input(
        "Welcome to TicTacToe!\nFor your turn, please pick where you want to go based off of the numbers.\nPick the "
        "row first, and then the column. For example, 0 2, would be the top right of the board.\nPress enter once "
        "you have finished reading this."
    )
    print("\nGame is beginning!\nYou are X\n")

    while not gameOver:
        OutputGame(game)  # Print the board before anything else

        if userTurn:
            validInput = False
            while not validInput:
                userMove = input("Where do you want to go? ")
                row, column = ParseUserInput(userMove)

                if row is False:
                    # Invalid input
                    print(
                        "Please provide a valid input!\nPick the row first, and then the column. "
                        "For example, 0 2, would be the top right of the board."
                    )
                    continue

                # Now check if the move itself is legal
                if game[row][column] != 0:
                    print("This is not a valid move! Please try again.")
                    continue

                # Cool, the move is valid. Do it and then move turns
                game[row][column] = 1
                userTurn = False
                validInput = True

        else:
            # Its the computers turn
            validMoves = GetValidAIMoves(game)
            AIMove = random.choice(validMoves)
            game[AIMove[0]][AIMove[1]] = 2
            userTurn = True
            time.sleep(random.random())
            print(f"\nAI played: {AIMove[0]} {AIMove[1]}")

        over = IsGameOver(game)
        if over[0] is True:
            gameWinner = over[1]
            gameOver = True

    # The game is over, the board is now full or someone has won
    print()
    OutputGame(game)

    if gameWinner is False:
        print("It was a tie!")
    elif gameWinner == 1:
        print("Congrats, you won dude!")
    elif gameWinner == 2:
        print("Sorry to say you lost dude..")


if __name__ == "__main__":
    main()
