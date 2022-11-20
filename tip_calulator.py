print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = (
    float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
)
num_people = int(input("How many people to split the bill? "))

tip = bill * tip_percentage
bill_w_tip = bill + tip
individual_bill = round(bill_w_tip / num_people, 2)

print(f"Each person should pay: ${individual_bill}")
