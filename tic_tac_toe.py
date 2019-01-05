#Tic Tac Toe

the_board = {'top left' : ' ', 'top middle' : ' ', 'top right' : ' ',
             'mid left': ' ', 'mid middle': ' ', 'mid right': ' ',
             'bottom left': ' ', 'bottom middle': ' ', 'bottom right': ' '}
def printBoard(board):
    print(board['top left'] + '|' + board['top middle'] + '|' + board['top right'])
    print('-+-+-')
    print(board['mid left'] + '|' + board['mid middle'] + '|' + board['mid right'])
    print('-+-+-')
    print(board['bottom left'] + '|' + board['bottom middle'] + '|' + board['bottom right'])
turn = 'X'
for i in range(9):
    printBoard(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(the_board)

#the game doesnt understand spaces not in the dict and also cant determine a winner 