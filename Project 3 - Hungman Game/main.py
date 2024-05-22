import random
from collections import Counter 

fruits = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

animals = '''tiger lion elephant leopord gorilla hyena panther camel alligator panda mole'''

fruitList = fruits.split()
animalList = animals.split()

word_category = {word:'fruit' for word in fruitList}
word_category.update({word:'animal' for word in animalList})

wordList = fruitList + animalList
word = random.choice(wordList)
category = word_category[word]
print(word)
if __name__ == '__main__' :
	print(f'Guess the Word! : Hint -> Category {category}')

	rounds = len(word) + 2
	print(f'------> Total Number of Rounds {rounds} <------')
	letterGuessed = ''
	correct = 0
	flag = 0

	try:
		for i in word:
			print("_", end=" ")
			print()
		while(rounds and flag == 0):
			guess = input("Enter a letter : ")
			if not guess.isalpha():
				print("Only Letters are Allowed !!!")
				continue
			if len(guess) != 1:
				print("Please Enter only Once Letter at a time")
				continue

			if guess in word:
				c = word.count(guess)
				for _ in range(c):
					letterGuessed += guess

			for char in word:
				if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
					print(char, end=" ")
					correct += 1
				elif (Counter(letterGuessed) == Counter(word)):
					print(f'The word is : ', end=" ")
					print(word)
					flag = 1
					print("Congratulations ***")
					break
					break
				else:
					print('_', end=" ")
			rounds -= 1

		if rounds <= 0 and (Counter(letterGuessed) != Counter(word)):
			print()
			print("You Lost the Game !!!")
			print('The word is {}'.format(word))

	except KeyboardInterrupt:
		print()
		print("Bye! Try Again...")
		exit()