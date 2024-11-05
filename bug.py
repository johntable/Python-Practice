try: 
    age = int(input('What is your age? '))
except ValueError:
    print('Invalid Input. Please enter a number.')
    age = int(input('What is your age? '))
if age > 18:
    print(f'You can drive, drink, go to jail (preferably not at the same time) at age {age}')