water = 300
milk = 200
coffee = 100
money = 0

quarter_val = 0.25
dime_val = 0.1
nickle_val = 0.05
penny_val = 0.01


enter = str(input("What would you like? (espresso/latte/capuccino): "))

if enter.lower() == "report":
    print(
        f"""
    Water: {water}ml
    Milk: {milk}ml
    Coffee: {coffee}g
    Money: ${money}
    """
    )
elif enter.lower() == "espresso":
    print("Please insert coins.")
    quarts_num = int(input("How many quarter? "))
    dime_num = int(input("How many dimes? "))
    nick_num = int(input("How many nickles? "))
    pen_num = int(input("How many pennies? "))
