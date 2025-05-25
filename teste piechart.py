import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create main window
root = tk.Tk()
root.title("Pie Chart in Tkinter")

# Create a canvas widget sized 418x234
canvas_widget = tk.Canvas(root, width=418, height=234)
canvas_widget.pack()

# Create a Matplotlib figure (size adjusted to fit the canvas)
fig = plt.Figure(figsize=(4.18, 2.34), dpi=100)  # 4.18 in x 100 dpi = 418 px
ax = fig.add_subplot(111)

# Pie chart data
labels = ['Pessoais', 'Financeiras', 'Contas da Casa', 'Rendas']
sizes = [300, 600, 200, 500]
colors = ['red', 'yellow', 'pink', 'brown']

# Plot pie chart
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title('Despesas')

# Embed figure in Tkinter
fig_canvas = FigureCanvasTkAgg(fig, master=root)
fig_widget = fig_canvas.get_tk_widget()
fig_canvas.draw()

# Add the Matplotlib widget to the Canvas, centered
canvas_widget.create_window(209, 117, window=fig_widget)

# Start Tkinter loop
root.mainloop()
