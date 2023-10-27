"""
#author: saozdemir
#description: Layout ayarlama işlemleri (Place)
"""
import tkinter as tk

form = tk.Tk()
form.title("Geometrik İşlemler")
form.geometry("500x500")

button = tk.Button(form, text="Place()")
# button.place(x=50, y=40) # sabit yerleşim
# button.place(relx=0.5, rely=0.5) # dinamik yerleşim
button.place(width=50, heigh=40) # boyut

form.mainloop()
