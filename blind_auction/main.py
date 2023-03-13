import os
from art import logo


def clear():
    os.system("clear")


def add_bidder():
    bidder_name = str(input("What is your name?: ")).capitalize()
    bid_amo = int(input("What is your bid: $"))
    bids["name"].append(bidder_name)
    bids["bid"].append(bid_amo)


bids = {"name": [], "bid": []}
another_bid = True

# Game Logic
########################################
print(logo)

while another_bid:
    add_bidder()
    response = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
    if response == "yes":
        another_bid = True
    elif response == "no":
        another_bid = False
    else:
        another_bid = False
    clear()

win_bid = max(bids["bid"])
winner = bids["name"][bids["bid"].index(win_bid)]

print(f"The winner is {winner} with a bid of ${win_bid}!!")
