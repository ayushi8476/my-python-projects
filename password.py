import random
import string   # gives access to letters, digits, symbols

def password_generator():
    print("🔑 Welcome to Password Generator 🔑")
    
    length = int(input("Enter password length: "))

    # characters to choose from (A-Z, a-z, 0-9, symbols)
    characters = string.ascii_letters + string.digits + string.punctuation

    # randomly pick characters
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"✅ Your password is: {password}")

password_generator()
