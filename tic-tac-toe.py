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
    player_map = {'X':player_list[0], 'O':player_list[1]}
    print(f'{player_list[0]} is {list(player_map.keys())[0]}')
    print(f'{player_list[1]} is {list(player_map.keys())[1]}')
    return player_map
    
    
def display_board(board):
    # Displays the tic-tac-toe board.
    print("-------------")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
        print("-------------")


def start(board, player_map):
    board_dict={}
    for i in range(9):
        board_dict.update({i: board[i]})
    display_board(list(board_dict.values()))
    winner_decided = False
    winner_who  = ''
    counter = 1
    while counter <= 9:
        board_dict = player_1_turn(board_dict, player_map)
        if counter >= 5:
            win_tuple = check_winner(board_dict)
            winner_decided = win_tuple[0]
            winner_who = win_tuple[1]
            if winner_decided:
                break
        counter = counter + 1
        board_dict = player_2_turn(board_dict, player_map)
        counter = counter + 1
        if counter >= 5:
            win_tuple = check_winner(board_dict)
            winner_decided = win_tuple[0]
            winner_who = win_tuple[1]
            if winner_decided:
                break
    if winner_decided:
        print("Congratulations!")
        print(f'Winner is {player_map.get(winner_who)}')
    else:
        print("Match Drawn!")
  
    
def player_1_turn(board_dict, player_map):
    confirm = False
    while not confirm: 
        print(f'{player_map.get(list(player_map.keys())[0])}\'s turn ')
        position = get_position(board_dict)
        new_board = board_dict.copy()
        new_board[position] = list(player_map.keys())[0]
        display_board(list(new_board.values()))
        confirm = confirmation()
        if confirm:
            return new_board
    

def player_2_turn(board_dict, player_map):
    confirm = False
    while not confirm:
        print(f'{player_map.get(list(player_map.keys())[1])}\'s turn ')
        position = get_position(board_dict)
        new_board = board_dict.copy()
        new_board[position] = list(player_map.keys())[1]
        display_board(list(new_board.values()))
        confirm = confirmation()
        if confirm:
            return new_board


def get_position(board_dict):
    # Get Positions from User 
    position = 'a'
    position_pass = False
    while (position not in range(9)) or  position_pass == False:
        position = input("Please enter a number (0-8): ")
        if position.isdigit(): 
            position = int(position)
            if board_dict[position] == ' ':
                position_pass = True
            else:
                print("Position already taken! Try Again!")
        else:
            print("Not a number! Try Again!")
    return position


def check_winner(board_dict):
    winner = False
    who_winner = ' '
    if board_dict[0] == board_dict[1] == board_dict[2] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[0] == board_dict[1] == board_dict[2] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[3] == board_dict[4] == board_dict[5] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[3] == board_dict[4] == board_dict[5] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[6] == board_dict[7] == board_dict[8] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[6] == board_dict[7] == board_dict[8] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[0] == board_dict[3] == board_dict[6] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[0] == board_dict[3] == board_dict[6] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[1] == board_dict[4] == board_dict[7] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[1] == board_dict[4] == board_dict[7] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[2] == board_dict[5] == board_dict[8] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[2] == board_dict[5] == board_dict[8] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[0] == board_dict[4] == board_dict[8] == 'X':
        who_winner = 'X'
        winner = True
    elif board_dict[0] == board_dict[4] == board_dict[8] == 'O':
        who_winner = 'O'
        winner = True
    elif board_dict[2] == board_dict[4] == board_dict[6] == 'X':
        print("winner")
        who_winner = 'X'
        winner = True
    elif board_dict[2] == board_dict[4] == board_dict[6] == 'O':
        who_winner = 'O'
        winner = True
    else:
        winner = False
    return (winner, who_winner)

  
# Select Players
player_list = player_selection()

# Assign 'X' and 'O' to Players
player_map =  player_assignment(player_list)

# Game Starts
print("-----------Game Start------------")
board = [" " for a in range(9)]
start(board, player_map)

