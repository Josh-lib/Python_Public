grade1 =float (input ("Type the grade of the first test: "))
grade2 =float (input ("Type the grade of the second test: "))
absences =int (input ("Type the number of absences: "))
total_classes = int(input ("Type the total number of classes: "))
constant = float(2)

avg_grade = (grade1 + grade2) / (constant)
attendance = (total_classes - absences) / total_classes
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