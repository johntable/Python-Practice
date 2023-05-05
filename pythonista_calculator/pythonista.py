from calc_art import logo

print(logo)
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What is the first number?: "))
    for operator in operations:
        print(operator)

    cont = "y"

    while cont == "y":
        operator_sym = input("Pick an operation from the line above: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operator_sym](num1, num2)

        print(f"{num1} {operator_sym} {num2} = {answer}")

        cont = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: "
        )
        if cont == "y":
            num1 = answer
        elif cont == "n":
            calculator()


calculator()
