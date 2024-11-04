from guess_art import logo 
import os, random
modes = ['easy','hard']

def is_number(num):
    num

def game():
    def compare(guess_num, tru_num):
        if (guess_num == tru_num):
            print(f'You got it! {guess_num} is my number: {tru_num}')
            return -guesses
        elif(guess_num > tru_num):
            print(f'Guess: {guess_num}. Your guess is too high.')
            return -1 
        elif(guess_num < tru_num):
            print(f'Guess: {guess_num}. Your guess is too low.')
            return -1

    def choose_mode(mode):
        if mode == 'easy':
            return guesses + 11
        elif mode == 'hard':
            return guesses + 6

    guesses = -1
    the_num = random.randint(1,100)
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
    
    guesses = choose_mode(difficulty)
    print(guesses)
    print(the_num)

    while guesses != 0:
        ur_guess = int(input(f'\tThe number is between 1 and 100\n\tNumber of guesses remaining: {guesses}\n\tType your guess: '))
        os.system('clear')
        print(logo)
        guesses += compare(ur_guess,the_num)
        if guesses == 0 and (ur_guess != the_num):
            print('You\'ve run out of guesses\n Better luck next time!')



while input('Do you want to play? \'y\' or \'n\': ') == 'y':
    os.system('clear')
    game()