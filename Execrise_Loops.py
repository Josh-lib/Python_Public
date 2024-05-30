import random as rd
people = []
for num in range(0,8):
    person = input ("Enter eight names for the people you are willing to play with this Game:")
    people.append(person)
index = rd.randint(0,7)

random_person = people[index]

print("Picking a random person:", random_person)

#~~~~~~~~~~~Question~Two~~~~~~~~~~~~~~~~~#

colors = ["white","black","red","green","blue","yellow","purple","grey"]

while True:
    color = colors[rd.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color,can you guess it: ")
    while True:
        if (color == guess):
            break
        else:
            guess =input("Nope, Try again: ")
    print("You guessd it! I was thinking about colour", color)
    play_again = input("Let's play again? Type 'no' to quit.")
    if play_again.lower() =='no':
        break
print("It was fun, playing with you")