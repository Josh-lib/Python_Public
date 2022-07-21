# ---Creating a program with predefined list of people. Ask the user for
# ---his name, add it to the end of the list and print the updated list
from numpy import append


name_list = ["Josh", "Joel", "Jane", "Alice", "Mary", "Moses"]
nw_name = input("What is your name? ")
name_list.append(nw_name)
print(name_list)
