"""
#author: saozdemir
#description: Entry text girişi

"""
import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Entry")  # Form title
form.geometry("500x400+500+350")

entry = tk.Entry(form, fg="black", bg="yellow")
entry.pack(side=tk.LEFT)

entry2 = tk.Entry(form, fg="white", bg="blue")
entry2.pack(side=tk.LEFT)

form.mainloop()
