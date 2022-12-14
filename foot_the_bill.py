import random

# 🚨 Don't change the code below 👇
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
rand_lim = len(names) - 1
index = random.randint(0, rand_lim)
payer = names[index]
print(f"{payer} is going to buy the meal today!")
