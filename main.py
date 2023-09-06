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
player1_symbol, player2_symbol, cpu_symbol = 'p1', 'p2', 'c'
fill_count = 0
player_connects, cpu_connects = 0, 0
game_over = False

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

def board_check(a_symbol, b_symbol):
    for i in range(6):
        for j in range(7):
            # Is space occupied
            if board[i][j] == 1:
                # ( middle conditions )
                if i == 3 and j == 3:
                    # ( check diagonals )
                    if string_board[i-1][j+1] == a_symbol and string_board[i-2][j+2] == a_symbol:
                        if string_board[i-3][j+3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i-1][j+1] == b_symbol and string_board[i-2][j+2] == b_symbol:
                        if string_board[i-3][j+3] == b_symbol:
                            # cpu_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    if string_board[i-1][j-1] == a_symbol and string_board[i-2][j-2] == a_symbol:
                        if string_board[i-3][j-3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i-1][j-1] == b_symbol and string_board[i-2][j-2] == b_symbol:
                        if string_board[i-3][j-3] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( linear )
                    if string_board[i][j+1] == a_symbol and string_board[i][j+2] == a_symbol:
                        if string_board[i][j+3] == a_symbol:
                            # player_connects += 3
                            print('(Player): Connect 4 !!!!')
                            return True
                    if string_board[i][j-1] == a_symbol and string_board[i][j-2] == a_symbol:
                        if string_board[i][j-3] == a_symbol:
                            # player_connects += 3
                            print('(Player): Connect 4 !!!!')
                            return True
                    if string_board[i][j+1] == b_symbol and string_board[i][j+2] == b_symbol:
                        if string_board[i][j+3] == b_symbol:
                            # cpu_connects += 3
                            print('(CPU): Connect 4 !!!!')
                            return True
                    if string_board[i][j-1] == b_symbol and string_board[i][j-2] == b_symbol:
                        if string_board[i][j-3] == b_symbol:
                            # cpu_connects += 3
                            print('(CPU): Connect 4 !!!!')
                            return True
                    # ( vert )
                    if string_board[i-1][j] == a_symbol and string_board[i-2][j] == a_symbol:
                        if string_board[i-3][j] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!! \n')
                            return True
                    if string_board[i-1][j] == b_symbol and string_board[i-2][j] == b_symbol:
                        if string_board[i-3][j] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!! \n')
                            return True
                    # print('\n Middle Condition \n')
                elif i == 2 and j == 3:
                    # ( check diagonals )
                    if string_board[i+1][j-1] == a_symbol and string_board[i+2][j-2] == a_symbol:
                        if string_board[i+3][j-3] == a_symbol:
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i+1][j+1] == a_symbol and string_board[i+2][j+2] == a_symbol:
                        if string_board[i+3][j+3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i + 1][j - 1] == b_symbol and string_board[i + 2][j - 2] == b_symbol:
                        if string_board[i + 3][j - 3] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    if string_board[i + 1][j + 1] == b_symbol and string_board[i + 2][j + 2] == b_symbol:
                        if string_board[i + 3][j + 3] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( linear )
                    if string_board[i][j+1] == a_symbol and string_board[i][j+2] == a_symbol:
                        if string_board[i][j+3] == a_symbol:
                            # player_connects += 3
                            print('(Player): Connect 4 !!!!')
                            return True
                    if string_board[i][j-1] == a_symbol and string_board[i][j-2] == a_symbol:
                        if string_board[i][j-3] == a_symbol:
                            # player_connects += 3
                            print('(Player): Connect 4 !!!!')
                            return True
                    if string_board[i][j+1] == b_symbol and string_board[i][j+2] == b_symbol:
                        if string_board[i][j+3] == b_symbol:
                            # cpu_connects += 3
                            print('(CPU): Connect 4 !!!!')
                            return True
                    if string_board[i][j-1] == b_symbol and string_board[i][j-2] == b_symbol:
                        if string_board[i][j-3] == b_symbol:
                            # cpu_connects += 3
                            print('(CPU): Connect 4 !!!!')
                            return True
                    # ( vert )
                    if string_board[i+1][j] == a_symbol and string_board[i+2][j] == a_symbol:
                        if string_board[i+3][j] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!! \n')
                            return True
                    if string_board[i+1][j] == b_symbol and string_board[i+2][j] == b_symbol:
                        if string_board[i+3][j] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!! \n')
                            return True
                    # print('\n Middle Condition \n')
                # ( edge conditions )
                if i >= 3 > j:
                    # ( check diagonals )
                    if string_board[i - 1][j + 1] == a_symbol and string_board[i - 2][j + 2] == a_symbol:
                        if string_board[i - 3][j + 3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i - 1][j + 1] == b_symbol and string_board[i - 2][j + 2] == b_symbol:
                        if string_board[i - 3][j + 3] == b_symbol:
                            # cpu_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( linear )
                    if string_board[i][j+1] == a_symbol and string_board[i][j+2] == a_symbol:
                        if string_board[i][j+3] == a_symbol:
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i][j + 1] == b_symbol and string_board[i][j + 2] == b_symbol:
                        if string_board[i][j + 3] == b_symbol:
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( vert )
                    if string_board[i-1][j] == a_symbol and string_board[i-2][j] == a_symbol:
                        if string_board[i-3][j] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!! \n')
                            return True
                    if string_board[i-1][j] == b_symbol and string_board[i-2][j] == b_symbol:
                        if string_board[i-3][j] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!! \n')
                            return True
                    # print('\n Edge Condition \n')
                elif i <= 3 and j < 3:
                    # ( check diagonals )
                    if string_board[i+1][j+1] == a_symbol and string_board[i+2][j+2] == a_symbol:
                        if string_board[i+3][j+3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i+1][j+1] == b_symbol and string_board[i+2][j+2] == b_symbol:
                        if string_board[i+3][j+3] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( linear )
                    if string_board[i][j+1] == a_symbol and string_board[i][j+2] == a_symbol:
                        if string_board[i][j+3] == a_symbol:
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i][j + 1] == b_symbol and string_board[i][j + 2] == b_symbol:
                        if string_board[i][j + 3] == b_symbol:
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( vert )
                    if string_board[i+1][j] == a_symbol and string_board[i+2][j] == a_symbol:
                        if string_board[i+3][j] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!! \n')
                            return True
                    if string_board[i+1][j] == b_symbol and string_board[i+2][j] == b_symbol:
                        if string_board[i+3][j] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!! \n')
                            return True
                    # print('\n Edge Condition \n')
                elif i >= 3 and j > 3:
                    # ( check diagonals )
                    if string_board[i-1][j-1] == a_symbol and string_board[i-2][j-2] == a_symbol:
                        if string_board[i-3][j-3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i-1][j-1] == b_symbol and string_board[i-2][j-2] == b_symbol:
                        if string_board[i-3][j-3] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( linear )
                    if string_board[i][j-1] == a_symbol and string_board[i][j-2] == a_symbol:
                        if string_board[i][j-3] == a_symbol:
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i][j-1] == b_symbol and string_board[i][j-2] == b_symbol:
                        if string_board[i][j-3] == b_symbol:
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( vert )
                    if string_board[i-1][j] == a_symbol and string_board[i-2][j] == a_symbol:
                        if string_board[i-3][j] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!! \n')
                            return True
                    if string_board[i-1][j] == b_symbol and string_board[i-2][j] == b_symbol:
                        if string_board[i-3][j] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!! \n')
                            return True
                    # print('\n Edge Condition \n')
                elif i <= 3 < j:
                    # ( check diagonals )
                    if string_board[i+1][j-1] == a_symbol and string_board[i+2][j-2] == a_symbol:
                        if string_board[i+3][j-3] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i+1][j-1] == b_symbol and string_board[i+2][j-2] == b_symbol:
                        if string_board[i+3][j-3] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( linear )
                    if string_board[i][j-1] == a_symbol and string_board[i][j-2] == a_symbol:
                        if string_board[i][j-3] == a_symbol:
                            print('\n(Player): Connect 4 !!!\n')
                            return True
                    if string_board[i][j-1] == b_symbol and string_board[i][j-2] == b_symbol:
                        if string_board[i][j-3] == b_symbol:
                            print('\n(CPU): Connect 4 !!!\n')
                            return True
                    # ( vert )
                    if string_board[i+1][j] == a_symbol and string_board[i+2][j] == a_symbol:
                        if string_board[i+3][j] == a_symbol:
                            # player_connects += 3
                            print('\n(Player): Connect 4 !!!! \n')
                            return True
                    if string_board[i+1][j] == b_symbol and string_board[i+2][j] == b_symbol:
                        if string_board[i+3][j] == b_symbol:
                            # player_connects += 3
                            print('\n(CPU): Connect 4 !!!! \n')
                            return True
    return False

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
    while not game_over:
        if fill_count == 43:
            break
        if game_over:
            break
        # ( Player 1 Input )
        player_input = input('\nPlayer 1 please enter location:\t')
        if board[row_counter][int(player_input)] == 1:
            # make this linear vertical traversal ( stack )
            for i in range(6):
                if board[i][int(player_input)] == 0 and board[i+1][int(player_input)] == 1:
                    board[i][int(player_input)] = 1
                    string_board[i][int(player_input)] = player1_symbol
        else:
            board[row_counter][int(player_input)] = 1
            string_board[row_counter][int(player_input)] = player1_symbol
        fill_count += 1

        # ( Update && Display Board )
        display_board()
        game_over = board_check(player1_symbol, cpu_symbol)

        # ( Generate CPU Input )
        cpu_input = random.randint(0, 6)
        if board[row_counter][cpu_input] == 1:
            # make this linear vertical traversal ( stack )
            for i in range(6):
                if board[i][cpu_input] == 0 and board[i+1][cpu_input] == 1:
                    board[i][cpu_input] = 1
                    string_board[i][cpu_input] = cpu_symbol
        else:
            board[row_counter][cpu_input] = 1
            string_board[row_counter][cpu_input] = cpu_symbol
        fill_count += 1
        print('\nCPU entered column:\t' + str(cpu_input))

        # ( Update && Display Board )
        display_board()
        game_over = board_check(player1_symbol, cpu_symbol)
