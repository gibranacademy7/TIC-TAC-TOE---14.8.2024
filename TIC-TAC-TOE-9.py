# TIC TAC TOE GAME

import tkinter as tk
from tkinter import messagebox

# Initialize the main window:
root = tk.Tk();
root.title("Tic-Tac-Toe");

# Variables to keep track of the game state:
player_turn = True  # True for Player 1 (X), False for Player 2 (O)
buttons = [[None for _ in range(3)] for _ in range(3)]; # List comprehension: [expression for item in iterable], outer list comprehension

# Label to show whose turn it is
turn_label = tk.Label(root, text="Player 1's Turn (X)", font=('Arial', 25), fg='blue', bg='white');
turn_label.grid(row=0, column=0, columnspan=3);

# Title of the game
title_label = tk.Label(root, text="Tic-Tac-Toe", font=('Arial', 30, 'bold'), fg='darkred', bg='white');
title_label.grid(row=1, column=0, columnspan=3);

# Function to check for a winner
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return (True, [(row, 0), (row, 1), (row, 2)])
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return (True, [(0, col), (1, col), (2, col)])
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return (True, [(0, 0), (1, 1), (2, 2)])
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return (True, [(0, 2), (1, 1), (2, 0)])
    return (False, [])


# Function to check if the board is full
def is_board_full():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True


# Function to handle a button click
def on_click(row, col):
    global player_turn

    if buttons[row][col]["text"] == "":
        if player_turn:  # Player 1's turn (X)
            buttons[row][col]["text"] = "X"
            turn_label.config(text="Player 2's Turn (O)")
        else:  # Player 2's turn (O)
            buttons[row][col]["text"] = "O"
            turn_label.config(text="Player 1's Turn (X)")
        player_turn = not player_turn

        winner, winning_positions = check_winner()
        if winner:
            for pos in winning_positions:
                buttons[pos[0]][pos[1]].config(bg="lightgreen")
            winning_player = "Player 1" if not player_turn else "Player 2"
            messagebox.showinfo("Tic-Tac-Toe", f"{winning_player} wins!")
            reset_board()
        elif is_board_full():
            for row in range(3):
                for col in range(3):
                    buttons[row][col].config(bg="lightcoral")
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
    else:
        return


# Function to reset the board
def reset_board():
    global player_turn
    player_turn = True
    turn_label.config(text="Player 1's Turn (X)");
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="SystemButtonFace");


# Create the buttons and place them in a grid:
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                      command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row+2, column=col)  # Adjust grid position to accommodate labels


# Start the main event loop
root.mainloop()
