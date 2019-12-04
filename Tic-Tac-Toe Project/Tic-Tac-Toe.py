from IPython.display import clear_output

#function to create tic-tac-toe board
def display_board(board):
    pass
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():

    #Output = (Player 1 marker, Player 2 marker)
    marker = ''
    while marker != 'X' and marker!= 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':

        return ('X','O')
    else:
        return ('O','X')

player1_marker , player2_marker = player_input()
