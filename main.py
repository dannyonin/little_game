import os
import time
# Function for games menu
def menu():
    chose = None
    while True:
        print("Welcome To Games Center")
        print("Please Choose")
        print("1. tic tac toe")
        print("2. Rock , paper , scissors")
        chose = input("input:")
        if chose == "1":
            print("You Choose: Tic Tac Toe")
            time.sleep(2)
            os.system('cls')
            import tic_tac_toe

            tic_tac_toe
        elif chose == "2":
            print("You Choose: Rock Paper Scissors")
            time.sleep(2)
            os.system('cls')
            import rps_game
        elif chose == "EXIT".lower() or chose == "exit".upper() or chose == "q":
            break
        else:
            print("Bad Choice")
            time.sleep(1)
            os.system('cls')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

