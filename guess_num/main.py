from guess_art import logo 
import os
modes = ['easy','hard']

def choose_mode(mode):
    if mode == 'easy':
        return guesses + 6
    elif mode == 'hard':
        return guesses + 11

def is_number(num):
    num

def game():
    print(logo)
    difficulty = input('''
Welcome to the Number Guessing Game!!!
Choose a difficulty. Type \'easy\' or \'hard\': 
''').lower()
    
    if difficulty not in modes:
        difficulty = input('''
Invalid Input.
Welcome to the Number Guessing Game!!!
Choose a difficulty. Type \'easy\' or \'hard\': 
''').lower()
     
    guesses = -1
    print(guesses)


while input('Do you want to play? \'y\' or \'n\': ') == 'y':
    os.system('clear')
    game()