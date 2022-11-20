print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("YOur mission is to find the treasure.")
choice = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right" '
).lower()

if choice == "left":
    choice = input(
        'You arrive at a dock. What do you want to do? "swim" or "wait" '
    ).lower()
    if choice == "wait":
        print("You wait. A ship arrives.")
        print(
            'The ship brings you to an island with three doors, each of a different color: "red", "blue", and "yellow".'
        )
        choice = input("The ship has already left. Which door do you choose? ").lower()
        if choice == "yellow":
            print(
                '''"You enter a dark room, and the door closes behind you. You found a room full of treasure!!! You win!!!"'''
            )
        elif choice == "red":
            print("You enter a dark room, and the door locks behind you.")
            print(
                """
                "Suddenly, the room bursts into a fiery furnace and you are burnt to a crisp.
                Game over."
                """
            )
        elif choice == "blue":
            print("You enter a dark room, and the door locks behind you.")
            print("You hear panting...then growling...")
            print("Suddenly the room is filled with glowing eyes and bared fangs!")
            print("The room is filled with hungry beasts and they lunge at you!")
            print("You are eaten.")
            print("Game over.")
    else:
        print("You are attacked by a trout.\nGame over.")
else:
    print("You fall into a hole. Game over.")
