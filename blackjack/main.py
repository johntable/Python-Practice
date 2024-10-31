import random, os
from blackjack_art import logo

# #BlackJack House Rules
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The following list is are the cards used.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal opportunity to be drawn
# Cards are not removed from the deck as they are draw; this is an infinite deck.

def draw(hand):
    hand.append(random.choice(cards))
    return 0

def starting_hand(hand):
    for i in range(2):
        draw(hand)

    return 0

def calc_score(hand):
    if sum(hand) == 21 and len(hand):
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(p_score, d_score):
    if p_score == d_score:
        print('It\'s a draw.')
    elif d_score == 0:
        print('Lose. Dealer has Blackjack.')
    elif p_score == 0:
        print('You win with a Blackjack!')
    elif p_score > 21:
        print('You went over 21. You lose.')
    elif d_score > 21:
        print('Dealer went over. You win!')
    elif p_score > d_score:
        print('You win!')
    else:
        print('You lose.')

    return 0

def play_game():
    print(logo)
    player_hand = []
    dealer_hand = []
    user_score = -1
    comp_score = -1
    starting_hand(player_hand)
    starting_hand(dealer_hand)
    is_game_over = False

    while not is_game_over:
        user_score = calc_score(player_hand)
        comp_score = calc_score(dealer_hand)
        
        print(f'\tYour current hand: {player_hand}, current score: {calc_score(player_hand)}')
        print(f'\tDealer\'s first card: {dealer_hand[0]}')

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            move = input('Type \'y\' to draw a card, type \'n\' to end your turn: ')
            if move == 'y':
                draw(player_hand)
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17 and comp_score < user_score:
        draw(dealer_hand)
        comp_score = calc_score(dealer_hand)

    print(f'\tYour final hand: {player_hand}, final score: {calc_score(player_hand)}')
    print(f'\tDealer\'s hand: {dealer_hand}, final score: {calc_score(dealer_hand)}')
    compare(user_score, comp_score)

    return 0

while input('Do you want to play? \'y\' or \'n\': ') == 'y':
    os.system('clear')
    play_game()