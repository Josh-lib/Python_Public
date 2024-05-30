
data_valid = False
while data_valid == False:
    grade1 =float (input ("Type the grade of the first test: "))
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 =float (input ("Type the grade of the Second test: "))
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True
data_valid = False
while data_valid == False:
    absences =int (input ("Type the number of absences: "))
    if absences <= 0 or absences >= 12:
        print("Number of Absences a 0 and 12")
        continue
    else:
        data_valid = True
total_classes = int(input ("Type the total number of classes: "))


avg_grade = (grade1 + grade2) / 2 # type: ignore
attendance = (total_classes - absences) / total_classes #type: ignore
Grade = print("The average grade", round(avg_grade,2))
Attend = print ("The attendance_rate", str(round((attendance*100),2))+'%')

if (avg_grade >= 6 and attendance >= 0.8):
    print("The student has been approved")        
elif(avg_grade < 6 and attendance < 0.8):
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("The student has failed due to an average grade lower than 6.0.")
else:
    print("The student has failed due to an attendance rate lower than 80%.")