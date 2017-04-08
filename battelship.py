from random import randint

board = []

for x in range(6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


#First ship
ship_row = random_row(board)
ship_col = random_col(board)

#Creating the Second ship(Tried by defining another random_row1 and randow_col1 function)

ship_row1=random_row(board)
ship_col1=random_col(board)

if ship_row1==ship_row and ship_col1==ship_col:
    ship_row1=randow_row(board)
    ship_col1=random_col(board)

elif ship_col1==ship_col:
    ship_col1=random_col(board)

elif ship_row1==ship_row:
    ship_row1=random_row(board)

else:
    ship_row1=random_row(board)

print ship_row, ship_col


print ship_row1, ship_col1

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!



for turn in range(4):

    print turn

    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if board[ship_row][ship_col]=="H" and board[ship_row1][ship_col1]=="H" :
        print "You win"
        break

    elif (guess_row == ship_row and guess_col == ship_col) or (guess_row==ship_row1 and guess_col==ship_col1):
        print "Congratulations! You sunk one of my battleship!"
        board[guess_row][guess_col]="H"

    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed this location already"
        else:
            print "You missed, Please try again."
            board[guess_row][guess_col] = "X"

    if turn == 3:
        print "Game Over"
    # Print (turn + 1) here!
    print_board(board)
    turn += 1
    print turn
