import tkinter as tk
import ttt_window

def start_game():
    # Close the welcome window
    welcome_window.destroy()
    # Call the function to start the game
    ttt_window.board()

def show_rules():
    # Display the game rules in a pop-up window
    rules_window = tk.Toplevel()
    rules_window.title("Game Rules")
    rules_text = """
    Welcome to Tic Tac Toe!

    Rules:
    1. The game is played on a 3x3 grid.
    2. Players take turns marking a cell with their symbol (X or O).
    3. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins.
    4. If all cells are filled and no player has won, the game is a draw.

    Let's start the game!
    """
    rules_label = tk.Label(rules_window, text=rules_text, justify='left')
    rules_label.pack(padx=10, pady=10)


# Create the welcome window
welcome_window = tk.Tk()
welcome_window.title("Welcome to Tic Tac Toe")

# Welcome message
welcome_label = tk.Label(welcome_window, text="Welcome to Tic Tac Toe!", font=("Helvetica", 16))
welcome_label.pack(padx=10, pady=10)

# Start button
start_button = tk.Button(welcome_window, text="Start Game", command=start_game)
start_button.pack()

# Rules button
rules_button = tk.Button(welcome_window, text="View Rules", command=show_rules)
rules_button.pack()

# Run the Tkinter main loop
welcome_window.mainloop()