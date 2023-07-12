# selecting random strings without using the module 'choice()'

import random

names_string = input("Give me everybody's name separated by a "
                     "comma. ")

# splitting the names with a comma.
names = names_string.split(", ")

# get the total number of items in the list.
num_items = len(names)

random_choice = random.randint(0,  num_items - 1)
person = names[random_choice]
print(person + " is going to by the meal Today.")

