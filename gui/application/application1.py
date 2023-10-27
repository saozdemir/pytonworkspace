"""
#author: saozdemir
#description: Button uygulaması

"""
import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Uygulama-1")  # Form title
form.geometry("500x400+500+350")

list = []
for i in range(5):
    while len(list) != 6:
        a = rd.randint(1, 50)
        if a not in list:
            list.append(a)


def show():
    label.config(text=list)

def make_transparent():
    form.wm_attributes("-alpha", 0.7)

def make_opaqe():
    form.wm_attributes("-alpha", 1)

def set_max_size():
    form.state("zoomed")
def set_min_size():
    form.state("iconic")

label = tk.Label(form)
label.pack()

btnShow = tk.Button(form, text="Göster", command=show)
btnShow.pack(side=tk.LEFT)

btnTransparent = tk.Button(form, text="Saydamlaştır", command=make_transparent)
btnTransparent.pack(side=tk.LEFT)

btnOpaqe = tk.Button(form, text="Opak", command=make_opaqe)
btnOpaqe.pack(side=tk.LEFT)

btnMax = tk.Button(form, text="Maksimum", command=set_max_size)
btnMax.pack(side=tk.LEFT)

btnMin = tk.Button(form, text="Minimum", command=set_min_size)
btnMin.pack(side=tk.LEFT)


form.mainloop()
