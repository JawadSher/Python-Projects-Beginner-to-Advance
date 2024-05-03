import random
import time

randomNumber = random.randint(0, 99)
Rounds = int(input("Please Enter number of Rounds: "))

if(Rounds==0):
    print("Enter Valid Number of Rounds")
else:
    print("---------------------------------------------")
    print("Count Down Start .....")
    countDown = 3
    while(countDown):
        mins, secs = divmod(countDown, 60)
        timeFormat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeFormat, end='\r')
        time.sleep(1)
        countDown -= 1

    while(Rounds):
        userInput = int(input("Please Guess the number : "))
        if(userInput != randomNumber and  userInput >= randomNumber):
            print("The userInput is greater than Random Number")
            print(f"Random Number : {randomNumber}")
            # print(f"userInput Number : {userInput}")
        elif(userInput != randomNumber  and userInput <= randomNumber):
            print("The userInput is less than Random Number")
            print(f"Random Number : {randomNumber}")
            # print(f"userInput Number : {userInput}")
        else:
            print("---> Nice You got the Number <---")
            print(f"Random Number : {randomNumber}")
            print(f"userInput Number : {userInput}")
            break

        Rounds = Rounds - 1
        print(f"**** Number of Rounds Remaining : {Rounds} ****")
        print("----------------------------------------")
        print("Try next time") if(Rounds == 0) else ""



