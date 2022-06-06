
myString = "some text"
exp = type(myString)
print (exp)

#----This is how to convert int to str----#
myNum = "33"
con_num_to_text = type(myNum)
print (con_num_to_text)

txt_a = 'She said "meet me at 5pm"'

print (txt_a)

#---This Show that every character has it own sequence in the string mean that its indexed---#
print (txt_a[0],txt_a[-1],txt_a[2])
#---the function of len helps you to count characters in a string--#
print (len(txt_a))
#--this is how we get the last character from a string
print (txt_a[len(txt_a)-1])
#-- the slicing method for selecting character in the string
account_ = "PT07387388003"
print (account_[0:2],account_[-2:-1],account_[-2:],account_[-5:],account_[:2])
#-----this how we can use the concat sign(+) with string and integer
char_var = "user" + str(22)
print (char_var)

