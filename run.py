import random
# creating the global variables
# the player sets the numerical value of the board size
# this then sets the size of the playable board size to be displayed
# player board displays were the player positioned thier ships
# and updated information miss and hits
# only the computer pseudo board is displayed on screen
# showing only updated miss and hits
# the com board has the ships locations
# these dictionaries will hold the positions of the ships location on the board
player_board = []
com_board = []
com_pseudo_board = []
player_ships = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol': 0}
com_ships = {'battleship': 0, 'destroyer': 0, 'submarine': 0, 'patrol': 0}

print('\n\n     ******----WELCOME TO BATTLESHIPS----******\n')
print(' in this version of terminal output battleships game\n')
print('             the boat icons = @ symbol')
print('             the miss icons = O symbol')
print('              the hit icons = X symbol')

board_size = 0
board_set = True
while board_set:
    print('\n   What board size would you like to play on?')
    print("\n   Select a board size: A number between 5-14")
    count = int(input())
    if count in range(5, 15):
        print('\n---"Good choice Captain, setting up radar systems now"---')
        count += 1
        board_set = False
    else:
        print("\nsorry that is an incorrect value")
        print("you need to pick a number between 5-14")
board_size = count


def random_num():
    '''
    random number generator to set the com ships location and for com guess
    '''
    in_range = True
    while in_range:
        num = round((random.random()) * 10, )
        if num in range(0, 6):
            in_range = False
    return num


def set_board_size():
    '''
    function takes input from the player to position thir boats on the board
    '''
    for x in range(board_size):
        player_board.append([])
        com_board.append([])
        com_pseudo_board.append([])
        for y in range(board_size):
            player_board[x].append([' - '])
            com_board[x].append([' - '])
            com_pseudo_board[x].append([' - '])


def set_ships():
    print("Please select the locations of your ships")
    last_boat = []
    for key, value in player_ships.items():
        ship = key
        selection = True
        while selection:
            print("\n" + f'select "{ship}" position' + "\n")
            column = board_size
            column -= 1
            print(f"please select a column from 0 to {column}")
            # this conditional checks that ships do not occupy the same space
            col_pick = True
            while col_pick:
                col = int(input())
                if col not in range(0, board_size):
                    print("---nope out of range try again---")
                else:
                    col_pick = False
            rows = board_size
            rows -= 1
            print(f"please select a row from 0 to {rows}")
            row_pick = True
            while row_pick:
                row = int(input())
                if row not in range(0, board_size):
                    print("---nope out of range, try again---")
                else:
                    row_pick = False
            boat = row, col
            check = 0
            for x in range(len(last_boat)):
                if boat == last_boat[x]:
                    check += 1
            if check > 0:
                print('\n---"This position is taken sailor"---\n')
            else:
                print('\n---"Yep, looks good setting up here Captain"---\n')
                last_boat.append(boat)
                check = 0
                selection = False
        player_ships[key] = [col], [row]
        print("")
        print("your current ship locations")
        print(player_ships)
        player_board[row][col] = [' @ ']
        display_ships()
    for key, value in com_ships.items():
        col = random_num()
        row = random_num()
        com_ships[key] = [col], [row]
        com_board[row][col] = [' @ ']
    print('---"computer setting its ships"---')
    display_ships()


