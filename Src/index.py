import random

number = random.randint(1, 100)

print("Guss the number: ")

chances = 3

while(chances > 0):
    gussedNumber = int(input())
    chances = chances - 1
    if(gussedNumber == number):
        print("You won!")
        chances = 0
    elif(chances < 1 and gussedNumber != number):
        print("You lost!")
    else:
        print("Wrong")