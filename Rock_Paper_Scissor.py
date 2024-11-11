import random
import time

def game_start():
    user_name = input("Enter your name: ")

    print(f"Hello {user_name}, Welcome to Rock, Paper, Scissors!")
    time.sleep(1)

    print('''
    Rules:
    - Rock beats Scissors
    - Scissors beats Paper
    - Paper beats Rock

    Ready? Let's go!
    ''')

    time.sleep(1)

    choices = ["rock", "paper", "scissor"]

    while True:
        time.sleep(0.5)
        user_choice = input("Please select your choice (Rock, Paper or Scissor): ").strip().lower()

        if user_choice in choices:
            print("choosing...")

            computer_choice = random.choice(choices)
            time.sleep(2)

            print(f"{user_name} chose {user_choice}")
            time.sleep(1)

            print(f"Computer chose {computer_choice}")
            time.sleep(1)

            if user_choice == computer_choice:
                print(f"It's a tie! Both chose {user_choice}")
            elif (user_choice == "scissor" and computer_choice == "paper") or\
                (user_choice == "paper" and computer_choice == "rock") or\
                (user_choice == "rock" and computer_choice == "scissor"):
                print(f"{user_name} wins! {user_name} chose {user_choice} and the computer chose {computer_choice}.")
            else:
                print(f"{user_name} loses! {user_name} chose {user_choice} and the computer chose {computer_choice}.")


            # Ask if the user wants to play again
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break

        else:
            print("Invalid input! Please select the correct option.")

game_start()