"""
#author: saozdemir
#description: Button uygulaması

"""
import tkinter as tk

form=tk.Tk()
form.title("Button Operation") # Form title
form.geometry("500x400")

def add():
    print("Topla")

button=tk.Button(form, text="Click", fg="black", bg="red", command=add)
button.pack(side=tk.LEFT) #Pozisyona göre ekleme

button2=tk.Button(form, text="Click2", command=add)
button2.pack(side=tk.LEFT) #Pozisyona göre ekleme
form.mainloop()