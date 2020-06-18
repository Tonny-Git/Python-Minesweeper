import tkinter as tk
from tkinter import ttk


class Root(tk.Tk):
    size = ["Small", "Medium", "Large"]

    def __init__(self, menu):
        super(Root, self).__init__()
        self.menu = menu
        self.frame = tk.Frame(self, height=500, width=500, bg="white")
        self.init_setup()
        self.start_button = tk.Button(self.frame, text="Start Game", command=self.minesweeper_mode)
        self.highscore_button = tk.Button(self.frame, text="Highscore", command=self.highscore_mode)
        self.highscore_return_button = tk.Button(self.frame, text="Return", command=self.return_to_menu)
        self.end_button = tk.Button(self.frame, text="End Game", command=lambda: self.menu.end_game("quit"))
        self.submit_button = tk.Button(self.frame, text="Submit Highscore", command=self.submit_score)
        self.submit_entry = tk.Entry(self.frame)
        self.score_labels = []
        self.size_button = ttk.Combobox(self.frame, values=self.size)
        self.main_menu_mode()

    def init_setup(self):
        self.title("Minesweeper")
        self.minsize(500, 500)
        self.maxsize(500, 500)
        self.frame.pack()

    def main_menu_mode(self):
        self.change_size(500)
        self.end_button.place_forget()
        self.start_button.place(relx=0.5, rely=0.49)
        self.size_button.place(relx=0.2, rely=0.5)
        self.size_button.set("Pick a size")
        self.highscore_button.place(relx=0.45, rely=0.7)

    def minesweeper_mode(self):
        if self.size_button.get() == "Small":
            self.change_size(400)
        elif self.size_button.get() == "Medium":
            self.change_size(560)
        elif self.size_button.get() == "Large":
            self.change_size(700)
        else:
            return
        self.start_button.place_forget()
        self.size_button.place_forget()
        self.highscore_button.place_forget()
        self.menu.start_game(self.size_button.get())

    def minesweeper_highscore_mode(self):
        self.end_button.place_forget()
        self.submit_entry.delete(0, 'end')
        self.submit_entry.insert(0, "Enter name...")
        self.submit_entry.place(relx=0.15, rely=0.9)
        self.submit_button.place(relx=0.15, x=180, rely=0.9)

    def submit_score(self):
        self.menu.score.handle_value(self.submit_entry.get(), self.menu.timer.time, self.size_button.get().lower())
        self.submit_entry.place_forget()
        self.submit_button.place_forget()
        self.menu.end_game("quit")

    def highscore_mode(self):
        self.start_button.place_forget()
        self.size_button.place_forget()
        self.highscore_button.place_forget()
        self.highscore_return_button.place(relx=0.45, rely=0.9)
        score = self.menu.score.fetch_all()
        scores = [[], [], []]
        for result in score:
            if result[3] == "small":
                scores[0].append(result)
            elif result[3] == "medium":
                scores[1].append(result)
            elif result[3] == "large":
                scores[2].append(result)
        size_name = ["Small", "Medium", "Large"]
        for i, size in enumerate(scores):
            size_label = tk.Label(self.frame, text=f"{size_name[i]}", bg="white")
            size_label.place(relx=0.4, y=120*i)
            self.score_labels.append(size_label)
            for j, label in enumerate(size):
                label = tk.Label(self.frame, text=f"{j+1}.   {label[2]}   {label[1]}", bg="white")
                label.place(relx=0.4, y=120*i + 30*j + 25)
                self.score_labels.append(label)

    def return_to_menu(self):
        self.highscore_return_button.place_forget()
        for label in self.score_labels:
            label.destroy()
        self.main_menu_mode()

    def change_size(self, num):
        self.minsize(num, num)
        self.maxsize(num, num)
        self.frame.config(height=num, width=num)
        self.end_button.place(relx=0.45, y=num-40)
