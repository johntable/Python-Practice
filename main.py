# Functions with Outputs


def format_name(f_name, l_name):
    name = f_name + " " + l_name
    return name.title()


first = str(input("First name: "))
last = str(input("Last name: "))

print(format_name(first, last))
