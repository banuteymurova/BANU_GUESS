import random
import sys


record = []
best_guess = []

def show_title():
    print("=" * 60)
    print("🎯                    BANU GUESS                    🎯")
    print("=" * 60)
    print("          Can you guess the secret number?")
    print("                ❤️ Good luck! ❤️")
    print("=" * 60)
    print()


def show_rules():
    print("📜 Instructions:")
    print("1. The computer will randomly select a secret number.")
    print("2. You have to guess the number.")
    print("3. You will get hints if your guess is too high or too low.")
    print("4. Try to guess the number in as few attempts as possible.")
    print("5. You can see your previous guesses and your best guess by typing 'record' at any time during the game.")
    print("6. To exit the game, type 'exit' at any time.")
    print()


def start_game():
    starting = input("Want to start? (yes/no): ").lower()

    if starting == "yes":
        print("\nGreat! Let's start the game. 🎉")
    else:
        print("\nNo worries! You can start the game anytime by running the program again. 👋")
        sys.exit()


def choose_difficulty():
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

    if difficulty == "easy":
        print("=" * 40)
        print("You have chosen easy difficulty.")
        print("The secret number will be between 1 and 20.")
        print("=" * 40)
        return 20

    elif difficulty == "medium":
        print("=" * 40)
        print("You have chosen medium difficulty.") 
        print("The secret number will be between 1 and 100.")
        print("=" * 40)
        return 100

    elif difficulty == "hard":
        print("=" * 40)
        print("You have chosen hard difficulty.")
        print("The secret number will be between 1 and 1000.")
        print("=" * 40)
        return 1000

    else:
        print("=" * 40)
        print("Invalid difficulty.")
        print("Please choose from easy, medium, or hard.")
        print("=" * 40)
        return None

def best_guesses(secret_number):
    best_guess.clear()
    for score in record:
        best_guess.append(abs(secret_number - score))
    smallest = min(best_guess)
    index = best_guess.index(smallest)
    closest = record[index]
    return closest


def play_game(max_number):
    secret_number = random.randint(1, max_number)
    found = False

    print("\nYou have ❤️❤️❤️❤️❤️ (5 lives).\n")
    lives = 5
    while lives > 0:
        print("=" * 40)
        print("❤️ Lives left:", "❤️" * (lives))

        guess = input(f"Enter your guess (1-{max_number}): ")
        if guess == "record":
            if record:
                print(f"\n🏆 Your previous guesses: {record}")
                print(f"🏆 Your best guess:", best_guesses(secret_number))
                continue
            else:
                print("\n🏆 No previous guesses found.")
                continue
        elif guess == "exit":
            print("\nThank you for playing! Goodbye! 👋")
            sys.exit()
        else:
            try:
                guess = int(guess)
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
                continue

            if guess < 1 or guess > max_number:
                print(f"❌ Invalid input. Please enter a number between 1 and {max_number}.")
                continue
        
        if guess < secret_number:
            print("📉 Too low! Try again.")
            record.append(guess)
            lives -= 1
        elif guess > secret_number:
            print("📈 Too high! Try again.")
            record.append(guess)
            lives -= 1
        else:
            print(f"\n🎉 Congratulations!")
            record.append(guess)
            lives -= 1 
            print(f"You guessed the secret number {secret_number} in {5 - lives} attempts!")
            found = True
            break

    if not found:
        print(f"\n💀 Game Over!")
        print(f"The secret number was {secret_number}.")
    
    record.clear()
    best_guess.clear()


def play_again():
    answer = input("\nDo you want to play again? (yes/no): ").lower()

    if answer == "yes":
        return True

    print("\nThank you for playing! Goodbye! 👋")
    sys.exit()




def main():
    show_title()
    show_rules()
    start_game()

    while True:
        max_number = choose_difficulty()

        if max_number is None:
            continue

        play_game(max_number)

        play_again()


main()