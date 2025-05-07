from tkinter import *

janela = Tk()

janela.geometry("500x500")
janela.title("Bem-Vindo!")

janela.resizable(False, False)
canvas = Canvas(janela, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)
janela.mainloop()