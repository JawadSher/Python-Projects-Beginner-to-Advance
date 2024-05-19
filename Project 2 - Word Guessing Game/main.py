import random

def display_words(secret_words, guessed_words):
    for word in secret_words:
        if word in guessed_words:
            print(word, end=" ")
        else:
            print("_", end=" ")


