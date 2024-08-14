import tkinter as tk
from tkinter import messagebox
import random


class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Game")

        self.colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'yellow', 'E': 'purple', 'F': 'orange'}
        self.deck = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'A', 'A', 'B', 'B']
        self.board = ['*'] * 16
        self.first_guess, self.pairs_found, self.points = None, 0, 0
        self.create_widgets()
        self.init_game()

    def create_widgets(self):
        tk.Label(self.master, text="MEMORY GAME", font=('Arial', 18)).grid(row=0, column=0, columnspan=4)

        self.buttons = [
            tk.Button(self.master, width=16, height=8, bg='lightgray', command=lambda i=i: self.reveal_card(i))
            for i in range(16)]
        [button.grid(row=(i // 4) + 1, column=i % 4) for i, button in enumerate(self.buttons)]

        self.status_label = tk.Label(self.master, text="Points: 0", font=('Arial', 14))
        self.status_label.grid(row=5, column=0, columnspan=4)

    def init_game(self):
        random.shuffle(self.deck)
        self.first_guess, self.pairs_found, self.points = None, 0, 0
        self.update_status()
        [button.config(bg='lightgray', text='') for button in self.buttons]

    def update_status(self):
        self.status_label.config(text=f"Points: {self.points}")

    def reveal_card(self, index):
        if self.first_guess is None:
            self.first_guess = index
            self.buttons[index].config(bg=self.colors[self.deck[index]], text=self.deck[index])
        else:
            if index == self.first_guess:
                return
            self.buttons[index].config(bg=self.colors[self.deck[index]], text=self.deck[index])
            self.master.after(1000, lambda: self.check_match(index))

    def check_match(self, second_guess):
        first_card = self.first_guess
        if self.deck[first_card] == self.deck[second_guess]:
            self.pairs_found += 1
            self.points += 10
            self.update_status()
            if self.pairs_found == 8:
                self.points += 50
                messagebox.showinfo("Congratulations!", f"You've found all pairs!\nTotal Points: {self.points}")
                self.ask_restart()
        else:
            self.points -= 2
            self.update_status()
            self.buttons[first_card].config(bg='lightgray', text='')
            self.buttons[second_guess].config(bg='lightgray', text='')
        self.first_guess = None

    def ask_restart(self):
        messagebox.showinfo("Final Score", f"Your final score is: {self.points}")
        if messagebox.askyesno("Play Again?", "Do you want to play again?"):
            self.init_game()
        else:
            self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    MemoryGame(root)
    root.mainloop()
