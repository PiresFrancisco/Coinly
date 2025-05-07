import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create main window
root = tk.Tk()
root.title("Pie Chart in Tkinter")

# Create a Matplotlib figure
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

# Pie chart data
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [20, 35, 30, 15]
colors = ['red', 'yellow', 'pink', 'brown']

# Plot pie chart
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title('Fruit Distribution')

# Embed figure in Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Start Tkinter loop
root.mainloop()
