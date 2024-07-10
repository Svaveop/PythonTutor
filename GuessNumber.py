import random

x = random.randint(1,5)
print("Guess number")
y = int(input())
while x !=y:
    print("Try again")
    y = int(input())
else:
    print("You Guessed!")
