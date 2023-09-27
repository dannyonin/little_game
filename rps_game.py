import random
import time
import os

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    ________
---'   _____)_____  
          ________)  
          _________)  
         _________)
---.____________)  
'''

scissors = '''  
    _______
---'   ____)_______  
          _________)  
       _____________)  
      (____)
---.__(___)  
'''


def random_choice_based_on_time():
    # Get the current time in seconds since the epoch
    current_time = int(time.time())

    # Seed the random number generator with the current time
    random.seed(current_time)

    # Define your three options
    options = [rock, paper, scissors]

    # Choose a random option from the list
    random_choice = random.choice(options)
    return random_choice



def get_user_choice():
    user_choice = input("Enter your choice (r, p, or s): ").lower()
    while user_choice not in ["r", "p", "s"]:
        user_choice = input("Invalid choice. Please enter r, p, or s: ").lower()
    if user_choice in "r":
        return user_choice , rock
    if user_choice in "p":
        return user_choice, paper
    if user_choice in "s":
        return user_choice, scissors

# Function for Compuer random choice
def get_computer_choice():
    computer_choice = random_choice_based_on_time()
    return computer_choice

# Function check for winner
def determine_winner(user_choice, computer_choice):
    if user_choice[1] == computer_choice:
        return "It's a tie!"
    elif user_choice[0] == "r":
        return "You win!" if computer_choice == scissors else "Computer wins!"
    elif user_choice[0] == "p":
        return "You win!" if computer_choice == rock else "Computer wins!"
    elif user_choice[0] == "s":
        return "You win!" if computer_choice == paper else "Computer wins!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    compuer_score = 0
    while player_score < 3 or compuer_score < 3:
        print(f"Score Player {player_score} - Computer {compuer_score}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice[1]}")
        print(f"The computer chose {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "Computer wins!":
            compuer_score += 1
        elif result == "You win!":
            player_score += 1
        else:
            time.sleep(3)
            os.system('cls')
            continue

        if player_score == 3  or compuer_score == 3:
            play_again = input("Do you want to play again? (y/n): ").lower()
            player_score = 0
            compuer_score = 0
            if play_again != "y":
                print("Thanks for playing!")
                break
        time.sleep(3)
        os.system('cls')

play_game()
