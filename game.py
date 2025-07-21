import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "user"
    else:
        return "computer"

def play_round():
    print("\n--- Rock, Paper, Scissors ---")
    print("Choose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Oops! That's not a valid choice. Please try again.")
        return None, None

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie! 🤝")
    elif result == "user":
        print("You win! 🎉")
    else:
        print("You lose! 💔")

    return result, user_choice

def main():
    user_score = 0
    computer_score = 0
    round_number = 0

    print("👋 Welcome to Rock-Paper-Scissors!")
    print("Try to beat the computer. Best of luck!")

    while True:
        result, _ = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        elif result is None:
            continue  # Invalid input, don't count this round

        round_number += 1
        print(f"\n📊 Score after {round_number} round(s):")
        print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score}")

        again = input("\nWould you like to play another round? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\nThanks for playing! Final score:")
            print(f"🧑 You: {user_score} | 🤖 Computer: {computer_score}")
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
