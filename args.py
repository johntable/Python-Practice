x = input("Enter num: ")
count = 0

while x != "":
    new_num = int(x)
    print("doble num: " + str(new_num*2))
    count += 1
    x = input("\nEnter num: ")

print("we read " + str(count) + " numbers")
