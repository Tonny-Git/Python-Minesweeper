import tkinter as tk


class Timer:

    def __init__(self, root):
        self.root = root
        self.time_label = tk.Label(self.root, text=0)
        self.time = 0
        self.isActive = True
        self.start_timer()

    def start_timer(self):
        self.time_label.place(relx=0.5, rely=0.05)
        self.counter()

    def counter(self):

        if self.time < 999 and self.isActive:
            self.time += 1
            self.time_label.config(text=self.time)
            self.root.after(1000, self.counter)
