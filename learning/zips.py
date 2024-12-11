# zip (*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_date = ["1/1/2021", "1/2/2011", "1/3/2021"]

# users = dict(zip(usernames,passwords,login_date))

# print(type(users))

# for key,value,login in users.items():
#     print (key+" : "+value+" : "+login)
# wrong ^^^^^^

# users = dict(zip(usernames, passwords))

# print(type(users))

# for key,value in users.items():
#     print(key+" : "+value)
# correct ^^^^^^^^^^^

######################################### zip in python############################################

# Zip Practice #1
# Print to the screen phrases like the following example:

# "The capital of Germany is Berlin"

# Use the zip function, loops, and the following lists of countries and capitals to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

capital_country = zip(capitals,countries)

for cap,count in capital_country:
    print("The capital of "+count+" is "+cap)

# Zip Practice #2
# Create a zip object made up of lists, of a set of brands and products that you prefer, inside the my_zip variable.
    
brands = ["Colgate-Palmolive", "Pepsico", "P&G", "Mondelez", "Kraft Heinz"]
products = ["Toothpaste", "Pepsi", "Tide", "Oreo", "Jell-o"]

my_zip = zip(brands,products)

for i in my_zip:
    print(i)

# Zip Practice #3
# Create a zip object with the translations of the numbers from 1 to 5 in Spanish, Portuguese and English (in that same order), and then convert the generated object into a list called numbers:

# one / um / one

# two / two / two

# three / three / three

# four / four / four

# five / five / five

# The result should follow the structure:

# [('one', 'um', 'one'), ('two', 'dois', 'two'), ... ]

# 1: uno / um / one
# 2: dos / dois / two
# 3: tres / três / three
# 4: cuatro / quatro / four
# 5: cinco / cinco / five

english = ["one", "two", "three", "four", "five"]
spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]

numbers = zip(spanish,portuguese,english)

print(list(numbers))