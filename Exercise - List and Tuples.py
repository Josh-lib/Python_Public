#--create a program that asks the user for his birthday in 
#--the format "DD-MM-YYYY". Then print:
#--"You were born in [month]"

month = ('January','Feburary','March','April','May','June','July','August','September','October','November','December')
Date = input("When were you born, enter in this format DD-MM-YYYY:")

entry = int(Date[3:5])-1
date_of_birth = month[entry]

print("You were Born in ", date_of_birth)