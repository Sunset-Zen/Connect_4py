import random

# ( Variables )
multiplayer, singleplayer = False, False
board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
string_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
player1_f, player2_f, cpu_f = False, False, False
turn_array = ['Heads', 'Tails']
coin_flip = random.randint(0, 1)
player1_symbol, cpu_symbol = 'p', 'c'

# ( Functions )
def display_board():
    print('')
    tracker = 0
    for i in range(len(board)):
        for j in range(7):
            tracker += 1
            if tracker == 7:
                print(string_board[i][j], end=' ')
                tracker -= 7
            else:
                print(string_board[i][j], end=' | ')
        print()
    print('')

def determine_first(a, b, c):
    print('determine first')

def re_roll(a, b):
    # Base Condition
    if board[a][b] == 0:
        board[a][b] = 1
        print(b)
        return b
    else:
        temp_b = random.randint(0, 6)
        re_roll(a, temp_b)

print('=================================================' * 2)
print('\nWelcome To Connect-4')
print('Developed by : Otis Ray Jackson IV')

# ( Display Ruleset )
print('_________________________________________________' * 2)
print('\n( Basic Ruleset of Connect 4 )')
print('_________________________________________________' * 2)
print('Depending on who goes first, [CPU, Player1, Player2]\tTurns granted are board space based')
print('100% Indexed && Turn based application.\t\t\t\t\t** ( Indexes start from 0 & Ends at 6 ) ** ')
print('Select Box Example : => \t\t\t\t\t\t\t\t0\t [Column]\n')

# ( Ask if multiplayer -> ( ... ))
first_answer = input('Multiplayer ?? A for [Yes] B for [No]:\t')
if first_answer == 'A' or first_answer == 'a':
    multiplayer = True
    singleplayer = False
if first_answer == 'B' or first_answer == 'b':
    singleplayer = True
    multiplayer = False

# ( Pick a symbol )
if multiplayer:
    player1_symbol = input('Player 1 please enter desired symbol:\t')
    player2_symbol = input('Player 2 please enter desired symbol:\t')
elif singleplayer:
    player1_symbol = input('Player 1 please enter desired symbol:\t')
    cpu_symbol = 'C'
    cf1_guess, cf2_guess = '', ''

    # ( Determine Who Goes First ) -> make into function
    cf1_guess = input('\nPlayer 1 Heads or Tails ??:\t')
    if cf1_guess == 'Heads':
        cf2_guess = 'Tails'
    if cf1_guess == 'Tails':
        cf2_guess = 'Heads'

    if cf1_guess == turn_array[coin_flip]:
        player1_f = True
        print('\nPlayer 1 Goes First !!!')
    if cf2_guess == turn_array[coin_flip]:
        cpu_f = True
        print('\nCPU Goes First !!!')

if player1_f:
    row_counter = 5
    while row_counter < 6:
        if row_counter == 6:
            break

        # ( Row Check )
        fill_count = 0
        for i in range(len(board)):
            if fill_count == len(board):
                print('row: ' + str(i) + ' full')
                row_counter -= 1
            if i == 1:
                fill_count += 1

        # ( Player 1 Input )
        player_input = input('\nPlayer 1 please enter location:\t')
        if board[row_counter][int(player_input)] == 1:
            board[row_counter-1][int(player_input)] = 1
            string_board[row_counter-1][int(player_input)] = player1_symbol
        else:
            board[row_counter][int(player_input)] = 1
            string_board[row_counter][int(player_input)] = player1_symbol

        # ( Update && Display Board )
        display_board()
        print('(row_count): ' + str(row_counter))

        # ( Generate CPU Input )
        cpu_input = random.randint(0, 6)
        if board[row_counter][cpu_input] == 1:
            board[row_counter - 1][cpu_input] = 1
            string_board[row_counter-1][cpu_input] = cpu_symbol
        else:
            board[row_counter][cpu_input] = 1
            string_board[row_counter][cpu_input] = cpu_symbol
        print('\nCPU entered column:\t' + str(cpu_input))

        # ( Update && Display Board )
        display_board()
        print('(row_count): ' + str(row_counter))


if cpu_f:
    row_counter = 5
    while row_counter < 6:
        if row_counter == 6:
            break

        # ( Row Check )
        fill_count = 0
        for i in range(len(board)):
            if fill_count == len(board):
                print('row: ' + str(i) + ' full')
                row_counter -= 1
            if i == 1:
                fill_count += 1

        # ( Generate CPU Input )
        cpu_input = random.randint(0, 6)
        if board[row_counter][cpu_input] == 1:
            board[row_counter - 1][cpu_input] = 1
            string_board[row_counter - 1][cpu_input] = cpu_symbol
        else:
            board[row_counter][cpu_input] = 1
            string_board[row_counter][cpu_input] = cpu_symbol
            print('\nCPU entered column:\t' + str(cpu_input))

        # ( Update && Display Board )
        display_board()
        print('(row_count): ' + str(row_counter))

        # ( Player 1 Input )
        player_input = input('\nPlayer 1 please enter location:\t')
        if board[row_counter][int(player_input)] == 1:
            board[row_counter - 1][int(player_input)] = 1
            string_board[row_counter - 1][int(player_input)] = player1_symbol
        else:
            board[row_counter][int(player_input)] = 1
            string_board[row_counter][int(player_input)] = player1_symbol

        # ( Update && Display Board )
        display_board()
        print('(row_count): ' + str(row_counter))

print('=================================================' * 2)