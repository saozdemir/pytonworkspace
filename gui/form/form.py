"""
#author: saozdemir
#description:

"""
import tkinter as tk

form =tk.Tk() # Form oluşturma
form.title("Tkinter Dersleri") # Form title
form.geometry("500x250+500+350") #From boyutlandırma +500+350> pozisyon
form.minsize(450,400)
form.maxsize(550,550)

#form.resizable(False,False) # Resize özelliğini kapatma

label = tk.Label(text="Tkinter Pyton") #Label oluşturma
label.pack() #Ekrana ekleme

#Asıl kullanım şekli hangi formda kullanılacaksa o referans verilir.
label2 = tk.Label(form, text="Pyton Tkinter Dersleri")
label2.pack()

form.mainloop()