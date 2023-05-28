# Pizza order project

print("Welcome to the Python Pizza Deliveries!")
size = input("What size do you want? S, M, or L ")
size = size.title()
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_pepperoni = add_pepperoni.title()
extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese = extra_cheese.title()

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
