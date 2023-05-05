# Functions with Outputs


def format_name(f_name, l_name):
    """Correctly capatilizes and formats first and last name in
    a name and prints the two inputs in one line"""
    if f_name == "" or l_name == "":
        return ""
    formtted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formtted_f_name} {formatted_l_name}"


format_name("joHn", "tabeliSma")
