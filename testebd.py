import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk
from datetime import datetime

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="sensor_data"
)
cursor = conexao.cursor()
cursor.execute("SELECT data_hora, valor FROM temperatura ORDER BY data_hora")
resultados = cursor.fetchall()
cursor.close()
conexao.close()

if not resultados:
    print("⚠️ Nenhum dado encontrado na tabela.")
    exit()

datas = [registro[0] for registro in resultados]
valores = [registro[1] for registro in resultados]

janela = Tk()
janela.title("Gráfico de Temperatura")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(datas, valores, marker='o', linestyle='-', color='red')
ax.set_title('Temperatura ao longo do tempo')
ax.set_xlabel('Data e Hora')
ax.set_ylabel('Temperatura (°C)')
ax.grid(True)
ax.set_facecolor('black')
fig.patch.set_facecolor('gray')
plt.xticks(rotation=45)
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.draw()
canvas.get_tk_widget().pack(fill='both', expand=True)

janela.mainloop()
