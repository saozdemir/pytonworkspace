"""
#author: saozdemir
#description: Layout ayarlama işlemleri (Pack)
side    : left-right-top-bottom => yerleşim
expand  : 0-1 => genişletme özelliği
fill    : x-y =yatay ve düşey doldurma
ancor   : (n) kuzey - (s) güney - (e) doğu - (w) batı
            (ne) kuzeydoğu - (nw) kuzeybatı
            (se) güneydoğu - (sw) güneybatı
padx, pady :Kenar boşlukları
ipadx, ipady :Komponent boyutu ayarlama
"""
import tkinter as tk

form = tk.Tk()
form.title("Geometrik İşlemler")
form.geometry("500x500")
label = tk.Label(form, text="Geometrik yöneticiler")
label.pack(side=tk.TOP)

button = tk.Button(form, text="Pack()", bg="yellow")
#button.pack(side = tk.BOTTOM, fill=tk.X, expand=tk.YES) #fill=tk.Y
button.pack(expand=tk.YES, anchor="se", padx=5, pady=5 ,ipadx = 20, ipady=15) #fill=tk.Y


form.mainloop()