programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from the dictionary
# print(programming_dictionary["Function"])

# Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary/
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

##############################################

# Nesting

capitals = {"France": "Paris", "Germany": "Berlin"}

# Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3,
    },
    "Japan": {"cities_visited": ["Osaka", "Okinawa", "Saitama"], "total_visits": 4},
}

# Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 3,
    },
    {
        "country": "Japan",
        "cities_visited": ["Osaka", "Okinawa", "Saitama"],
        "total_visits": 4,
    },
]
