"""
#author: saozdemir
#description:

"""
import tkinter as tk #tkinter kütüphanesini import et ve kod içinde tk olarak kullan

form =tk.Tk() # Form oluşturma
form.title("Label İşlemleri") # Form title

label=tk.Label(form, text="Pyton Tkinter")
label.pack()

label2=tk.Label(form, text="Ders-2", fg="red") #Kırmızı renk
label2.pack()

label3=tk.Label(form, text="Ders-2 Arkaplan", fg="black", bg="green")
label3.pack()

label4=tk.Label(form, text="Yeni label", fg="red", bg="blue", font="Times 15 italic")
label4.pack()

label5=tk.Label(form, text="Son Label", fg="green", bg="red", font="Times 17 bold")
label5.pack()

form.mainloop()


