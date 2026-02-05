# conditional statement

# If statement                    # use when you have one condition to check
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If-elif-else statement          # use when you have multiple conditions to check
temperature = 25
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a warm day")
elif temperature > 10:
    print("It's a cool day")
else:
    print("It's a cold day")

# Nested if statement             # use when you have conditions within conditions
num = 15
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")

# and, or, not operators                            # use to combine multiple conditions
score = int(input("Enter your score (0-100): "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:                    # what happen here is if score < 90 is true then it will check if score >= 80
    print("Grade: B")                   
if not score < 0:
    print("Score is valid")



# conditional statement excercise

weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in cm: "))

bmi = weight / (height / 100) ** 2 

print(f"Your BMI is: {bmi:.2f}")        

if bmi > 30:
    print("You are obese")

elif bmi < 29.9:
    print("You are overweight")

elif bmi < 24.9:
    print("You weight is normal")

elif bmi < 18.5:
    print("You are underweight")

else:
    print("You have a normal weight")