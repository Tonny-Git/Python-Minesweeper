
class Timer:

    def __init__(self):
        self.time = 0

    def counter(self, root, label):
        self.time += 1
        label.config(text=self.time)

        if self.time <= 200:
            root.after(10, self.counter(root, label))
