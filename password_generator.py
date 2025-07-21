import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define possible characters
    letters = string.ascii_letters       # a-z, A-Z
    digits = string.digits               # 0-9
    symbols = string.punctuation         # !@#$%^&*()

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
