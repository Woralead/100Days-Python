# Check if the year is a leap year or not.

# Gathering some user input.
year = int(input("Which year do you want to  check?"))

# Nested if statements for printing the result.
if year % 4 == 0:
    if year % 400 == 0:
        if year % 100 == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")


