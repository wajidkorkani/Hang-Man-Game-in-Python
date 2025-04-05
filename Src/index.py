import random

number = random.randint(1, 100)

print("Guss the number: ")

chances = 5

while(chances > 0):
    gussedNumber = int(input())
    chances = chances - 1
    
    if(gussedNumber == number):
        print("You won!")
        chances = 0
        if(answer == "Yes"):
            chances = 5
            number = random.randint(1, 100)
    
    elif(chances < 1 and gussedNumber != number):
        print("You lost!")
        print("Would you like to try again?")
        answer = input().capitalize()
        if(answer == "Yes"):
            chances = 5
            number = random.randint(1, 100)
    else:
        print("Wrong")