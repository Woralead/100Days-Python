# Height, age  & extra -> check for roller-coaster pricing.

# Some text and asking for input from the user.

print("Welcome to our Roller-Coaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is you age?"))
    if age < 12:
        bill += 5
        print(f"Child ticket are ${bill}.")
    elif age <= 18:
        bill += 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <= 55:
        print(f"Everything is going to be ok. Have a free ride on us!")
    else:
        bill += 12
        print(f"Adult tickets are ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    wants_photo = wants_photo.title()

    if wants_photo == 'Y':
        # Add $3 to the bill
        bill += 3

    print(f"Your final amount is ${bill}")

else:
    print("Sorry, you have to grow taller to be able to ride.")