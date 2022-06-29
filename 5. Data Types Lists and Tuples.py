
students = "joe","jane","zoe"
students = ["joe","jane","zoe"]
print (type(students),students)
print (students[0], students[-1],students[:2])

months = ("Jan","Feb","Mar")
print(type(months),months[0],months[-1],months[:2])

students[0] ="Jerry"
print(students)
#--months[0] = "January"
#--print(months)
# the append help to add data in a str(var) ,It is one entry at a time.

students.append("Kate")
students.append("Enoch")
students.pop(1)
students.insert(0, "Daniel")
students.remove("zoe")
students2 =["John","Hellen","Doe","Musa"]
Concat_a = students + students2 
print (students)
print (Concat_a)





