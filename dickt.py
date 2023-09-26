import tkinter as tk

entry_value = str()


class MyGUI():

    def __init__(self):
        self.root = tk.Tk()

        self.entry = tk.Entry()
        self.entry.bind("<Enter>")
        self.entry.pack()

        self.root.mainloop()

    def say_hi(self):
        print('Hello, my name is', self.entry.get())

MyGUI()