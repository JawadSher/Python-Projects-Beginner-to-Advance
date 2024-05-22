import random

fruits = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

animals = '''tiger lion elephant leopord  
gorilla hyena panther camel alligator panda mole'''

word = fruits.split(" ")

word = random.choice(word)
print(word)

if __name__ == '__main__' :
	print("Guess the Fruit Word!")

