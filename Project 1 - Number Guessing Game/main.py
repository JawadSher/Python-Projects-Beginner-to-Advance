import random

randomNumber = random.randint(0, 99)
Rounds = int(input("Please Enter number of Rounds: "))
print("---------------------------------------------")

while(Rounds):
    userInput = int(input("Please Guess the number : "))
    if(userInput != randomNumber and  userInput >= randomNumber):
        print("The userInput is greater than Random Number")
        print(f"Random Number : {randomNumber}")
        print(f"userInput Number : {userInput}")
    elif(userInput != randomNumber  and userInput <= randomNumber):
        print("The userInput is less than Random Number")
        print(f"Random Number : {randomNumber}")
        print(f"userInput Number : {userInput}")
    else:
        print("Woooooooh You got the Number")
        print(f"Random Number : {randomNumber}")
        print(f"userInput Number : {userInput}")
        break

    Rounds = Rounds - 1
    print(f"Number of Rounds Remaining : {Rounds}")
    print("----------------------------------------")

if(Rounds==0 & userInput != randomNumber):
    print("Try Next Time")
