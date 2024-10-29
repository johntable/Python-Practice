import random
from blackjack_art import logo

# #BlackJack House Rules
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The following list is are the cards used.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal opportunity to be drawn
# Cards are not removed from the deck as they are draw; this is an infinite deck.

dealer_hand = []
player_hand = []


def draw(hand):
    hand.append(random.choice(cards))

def starting_hand(hand):
    for i in range(0,2):
        draw(hand)

def bust(hand):
    if sum(hand) > 21:
        return True
    else:
        return False
    
def dealer_win(dealer_hand, player_hand):
    if dealer_hand > player_hand:
        return True
    elif dealer_hand < player_hand:
        return False
    elif dealer_hand == player_hand:
        print('It\'s a draw.\nPush!')
        return False
    
starting_hand(dealer_hand)
starting_hand(player_hand)

print(dealer_hand)

revealed_card = str(random.choice(dealer_hand))

while bust(player_hand) != True:
    print(f'Your current hand: {player_hand}, current score: {sum(player_hand)}')
    print(f'Dealer\'s first card: {revealed_card}')
    move = input('Type \'y\' to draw another card, type \'n\' to pass: ')
    move.lower()
    if move == 'y':
        draw(player_hand)
        print(player_hand)
    elif move == 'n':
        break
    else:
        print('Input invalid')
        move = input("Type in what you want to do:\nHit (draw a card)\nor\nStand(end your turn)\n")

while bust(dealer_hand) == False:
    if sum(dealer_hand) > sum(player_hand):
        print(f'Computer\'s final hand: {dealer_hand}, final score: {sum(dealer_hand)}')
        print('Computer Wins')
    elif sum(dealer_hand) < sum(player_hand):
        draw(dealer_hand)
    elif sum(dealer_hand) == sum(player_hand):
        print(f'Computer\'s final hand: {dealer_hand}, final score: {sum(dealer_hand)}')
        print()

