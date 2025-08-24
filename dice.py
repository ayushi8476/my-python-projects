import random
def dice():
    print("the dice game")
    while True:
        dice=random.randint(1,6)
        print(f"rolled number:{dice}")
        choice=(input("roll again:").lower())
        if choice!="yes":
           print("thank you for playing")
           break
dice()       