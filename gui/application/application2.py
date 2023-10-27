"""
#author: saozdemir
#description: Kullanıcı ado ve şifre formu

"""
import tkinter as tk

form = tk.Tk()
form.title("Kullanıcı İşlemleri")  # Form title
form.geometry("500x400")


def enter():
    entryName.delete(0, "end")
    entryPassword.delete(0, "end")


def register():
    labelEmail = tk.Label(form, text="Eposta ")
    labelEmail.place(x=10, y=100)

    labelName = tk.Label(form, text="Adı")
    labelName.place(x=10, y=130)

    labelPassword = tk.Label(form, text="Şifre")
    labelPassword.place(x=10, y=160)

    entryEmail = tk.Entry(form)
    entryEmail.place(x=100, y=100)

    entryName = tk.Entry(form)
    entryName.place(x=100, y=130)

    entryPassword = tk.Entry(form, show="*")
    entryPassword.place(x=100, y=160)

fileDialog= tk.FileDialog
labelName = tk.Label(form, text="Kullanıcı Adı ")
labelName.place(x=10, y=10)

labelPassword = tk.Label(form, text="Şifre")
labelPassword.place(x=10, y=40)

entryName = tk.Entry(form)
entryName.place(x=100, y=10)

entryPassword = tk.Entry(form, show="*")
entryPassword.place(x=100, y=40)

btnEnter = tk.Button(form, text="Giriş", command=enter)
btnEnter.place(x=100, y=70)

btnRegister = tk.Button(form, text="Kayıt", command=register)
btnRegister.place(x=150, y=70)

form.mainloop()
