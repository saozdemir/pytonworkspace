"""
#author: saozdemir
#description: Entry text işlemleri

"""
import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Entry İşlemleri")  # Form title
form.geometry("500x400")

entry = tk.Entry(form)
entry.pack()


def get_data():
    label["text"] = entry.get()


def clear():
    entry.delete(0, "end")


entryPw = tk.Entry(form, show="*")
entryPw.pack()

button = tk.Button(form, text="Verileri Al", command=get_data)
button.pack()

btnClear = tk.Button(form, text="Sil", command=clear)
btnClear.pack()

label = tk.Label(form, text="Veriler bu alana gelecek")
label.pack()

form.mainloop()
