"""
#author: saozdemir
#description:

"""
import tkinter as tk

form=tk.Tk()
form.title("From Status") # Form title
form.geometry("500x500+350+250")

form.state("normal")
# form.state("zoomed") # Tam ekran
# form.state("iconic") # icon olarak

#saydamlık
form.wm_attributes("-alpha", 0.9)

form.mainloop()