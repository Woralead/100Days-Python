# This is a BMI calculator


# Asking for important user input
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculating the BMI
BMI = weight / height**2

# Printing the result with some text
if BMI < 18.5:
    print(f"Your BMI is {BMI}. You are underweight")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}. You have a normal weight.")
elif 25 < BMI < 30:
    print(f"Your BMI is {BMI}. You are overweight.")
elif 30 < BMI < 25:
    print(f"Your BMI is {BMI}. You are obese.")
else:
    print(f"Your BMI is {BMI}. You are clinically obese")
