print("This program checks your B.M.I Score and returns your body type.")
weight_in_kg = int(input("Please enter your weight in Kgs : "))
height_in_meters = float(input("Please enter your height in meters : "))
bmi = round(weight_in_kg/(height_in_meters*height_in_meters), 2)
if weight_in_kg <=0 or height_in_meters <=0:
    print("Please ENTER valid PARAMETERS.")
elif bmi < 18.5:
    print(f"Your BMI is {bmi}. You are UNDERWEIGHT.")
elif (bmi >= 18.5 and bmi<= 24.9):
    print(f"Your BMI is {bmi}. You have a NORMAL WEIGHT.")
elif (bmi >= 25 and bmi <= 29.9):
    print(f"Your BMI is {bmi}. You are OVERWEIGHT.")
elif (bmi >= 30 and bmi <= 34.9):
    print(f"Your BMI is {bmi}. You are OBESE. Please start dieting and weight losing exercises.")
else:
    print(f"Your BMI is {bmi}. You are EXTREMELY OBESE. Please consult dietician and start dieting and weight losing "
          f"exercises.")
