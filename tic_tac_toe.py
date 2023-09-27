import os
import random
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def game_description():
    print("Welcome to Tic Tac Toe!")
    print("Here are the rules:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players take turns marking a cell with their symbol (X or O).")
    print("3. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins.")
    print("4. If all cells are filled and no player has won, the game is a draw.")
    print("Let's start!")


def display_board(board):
    clear_screen()
    for row in board:
        print(" | ".join(row))
        print("---------")


def get_player_names():
    player1_name = input("Enter the name of Player 1 (X): ")
    player2_name = input("Enter the name of Player 2 (O): ")
    return player1_name, player2_name


def choose_first_player(player1_name, player2_name):
    players = [player1_name, player2_name]
    random.shuffle(players)
    print(f"{players[0]} goes first!")
    return players[0], players[1]


# Initialize the Tic Tac Toe board as a 3x3 grid
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


# Function to get player's move
def get_player_move(board, player_symbol, player_name):
    while True:
        try:
            row = int(input(f"{player_name}, enter the row (0, 1, or 2) for your move: "))
            col = int(input(f"{player_name}, enter the column (0, 1, or 2) for your move: "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number for both row and column.")


# Function to check for a win
def check_win(board, player_symbol):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # Check rows
        if all(board[i][j] == player_symbol for j in range(3)):
            return True
        # Check columns
        if all(board[j][i] == player_symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player_symbol for i in range(3)) or all(board[i][2 - i] == player_symbol for i in range(3)):
        return True
    return False


# Function to check for a draw

def check_draw(board):
    # If there are no empty spaces left, it's a draw
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

game_description()
player1_name, player2_name = get_player_names()
first_player, second_player = choose_first_player(player1_name, player2_name)

current_player = first_player




while True:
    display_board(board)

    row, col = get_player_move(board, 'X' if current_player == player1_name else 'O', current_player)

    # Update the board with the player's move
    board[row][col] = 'X' if current_player == player1_name else 'O'

    # Check for a win
    if check_win(board, 'X' if current_player == player1_name else 'O'):
        display_board(board)
        print(f"{current_player} wins!")
        remach = input("Do you want to play again? (Y/N):")
        if remach == "y" or remach == "y":
            clear_screen()
            continue

        elif remach == "N" or remach == "n":
            print("Exiting game Please wait")
            time.sleep(3)
            clear_screen()
            break
        else:
            print("Bad choice. Y/N")

    # Check for a draw
    if check_draw(board):
        display_board(board)
        print("It's a draw!")
        clear_screen()
        break

    # Switch to the other player
    current_player = player1_name if current_player == player2_name else player2_name