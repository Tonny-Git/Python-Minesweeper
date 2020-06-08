import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()
app.geometry("300x100")
fontStyle = tkFont.Font(family="Lucida Grande", size=20)

labelExample = tk.Label(app, text="20", font=fontStyle)

pixelVirtual = tk.PhotoImage(width=1, height=1)

buttonExample1 = tk.Button(app,
                           text="Increase",
                           image=pixelVirtual,
                           width=30,
                           height=30,
                           compound="c")
buttonExample2 = tk.Button(app,
                           text="Decrease",
                           image=pixelVirtual,
                           width=100,
                           height=100,
                           compound="c")

buttonExample1.place(x=10, y=10)
buttonExample2.pack(side=tk.RIGHT)
app.mainloop()