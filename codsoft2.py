import string
import random

def generate_password(length):
    if length < 8:
        return "Password length should be at least 8 for security."
    
    # Define character pools
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Secure random password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# User Input
try:
    user_input = int(input("Enter desired password length: "))
    generated = generate_password(user_input)
    print(f"\n🔑 Your password: {generated}")
except ValueError:
    print("Please enter a valid number.")