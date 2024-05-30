def say_hello(person, person2="The director"):
    print("Hello", person + ", how are you doing?", person2 ,"is waiting for you." )

def fahr2celsius(fahr):
    celsius = (5 * (fahr -32)) / 9
    return celsius

print("Celsius:",round(fahr2celsius(100),2))
print("Kelvin:",round(fahr2celsius(100) + 273.5,2))
print(say_hello("Lane","Tina"))