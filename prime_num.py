# Write your code below this line 👇
dividers = [2, 3, 5, 7]


def prime_checker(number):
    errors = 0
    for div in dividers:
        check = number % div
        if check == 0:
            errors += 1
    if errors:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
