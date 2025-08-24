import random

def rps():
    print("Rock, Paper, Scissors Game 🎮")
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("Enter your choice (rock/paper/scissors or 'exit' to quit): ").lower()

        if user == "exit":
            print("Thanks for playing! 👋")
            break

        if user not in choices:
            print("❌ Invalid choice, try again.")
            continue

        computer = random.choice(choices)  # ✅ Corrected
        print(f"Computer's choice: {computer}")

        if user == computer:
            print("It's a tie! 😐")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("🎉 Winner: You")
        else:
            print("🤖 Winner: Computer")

rps()
