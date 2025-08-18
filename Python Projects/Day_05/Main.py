import random

from hangman_wordlist import word_list
from hangman_art import stages,logo

lives=6

print(logo)

word=random.choice(word_list)
print(word)

#placeholder

placeholder=""
count=len(word)
for num in range(count):
    placeholder+="_"
print("Word to guess: " + placeholder)

#Guess

game_over=False
correct_list=[]

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess=input("Guess your word : ").lower()

    if guess in correct_list:
        print(f"You've already guessed {guess}")

    display=""

    for char in word:
        if guess==char:
            display+=char
            correct_list.append(char)
        elif char in correct_list:
            display+=char
        else:
            display+="_"

    print("Word to guess: " + display)

    if guess not in word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over=True
            print(f"***********************IT WAS {word}! YOU LOSE**********************")

    if "_" not in display:
        game_over=True
        print("****************************YOU WIN****************************")
    
    print(stages[lives])