if cpu_f:
    row_counter = 5
    while not game_over:
        if fill_count == 43:
            break
        if game_over:
            break

        # ( Generate CPU Input )
        cpu_input = random.randint(0, 6)
        if board[row_counter][cpu_input] == 1:
            # make this linear vertical traversal ( stack )
            for i in range(6):
                if board[i][cpu_input] == 0 and board[i+1][cpu_input] == 1:
                    board[i][cpu_input] = 1
                    string_board[i][cpu_input] = cpu_symbol
        else:
            board[row_counter][cpu_input] = 1
            string_board[row_counter][cpu_input] = cpu_symbol
        fill_count += 1
        print('\nCPU entered column:\t' + str(cpu_input))

        # ( Update && Display Board )
        display_board()
        game_over = board_check(player1_symbol, cpu_symbol)

        # ( Player 1 Input )
        player_input = input('\nPlayer 1 please enter location:\t')
        if board[row_counter][int(player_input)] == 1:
            # make this linear vertical traversal ( stack )
            for i in range(6):
                if board[i][int(player_input)] == 0 and board[i+1][int(player_input)] == 1:
                    board[i][int(player_input)] = 1
                    string_board[i][int(player_input)] = player1_symbol
        else:
            board[row_counter][int(player_input)] = 1
            string_board[row_counter][int(player_input)] = player1_symbol
        fill_count += 1

        # ( Update && Display Board )
        display_board()
        game_over = board_check(player1_symbol, cpu_symbol)

    print('\nGAME OVER !!!\n')
print('=================================================' * 2)