from guess_art import logo 
import os, random
# Game function
def game():
    # Compares the guess number with the true number
    def compare(guess_num, tru_num):
        if (guess_num == tru_num):
            print(f'You got it! {guess_num} is my number!')
            print(f'You had {guesses-1} guess(es) remaining')
            return -guesses
        elif(guess_num > tru_num):
            print(f'Previous guess: {guess_num}. \nYour guess is too high.')
            return -1 
        elif(guess_num < tru_num):
            print(f'Previous guess: {guess_num}. \nYour guess is too low.')
            return -1

    # Gives the user 10 or 5 guesses based on difficulty
    def choose_mode(mode):
        if mode == 'easy':
            return guesses + 11
        elif mode == 'hard':
            return guesses + 6
        
    # Guesses = -1 for debugging
    guesses = -1
    the_num = random.randint(1,100)
    print(logo)
    modes = ['easy','hard']
    difficulty = ''

    # Difficulty choice section
    while difficulty not in modes:
        print('Welcome to the Number Guessing Game!!!')
        print('Choose a difficulty.')
        difficulty = input('Type \'easy\' or \'hard\': ').lower()
    guesses = choose_mode(difficulty)

    # Game loop
    while guesses != 0:
        ur_guess = int(input(f'\tThe number is between 1 and 100\n\tNumber of guesses remaining: {guesses}\n\tType your guess: '))
        os.system('clear')
        print(logo)
        guesses += compare(ur_guess,the_num)
        if guesses == 0 and (ur_guess != the_num):
            print('You\'ve run out of guesses.')
            print(f'{the_num} is the number. Better luck next time!')

# main
while input('Do you want to play? \'y\' or \'n\': ') == 'y':
    os.system('clear')
    game()