import tkinter as tk
import time

from root import Root


class Example:
    staticVar = 0


def timeout():
    time_sum.staticVar += 1
    time_label.config(text=time_sum.staticVar)
    window.after(1000, timeout)


time_sum = Example()
window = tk.Tk()
window.title("Example")


time_label = tk.Label(window, text='', bg="black", fg="white")
time_label.grid(row=1, column=2)

timeout()
window.geometry("100x100+100+100")
window.mainloop()



"""
class Example:
    staticVariable = 0


example = Example()


def timeout():
    time_label.config(text=example.staticVariable)
    # print(type(num))
    example.staticVariable += 1
    if example.staticVariable > 200:
        pass
    else:
        window.after(1, timeout())


window = tk.Tk()
window.title("Example")


time_label = tk.Label(window, text='', bg="black", fg="white")
time_label.grid(row=1, column=2)

# window.after(1000, timeout())
timeout()
window.geometry("100x100+100+100")
window.mainloop()
"""




"""
def count_time(time):
    time += 1
    root.after(1000, time)
    return time


current_time = 0
root = Root()
time_label = tk.Label(root, text=count_time(current_time))
time_label.pack()
root.mainloop()
"""


"""
import time
60 * 60 * 24
# time.clock()
# time.time()
print(time.time())
# print(time.clock())

print(time.process_time())
"""