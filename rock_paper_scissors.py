rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

signs = [rock, paper, scissors]
p_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
)
if (p_choice < 0) or (p_choice > 2):
    exit()
player = signs[p_choice]
print(player)


opponent = random.choice(signs)
print(f"Computer chose: {opponent}")

if (
    ((player == rock) and (opponent == scissors))
    or ((player == scissors) and (opponent == paper))
    or ((player == paper) and (opponent == rock))
):
    print("You win")
elif player == opponent:
    print("It's a draw")
else:
    print("You lost.")
