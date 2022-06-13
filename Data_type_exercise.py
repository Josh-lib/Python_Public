#---Question One ----#
#--Create a program that asks the user for his first name his middle name and his last name.
#--Then you're going to print the user's initials number two.
fname = input("Enter your First name: ")
mname = input("Enter your Middle name: ")
lname = input("Enter your Last name: ")

print ("Your initials are",fname,mname,lname)

#--Question Two--#
#--Let say your company has aproduct with
#--this lot number:"037-00901-00027".
# create a program to print:
# Country code:___
# Product code:___
# Batch number:___

lot_num = "037-00901-00027"
print ("Country Code: ",lot_num[0:3])
print ("Product code: ",lot_num[4:9])
print ("Batch number: ",lot_num[10:15])