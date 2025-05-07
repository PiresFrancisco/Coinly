import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create main window
root = tk.Tk()
root.title("Multiple Entries Graph in Tkinter")

# Create a Matplotlib figure
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# First data series
x1 = [1, 2, 3, 4, 5]
y1 = [5, 7, 4, 6, 8]
ax.plot(x1, y1, marker='o', label='Data Series 1')

# Second data series
x2 = [1, 2, 3, 4, 5]
y2 = [3, 5, 2, 4, 6]
ax.plot(x2, y2, marker='s', label='Data Series 2')

# Third data series
x3 = [1, 2, 3, 4, 5]
y3 = [8, 6, 9, 7, 10]
ax.plot(x3, y3, marker='^', label='Data Series 3')

# Add title and legend
ax.set_title('Multiple Entries Graph')
ax.legend()

# Embed the figure in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Start Tkinter loop
root.mainloop()
