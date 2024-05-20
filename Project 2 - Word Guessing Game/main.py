import random

Name = input("Please Enter your name : ")
print(f'Hey, Welcome Mr.{Name}')

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water',]

word = random.choice(words)

guesses = ''
rounds = len(word) + 1
while(rounds):
    failed = 0
    print(f'----------> Total Rounds : {rounds} <----------')
    
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if(failed == 0):
        print(f'===> You Won the Game <===')
        print(f'The word is : {word}')
        break
    
    guess = input("Guess a letter : ")
    guesses += guess

    if guess not in word:
        print("Wrong")
        rounds -= 1
        print(f'************** Remaining Rounds :{rounds} **************')
    
        if(rounds == 0):
            print("Sorry You Loose")