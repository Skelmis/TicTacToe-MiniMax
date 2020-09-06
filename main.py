"""
Lets make a simple as fuck game, for learning purpose

0 - Empty space
1 - X
2 - O
"""


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


def main():
    game = [[x for x in range(3)] for y in range(3)]
    OutputGame(game)


if __name__ == "__main__":
    main()
