from random import shuffle

my_list = [' ', 'O', ' ']

def shuffle_list(list):
    # This Function shuffles a list and returns a new list
    print(list)
    shuffle(list)
    return list

def guess_input():
    # This method takes gues from user input from 0,1,2 and return this number
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Enter any number in 0,1, or 2 \n')
    return int(guess)

def check_guess(list, guess):
    if list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong Guess!')
        print(list)

# Shuffle the List
shuffled_list = shuffle_list(my_list)

# Input Guess
guess = guess_input()

# Validate the guess
check_guess(shuffled_list, guess)


        
