from tkinter import *

janela = Tk()

texto = Label(janela,text="Ola insere o teu guito")
texto.pack()
guito = Entry(janela)
guito.pack()
janela.mainloop()