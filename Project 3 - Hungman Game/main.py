import random
from collections import Counter

fruits = '''mango banana strawbarry apple leamon tomato'''
animals = '''tiger lion chita rabit snake elephant giraffe'''

fruitList = fruits.split()
animalList = animals.split()

word_Category = {word:'fruit' for word in fruitList}
word_Category.update({word: 'animal' for word in animalList})

wordList = fruitList + animalList
word = random.choice(wordList)
category = word_Category[word]
print(word)
if __name__ == '__main__':
	print(f'Guess the word! : Hint - Category {category}')
	
	for i in word:
		print("_", end="")
		print()
	
	rounds = len(word) + 2
	flag = 0
	letterGuessed = ''
	chances = 3

	print(f'---> Total Number of Rounds : {rounds} <---')
	try:
		while(rounds and flag == 0):
			guess = input("Inter a letter : ")

			if not guess.isalpha:
				print("Only Alhpabetic Character Allowed")
			if len(guess) != 1:
				print("Only Once Character Allowed at a Time")
			if guess not in word:
				chances -= 1
				print(f'Chances Remaining : {chances}')
				print("Correct Answer To Reset Chances")
			if chances == 0:
				print("You have Zero Chances")
				break
				break
			if guess in word:
				if chances < 3 :
					chances = 3
					print(f'Chances Reset Remaining Chances: {chances}')
				w = word.count(guess)
				for _ in range(w):
					letterGuessed += guess
			for char in word:
				if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
					print(char, end=" ")
					
				elif(Counter(letterGuessed) == Counter(word)):
					flag = 1
					print(f'The word is : {word}')
					print("*** Congratulations ***")
					break
					break
				else:
					print("_", end=" ")
			rounds -= 1

		if rounds <= 0 and (Counter(letterGuessed) != Counter(word)):
			print()
			print("You Lose the Game")
			print(f'The word is {word}')

	except KeyboardInterrupt:
		print()
		print("Bye! Try Next Time")
		exit()
