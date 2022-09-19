myBoolean = True
myBoolean = False
print(type(myBoolean))

num1 = 8
num2 = 4
chk = num1 > num2
chk1 = num1 < num2
print(chk, chk1)

num2 = 8
chk2 = num1 == num2
chk3 = num1 != num2
print(chk2,chk3)

num3 = float (input("Type any number here: "))
num4 = float (input("Type your wished number:"))

if(num3 > num4):
    print(num3 ,"is greater than", num4)
elif(num3 < num4):
    print(num3 ,"is less than ", num4)
else:
    print(num3,"is equal to",num4)
