import random

print("Welcome to ---> Rock Paper Scissor Game <--- ")
print("---------> H U M A N  vs  C O M P U T E R <---------")
print()
print("***** WINING GAME RULES *****")
print("ROCK vs PAPER --> PAPER WINS\n"
	+"ROCK vs SCISSOR--> ROCK WINS\n"
	+"PAPER vs SCISSOR --> SCISSOR WINS\n")

rounds = int(input("Enter Number of Rounds : "))
userChoice = ""
computerChoice = ""
while(rounds):
	rounds = rounds -1

	choices = ['ROCK', 'PAPER', 'SCISSOR']
	for index, val in enumerate(choices):
		print(index+1,"-", val)

	print()
	userInput = int(input("Enter your Choice : ")) -1
	match userInput:
		case userInput : 
			userChoice = choices[userInput]
			print("Your Choice is : ", userChoice)

	print()
	computerInput = random.randint(0, 2)
	match computerInput:
		case computerInput : 
			computerChoice = choices[computerInput]
			print("Computer Choice is : ", computerChoice)
			
	print()
	if(userChoice == "ROCK" and computerChoice == "PAPER"):
		print(f'Computer Choice : {computerChoice} - COMPUTER WINS')
		print("Try! Next Time")

	elif(userChoice == "PAPER" and computerChoice == "ROCK"):
		print(f'Your Choice : {userChoice} - YOU WIN')
		print("Congratulations")

	elif(userChoice == "ROCK" and computerChoice == "SCISSOR"):
		print(f'Your Choice : {userChoice} - YOU WIN')
		print("Congratulations")

	elif(userChoice == "SCISSOR" and computerChoice == "ROCK"):
		print(f'Computer Choice : {computerChoice} - COMPUTER WINS')
		print("Try! Next Time")

	elif(userChoice == "SCISSOR" and computerChoice == "PAPER"):
		print(f'Your Choice : {userChoice} - You WIN')
		print("Congratulations")

	elif(userChoice == "PAPER" and computerChoice == "SCISSOR"):
		print(f'Computer Choice : {computerChoice} - COMPUTER WINS')
		print("Try! Next Time")
	
	else:
		print("ooooooohh - GAME DRAW")

	again = input("You want to play again yes/no: ")
	match again:
		case 'yes':
			rounds += 1
		case 'no' :
			rounds += 0
			print("ROUNDS OVER")
			exit()
	
		
	

	
