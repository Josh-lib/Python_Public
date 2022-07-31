# --Create a program with a predefined dictionary for a person include
# -the following information: name, gender, age, address and phone.
# Ask the user what information he wants to know about the person
# (example:"name"), then print the value associated to that key or
#  display a message in case the key is not found.

Person = {"name": "Muwanguzi Joshua", "gender": "Male", "age": 23.9, 
          "address": "Namboole,Kirinya", "phone": "0703446795"}
qtn = input("What infomation would like to know about the users? ").lower()

ans = Person.get(qtn , "Information requested is not available")
print(ans)