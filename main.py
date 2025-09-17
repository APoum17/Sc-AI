# import tkinter as tk
# from main_window import MainWindow

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MainWindow(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()