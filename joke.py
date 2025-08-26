import pyjokes
def jokes():
    print("Welcome to jokes")
    print("1.for jokes")
    print("2.exit")
    choice=int(input("Enter your  choice:"))
    if choice==1:
         joke=pyjokes.get_joke()
         print(f"joke: {joke}")
    elif choice==2:
         print("Thanks for visit")
    else:
         print("invalid")
x=jokes()
print(x)