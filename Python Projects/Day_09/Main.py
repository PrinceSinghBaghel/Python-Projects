import random

EASY=10
HARD=5

#Function to check users' guess against actual answer
def check_answer(guess,num,turns):
    if guess>num:
        print("Too high.")
        return turns-1
    elif guess<num:
        print("Too low.")
        return turns-1
    else:
        print(f"You got the answer right: {num}")

#function to set difficulty level

def difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level=="easy":
        return EASY
    else:
        return HARD



#choosing a random number between 1 and 100
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thnking of a number between 1 and 100.")
    num=random.randint(1,100)
    turns=difficulty()
    


    guess=0
    while guess != num:
#Let the user guess a number
        print(f"You have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,num,turns)
        if turns==0:
            print("You have run out of attempts, You LOOOSE!")
            return
        elif guess!=num:
            print("Guess again")

#trace the number of turns and reduce it by 1

#repeat the guessing functionality if they get it wrong
game()

