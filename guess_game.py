import random
def guess_game():
    print("Guess the number")
    number=random.randint(1,10)
    guess=(input('Guess The Number:'))
    if guess==number:
        print("you won the game!")
    else:
        print("Better luck next time!")
guess_game()