def display_ships():
    '''
    optional display of the player and computers boards
    '''
    print("")
    print("Display boards")
    blue = True
    while blue:
        print("To display players board select 'p'")
        print("To display computers board select 'c'")
        print("To skip board display select 's'")
        selection = input()
        if selection == 'p':
            print("\n")
            print("   Player Board")
            print("  ", end=" ")
            for x in range(board_size):
                print('-----', end="-")
            print("")
            print("")
            print("  ", end=" ")
            for x in range(board_size):
                print(f'  {x}', end="   ")
            print("")
            print("")
            for x in range(board_size):
                print(f'{x}', end=" | ")
                for y in range(board_size):
                    print(f'{player_board[x][y][0]}', end=" | ")
                print("")
                print("")
        elif selection == 'c':
            print("\n")
            print("   Computers Board")
            print("  ", end=" ")
            for x in range(board_size):
                print('-----', end="-")
            print("")
            print("")
            print("  ", end=" ")
            for x in range(board_size):
                print(f'  {x}', end="   ")
            print("")
            print("")
            for x in range(board_size):
                print(f'{x}', end=" | ")
                for y in range(board_size):
                    print(f'{com_pseudo_board[x][y][0]}', end=" | ")
                print("")
                print("")
        elif selection == 's':
            print("")
            blue = False
        else:
            print("\n---That selection is not supported---\n")


def start_game():
    '''
    function for the game itself
    '''
    player_lives = 4
    com_lives = 4
    game_on = True
    while game_on:
        print('-----"READY TO FIGHT"-----')
        print('\n///missile tubes ready///')
        missile_flight = True
        while missile_flight:
            print('\n---"Captain select a column"---')
            guess_col = int(input())
            print('\n---"Captain select a row"---')
            guess_row = int(input())
            print("\n///LAUNCH MISSILE///")
            print('---"missile away"---')
            if player_lives == 0:
                missile_flight = False
            elif com_board[guess_row][guess_col][0] == ' @ ':
                print('\n---"KABOOM"---')
                print('---"Thats a hit Captain"---')
                com_board[guess_row][guess_col][0] = ' X '
                com_pseudo_board[guess_row][guess_col][0] = ' X '
                missile_flight = False
                com_lives -= 1
                display_ships()
            elif com_board[guess_row][guess_col][0] == ' O ':
                print('\n---"Uhh, Captain we already hit that spot"---\n')
                display_ships()
                print('---"Here Sir, fresh coffee')
                print('\n---"Requesting new co-ordinates, Sir"---\n')
            elif com_board[guess_row][guess_col][0] == ' X ':
                print('\n---"Uhh, Captain we already hit that spot"---')
                display_ships()
                print('---"Yep, there toast"---\n')
                print('---"Requesting new co-ordinates, Sir"---\n')
            else:
                print('\n---"SPLASH"---')
                print('---"Thats a miss Captain"---\n')
                com_board[guess_row][guess_col][0] = ' O '
                com_pseudo_board[guess_row][guess_col][0] = ' O '
                missile_flight = False
                display_ships()
        print('\n---"ALARM"---')
        print('---"incoming missile Captain"---')
        enemy_fire = True
        while enemy_fire:
            com_guess1 = random_num()
            com_guess2 = random_num()
            if com_lives == 0:
                enemy_fire = False
            elif player_board[com_guess1][com_guess2][0] == ' @ ':
                print('\n---"KABOOM"---')
                print('---"Thats a hit Captain"---\n')
                player_board[com_guess1][com_guess2][0] = ' X '
                player_lives -= 1
                enemy_fire = False
                display_ships()
            elif player_board[com_guess1][com_guess2][0] == ' O ':
                print('\n---"Ha, there just hitting open water and fish"---')
                print('---"poor fish"---')
            elif player_board[com_guess1][com_guess2][0] == ' X ':
                print('\n---"those idiots were aiming at a downed ship"---')
            else:
                print('\n---"SPLASH"---')
                print('---"Thats a miss Captain"---\n')
                player_board[com_guess1][com_guess2][0] = ' O '
                enemy_fire = False
                display_ships()
        if com_lives == 0:
            print('\n---"GAME OVER"---')
            print('---"YOU WIN"---')
            game_on = False
        elif player_lives == 0:
            print('\n---"GAME OVER"---')
            print('\n---"YOU LOST"---')
            game_on = False
        else:
            print('\n---"Were still in this fight Captain"---\n')


def main():
    '''
    this is the main function for the whole game
    '''
    set_board_size()
    display_ships()
    set_ships()
    start_game()


main()
