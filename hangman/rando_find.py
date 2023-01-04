import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list


lives = 6
word = list(random.choice(word_list))
display = []
for n in word:
    display += "_"

print(logo)
print(f"Psst, the solution is {''.join(word)}")

end_of_game = False
print(stages[lives])
print(f"{' '.join(display)}")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for n in range(len(word)):
        if word[n] == guess:
            display[n] = guess

    if guess in display:
        print(f"You have already guessed {guess}")

    if guess not in word:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("You lose.")
            break
        else:
            print(stages[lives])
            print(f"{' '.join(display)}")
    else:
        print(stages[lives])
        print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
