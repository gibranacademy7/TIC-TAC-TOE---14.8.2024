# TIC TAC TOE GAME - shorter way (using comprehension & lambda):

import tkinter as tk
from tkinter import messagebox

root = tk.Tk();
root.title("Tic-Tac-Toe");

player_turn = True
buttons = [[None for _ in range(3)] for _ in range(3)];

turn_label = tk.Label(root, text="Player 1's Turn (X)", font=('Arial', 25), fg='blue', bg='white');
turn_label.grid(row=0, column=0, columnspan=3);

title_label = tk.Label(root, text="Tic-Tac-Toe", font=('Arial', 30, 'bold'), fg='darkred', bg='white');
title_label.grid(row=1, column=0, columnspan=3);

def check_winner():
    lines = [(lambda r: [(r, i) for i in range(3)])(r) for r in range(3)] + \
            [(lambda c: [(i, c) for i in range(3)])(c) for c in range(3)] + \
            [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]

    for line in lines:
        if all(buttons[r][c]["text"] == buttons[line[0][0]][line[0][1]]["text"] != "" for r, c in line):
            return True, line
    return False, [];

def is_board_full():
    return all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3));


def on_click(row, col):
    global player_turn

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = "X" if player_turn else "O"
        turn_label.config(text=f"Player {'2' if player_turn else '1'}'s Turn ({'O' if player_turn else 'X'})");
        player_turn = not player_turn

        winner, winning_positions = check_winner();
        if winner:
            [buttons[pos[0]][pos[1]].config(bg="lightgreen") for pos in winning_positions]
            messagebox.showinfo("Tic-Tac-Toe", f"Player {'1' if not player_turn else '2'} wins!");
            reset_board();
        elif is_board_full():
            [buttons[row][col].config(bg="lightcoral") for row in range(3) for col in range(3)];
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!");
            reset_board();

def reset_board():
    global player_turn
    player_turn = True
    turn_label.config(text="Player 1's Turn (X)");
    [buttons[row][col].config(text="", bg="SystemButtonFace") for row in range(3) for col in range(3)];

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                      command=lambda row=row, col=col: on_click(row, col));
        buttons[row][col].grid(row=row+2, column=col)


root.mainloop()
