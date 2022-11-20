from cgi import print_exception
from operator import truediv


height = int(input("What is your height? "))
age = int(input("What is your age? "))
price = 0

if height > 120:
    print("You can ride.")
    if age < 12:
        price += 5
    elif age <= 18:
        price += 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        price += 12

    wants_photo = input("Do you want a photo? Type Y or N. ").lower()
    if wants_photo == "y":
        price += 3

    print(f"Your total bill is {price}.")
else:
    print("You're too short!")
