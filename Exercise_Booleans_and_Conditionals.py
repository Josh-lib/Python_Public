# Create a program and store  your age in a variable. then,ask the user for his age and print whether:
# -He's older than you
# -He's younger than you
# You two have the same age
myAge = int(23)
ctAge = int(input("How older are you? "))

if(myAge > ctAge):
    print("He's older than you")
elif(myAge < ctAge):
    print("He's younger than you")
else:
    print("You two have the same age")