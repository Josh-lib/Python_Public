print("\nThis program calculates your body mass index.")

weight = float(input("What is your current weight in kg(ex. 70.5): "))
height = float(input("what is your current height in Meters (ex. 1.70): "))

BMI = weight / (height * height)

less = "Underweight"
Normal = "Normalweight"
Over = "Overweight"
print("Your BMI is:",round(BMI,2))

if (BMI <= 18.5):
    classification = less
elif (BMI > 18.5 and BMI <= 24.9):
    classification = Normal
elif (BMI > 24.9 and BMI <= 29.9):
    classification = Over
else:
    classification = "Obesity"
print("The classification of your BMI is:", classification)