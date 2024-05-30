import random as nd

number = nd.randint(1,10)

guess = int (input("I'm thinking of a number. Can you guess it? "))

while True:
    if guess == number:
        break
    else:
        guess =int (input("Nope. Try again: "))
print("I have been thinking of number",number,"\n You have guessed Right.")

