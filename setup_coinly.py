import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time

def pag_entradafinanc():
    financsetup = tk.Tk()
    pag_nome.geometry("500x500")
    pag_nome.title("Bem-Vindo ao Coinly!")
    pag_nome.resizable(False, False)

    canvas = tk.Canvas(pag_nome, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

def pag_nome():

    pag_nome = tk.Tk()

    pag_nome.geometry("500x500")
    pag_nome.title("Bem-Vindo ao Coinly!")

    pag_nome.resizable(False, False)

    canvas = tk.Canvas(pag_nome, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    bvindo = Image.open("assets\setup_pag1.png")
    bvindo2 = ImageTk.PhotoImage(bvindo)

    canvas.create_image(0, 0, image=bvindo2, anchor="nw")

    btn_proximo = Image.open("assets\\btn_proximo.png")
    btn_proximo2 = ImageTk.PhotoImage(btn_proximo)

    canvas.create_image(236, 445, image=btn_proximo2, anchor="nw")

    nomeuser = tk.Entry(pag_nome, width=30, font=("Arial", 12))
    canvas.create_window(250, 380, window=nomeuser)

    pag_nome.mainloop()

