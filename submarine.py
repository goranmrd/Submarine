from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print("Sink my ship in 5 turns.")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#print(ship_row)
#print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
guesses = 0

while guesses < 5:
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    elif guess_row not in range(5) or guess_col not in range(5):
        print("Oops, that's not even in the ocean.")

    elif board[guess_row][guess_col] == 'X':
         print("You guessed that one already.")

    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = 'X'
        # Print (turn + 1) here!
        print_board(board)
        guesses += 1
        if guesses == 5:
            print("Out of turns. Game Over!")

