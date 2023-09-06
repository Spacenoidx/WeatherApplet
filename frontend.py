import tkinter as tk
from tkinter import messagebox
import os

import weada as backend

class MyGUI:
    def __init__(self):

        self.root = tk.Tk()


        self.label = tk.Label(self.root, text="Find the weather in your area", font=("Arial", 20))
        self.label.pack(padx=10, pady=10)

        self.label2 = tk.Label(self.root, text="Enter your United States ZIP code below.", font=("Arial", 12))
        self.label2.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root,font=("Arial", 16))
        self.entry.pack(padx=10, pady=10)

        grabbedzip = ""



        def on_return(self, event):
            # Bind the return key event to the entry widget
            self.entry.bind("<Return>", self.on_return)

            # Get the data from the entry widget
            grabbedzip = self.entry.get()

            backend.zipcodegrab(grabbedzip)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show messagebox", font=("Arial", 18), variable = self.check_state)
        self.check.pack(padx=10, pady=10)


        self.root.mainloop()



MyGUI()
print(grabbedzip)
