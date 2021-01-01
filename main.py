#DISPLAY BOARD
def display_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#TAKE PLAYER INPUT
def player_marker():
    value = 'dummy'
    acceptable_value = ['X','O']

    while value not in acceptable_value:
        value = input('Player 1: Do you want to be X or O? : ').upper()

        if value not in acceptable_value:
            print('Please select either X or O')
        else:
            return value

#ASK FOR INDEX POSITION TO PUT MARK ON
def get_position():
    index = 'dummy'
    acceptable_value = [x for x in range(1,10)]

    while index not in acceptable_value:
        index = input('Enter the position at which you want to put your marker : ')

        if index.isalpha():
            print('It must be a number between 1 to 9')
        elif int(index) not in acceptable_value:
            print('Please enter valid position i.e. 1 to 9')
        else:
            return int(index)

#op = get_position()
#print(op)

#UPDATE THE BOARD AS PER USER INPUT
def player_turn(board, position, player):
    board[position-1] = player
    return board

#my_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#my_list = player_turn(my_list, 1, 'X')
#display_board(my_list)

#CHECK IF ANYONE IS WINER OR NOT
def winner(board):
    winner_player = 'dummy'
    acceptable_value = ['X','O']

    if board[0] == board[1] ==board[2]:
        winner_player = board[0]
    elif board[3] == board[4] ==board[5]:
        winner_player = board[3]
    elif board[6] == board[7] ==board[8]:
        winner_player = board[6]
    elif board[0] == board[3] ==board[6]:
        winner_player = board[0]
    elif board[1] == board[4] ==board[7]:
        winner_player = board[1]
    elif board[2] == board[5] ==board[8]:
        winner_player = board[2]
    elif board[0] == board[4] ==board[8]:
        winner_player = board[0]
    elif board[2] == board[4] ==board[6]:
        winner_player = board[2]

    if winner_player in acceptable_value:
        return winner_player
    else:
        return False

#my_list = ['X','O','X','O','O','O','O','X','O']
#op = winner(my_list)
#print(op)
