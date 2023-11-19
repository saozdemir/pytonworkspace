"""
 @author saozd
 @project pytonworkspace sss
 @date 06 Kas 2023
 <p>
 @description:
"""
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_histogram():
    for widget in window.winfo_children():
        widget.destroy()
    fig = Figure(figsize=(5, 4))
    ax = fig.add_subplot(111)

    # Burada histogramı oluşturun ve verileri 'hist_data' adlı bir liste olarak ayarlayın.
    hist_data = [10, 20, 30, 40, 50]
    ax.bar(range(len(hist_data)), hist_data, tick_label=[f"Bin {i + 1}" for i in range(len(hist_data))])

    ax.set_title('Histogram')
    ax.set_xlabel('Bins')
    ax.set_ylabel('Frequency')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


window = tk.Tk()
window.title("Histogram Display")

btnShowHistogram = ttk.Button(window, text="Show Histogram", command=show_histogram)
btnShowHistogram.pack(padx=10, pady=10)

window.mainloop()
