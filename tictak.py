def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_choice(board):
    position = 0
 
    while position not in range(1, 10):
        position = int(input("Choose your position (1-9): "))
 
    return position
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board, mark):
    return (
        (board[7] == mark and board[8] == mark and board[9] == mark) or  # top row
        (board[4] == mark and board[5] == mark and board[6] == mark) or  # middle row
        (board[1] == mark and board[2] == mark and board[3] == mark) or  # bottom row
        (board[7] == mark and board[4] == mark and board[1] == mark) or  # left column
        (board[8] == mark and board[5] == mark and board[2] == mark) or  # middle column
        (board[9] == mark and board[6] == mark and board[3] == mark) or  # right column
        (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark)     # diagonal
    )
def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True
def replay():
    return input("Play again? Enter Yes or No: ").lower().startswith('y')
def player_input():
    marker = ''
 
    while marker not in ['X', 'O']:
        marker = input("Player 1: Choose X or O: ").upper()
 
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
import random
 
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
 
while True:
 
    # Reset the board
    theBoard = [' '] * 10
 
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
 
    play_game = input('Are you ready to play? Enter Yes or No.')
 
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
 
    while game_on:
        if turn == 'Player 1':
            # Player 1 Turn
 
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
 
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
 
        else:
            # Player 2 Turn
 
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
 
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
 
    if not replay():
        break
 