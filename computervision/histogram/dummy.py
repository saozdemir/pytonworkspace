import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_histogram():
    # Histogram verilerini oluşturun (örneğin, rastgele veri)
    data = [3, 5, 8, 2, 7, 4, 1, 6, 9]

    # Histogram oluşturun
    fig = Figure(figsize=(5, 4))
    ax = fig.add_subplot(111)
    ax.hist(data, bins=5, color='blue', alpha=0.7, rwidth=0.85)

    # Canvas oluşturun
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # Canvas'ı pencereye yerleştirin
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Tkinter penceresini oluşturun
window = tk.Tk()
window.title("Histogram")

# Histogramı oluşturun ve gösterin
create_histogram()

# Pencereyi çalıştırın
window.mainloop()
