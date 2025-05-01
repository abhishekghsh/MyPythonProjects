"""	
* Take Player 1 and Player 2 usernames
* Assign 'X' and 'O' to Player 1 and Player 2 respectively.
* Display blank board
* Input position from Player 1
* Change the List index with 'X' and then Display board 
* Input Position from Player 2
* Change the List index with 'O' and then Display board

"""


def player_selection():
    player_list = []
    player_set = {}
    while len(player_set) != 2:
        player_list = [input_name(1), input_name(2)]
        player_set = set(player_list.copy())
        if len(player_set) != 2:
            print("Same names not allowed, Please try again!")
    return player_list


def input_name(counter):
    # Take Player's name
    confirm = False
    name = ''
    while not confirm:
        name = input(f'Please enter player {counter}\'s name: ')
        print(f'You have chosen Player {counter}\'s Name --> {name}')
        confirm = confirmation()
    return name
    

def confirmation():
    # Takes Confirmation
    confirm = ''
    while confirm not in ['Y', 'N']:
        confirm = input("Are your sure? (Y/N): ").upper()
        if confirm not in ['Y','N']:
            print("Sorry, Couldn't understand your input, Please try again! ")
        if confirm == 'Y':
            return True
        elif confirm == 'N':
            return False

        
def player_assignment(player_list):
    player_map = {player_list[0]:'X', player_list[1]:'O'}
    print(f'{player_list[0]} is {player_map.get(player_list[0])}')
    print(f'{player_list[1]} is {player_map.get(player_list[1])}')
    return player_map
    
    
def display_board(board):
    # Displays the tic-tac-toe board.
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
        print("-------------")


def start(board, player_map):
    display_board(board)
    while True:
        board = player_1_turn(board, player_map)
        print(board)
        board = player_2_turn(board, player_map)
        print(board)
        break
        # player 1 Turn
        # Board Refresh
        # Player 2 Turn 
        # Board Refresh   
        # If counter >= 5 Check Winner
   
    
def player_1_turn(board, player_map):
    confirm = False
    while not confirm: 
        print(f'{list(player_map.keys())[0]}\'s turn ')
        position = get_position()
        new_board = board[:]
        new_board[position] = player_map.get(list(player_map.keys())[0])
        display_board(new_board)
        confirm = confirmation()
        if confirm:
            return new_board
    

def player_2_turn(board, player_map):
    confirm = False
    while not confirm:
        print(f'{list(player_map.keys())[1]}\'s turn ')
        position = get_position()
        new_board = board[:]
        new_board[position] = player_map.get(list(player_map.keys())[1])
        display_board(new_board)
        confirm = confirmation()
        if confirm:
            return new_board


def get_position():
    # Get Positions from User 
    position = -1
    while position not in range(9):
        position = input("Please enter a number (0-8): ")
        if position.isdigit():
            position = int(position)
        else:
            print("Not a number! Try Again!")
    return position



# Select Players
player_list = player_selection()

# Assign 'X' and 'O' to Players
player_map =  player_assignment(player_list)

# Game Starts
print("-----------Game Start------------")
board = [" " for a in range(9)]
start(board, player_map)

