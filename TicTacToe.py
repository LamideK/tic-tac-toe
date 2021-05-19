import random

# visualize the board
theBoard = {'1': ' ', '2': ' ', '3': ' ',
 '4': ' ', '5': ' ', '6': ' ',
 '7': ' ', '8': ' ', '9': ' '}

game_space = []
turn = ''

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '\n' +'-+-+-'
          + '\n' + board['4'] + '|' + board['5'] + '|' + board['6'] + '\n' + '-+-+-'
          + '\n' +board['7'] + '|' + board['8'] + '|' + board['9'] )

#choosing player
strt = input('Press Enter to start')
choice = random.randrange(2)
if choice == 0:
    turn = 'X'
else:
    turn = 'O'
print(choice)

for play in range(9):
    printBoard(theBoard)
    print('turn for ' + turn + '. Move to what space?' )
    move = input()
    if move in game_space:
        print('please pick another position')
        #move = input()
    else:
        theBoard[move] = turn
        game_space.append(move)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        print(game_space)

# Deciding when the game ends
    # if len(game_space == 9):
    #     if theBoard[0] == theBoard[1] == theBoard[2]\
    #             or theBoard[0] == theBoard[1] == theBoard[2]\
    #             or theBoard[0] == theBoard[1] == theBoard[2]\
    #             or theBoard[0] == theBoard[1] == theBoard[2]:
    #         print('The winner is: ', theBoard[0])

printBoard(theBoard)
print(theBoard.keys())


