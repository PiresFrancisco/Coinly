import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from setup_coinly import *
from configparser import ConfigParser 
import sys 

import mysql.connector


database = mydb = mysql.connector.connect(
   host = "localhost",
   user="root",
  password="password",
    database="coinly"
)

aquelacena = database.cursor()

def adicionarrendimento(event):
        rendimentoadd = tk.Toplevel()

        rendimentoadd.geometry("500x500")
        rendimentoadd.title("Coinly > Adicionar Rendimento")

        rendimentoadd.resizable(False, False)
        canvas = tk.Canvas(rendimentoadd, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        pagrendimento = Image.open("assets\\rendimento_add.png")
        pagrendimento2 = ImageTk.PhotoImage(pagrendimento)
        canvas.image = pagrendimento2
        canvas.create_image(0, 0, image=pagrendimento2, anchor="nw")

        rendimentodinheiro = tk.Entry(rendimentoadd,justify="center", width=15,font=("Urbanist", 30),bg="#0B313C",fg="white")
        canvas.create_window(250, 380, window=rendimentodinheiro)




        opcoes = ["                                     ", "Salário", "Subsídios (ex.: alimentação, férias, Natal)", "Bolsas de estudo","Pensão / Reforma","Ajudas familiares","Outros"]
        opcao_var = tk.StringVar()
        opcao_var.set(opcoes[0])

        rendimentotipo = tk.OptionMenu(rendimentoadd, opcao_var, *opcoes,)
        rendimentotipo.config(bg="#0B313C", fg="white", font=("Arial", 15))
        rendimentotipo.pack(pady=20)
        

        canvas.create_window(250, 263, window=rendimentotipo)

        def concluir(event):
            escolha  = opcao_var.get()
            if escolha == "Salário":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO rendimentos (tipo, quantidade) VALUES (%s, %s)", ("salario", quantidade))
                database.commit()
                rendimentoadd.destroy()

            if escolha == "Subsídios (ex.: alimentação, férias, Natal)":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO rendimentos (tipo, quantidade) VALUES (%s, %s)", ("subsidio", quantidade))
                database.commit()
                rendimentoadd.destroy()


            if escolha == "Bolsas de estudo":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO rendimentos (tipo, quantidade) VALUES (%s, %s)", ("bolsa", quantidade))
                database.commit()

                rendimentoadd.destroy()

            if escolha == "Pensão / Reforma":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO rendimentos (tipo, quantidade) VALUES (%s, %s)", ("pensao_reforma", quantidade))
                database.commit()
                rendimentoadd.destroy()

            if escolha == "Ajudas familiares":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO rendimentos (tipo, quantidade) VALUES (%s, %s)", ("pensao_reforma", quantidade))
                database.commit()
                rendimentoadd.destroy()

            
            if escolha == "Outros":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO rendimentos (tipo, quantidade) VALUES (%s, %s)", ("outros", quantidade))
                database.commit()

                rendimentoadd.destroy()

        btn_concluir = Image.open("assets\\btn_concluir.png")
        btn_concluir2 = ImageTk.PhotoImage(btn_concluir)
        btnconcluir3 = canvas.create_image(187, 444, image=btn_concluir2, anchor="nw")
        canvas.tag_bind(btnconcluir3, "<Button-1>",concluir)


        rendimentoadd.mainloop()

def adicionardespesa(event):
    despesaadd = tk.Toplevel()

    despesaadd.geometry("500x500")
    despesaadd.title("Coinly > Adicionar Despesa")

    despesaadd.resizable(False, False)
    canvas = tk.Canvas(despesaadd, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    pagrendimento = Image.open("assets\\despesa_add.png")
    pagrendimento2 = ImageTk.PhotoImage(pagrendimento)
    canvas.image = pagrendimento2
    canvas.create_image(0, 0, image=pagrendimento2, anchor="nw")

    rendimentodinheiro = tk.Entry(despesaadd,justify="center", width=15,font=("Urbanist", 30),bg="#0B313C",fg="white")
    canvas.create_window(250, 380, window=rendimentodinheiro)




    opcoes = ["                                     ", "Renda / Prestação da casa", "Contas da Casa", "Seguros","Transporte","Alimentação","Pessoais","Lazer","Financeiras"]
    opcao_var = tk.StringVar()
    opcao_var.set(opcoes[0])

    rendimentotipo = tk.OptionMenu(despesaadd, opcao_var, *opcoes,)
    rendimentotipo.config(bg="#0B313C", fg="white", font=("Arial", 15))
    rendimentotipo.pack(pady=20)

    canvas.create_window(250, 263, window=rendimentotipo)

    def concluir(event):
        escolha  = opcao_var.get()
        if escolha == "Renda / Prestação da casa":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("renda_prestacao", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Contas da Casa":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("contas_casa", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Seguros":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("seguros", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Transporte":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("transporte", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Alimentação":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("alimentacao", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Pessoais":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("pessoais", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Lazer":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("lazer", quantidade))
                database.commit()
                despesaadd.destroy()

        if escolha == "Financeiras":

                quantidade = rendimentodinheiro.get()
                aquelacena.execute("INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)", ("financeiras", quantidade))
                database.commit()
                despesaadd.destroy()


    btn_concluir = Image.open("assets\\btn_concluir.png")
    btn_concluir2 = ImageTk.PhotoImage(btn_concluir)
    btnconcluir3 = canvas.create_image(187, 444, image=btn_concluir2, anchor="nw")
    canvas.tag_bind(btnconcluir3, "<Button-1>",concluir)
    

    despesaadd.mainloop()

    

def adicionar_item():
    adicionar = tk.Toplevel() 
    adicionar.title("Coinly > Adicionar....")
    adicionar.geometry("500x500")
    adicionar.resizable(False, False)

    canvas = tk.Canvas(adicionar, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    bg_image = Image.open("assets\\adicionar_bg.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    rendimento = Image.open("assets\\rendimento_grande.png")
    rendimento2 = ImageTk.PhotoImage(rendimento)
    rendimento3 = canvas.create_image(40, 201, image=rendimento2, anchor="nw")
    
    despesa = Image.open("assets\\despesa_Grande.png")
    despesa2 = ImageTk.PhotoImage(despesa)
    despesa3 = canvas.create_image(40, 312, image=despesa2, anchor="nw")
    
    btnAnterior = Image.open("assets\\btn_anterior.png")
    btnAnterior2 = ImageTk.PhotoImage(btnAnterior)
    btnsair = canvas.create_image(235, 445, image=btnAnterior2, anchor="nw")
    def sair(event):
          adicionar.destroy()
    canvas.tag_bind(btnsair, "<Button-1>",sair)

    canvas.tag_bind(despesa3, "<Button-1>",adicionardespesa)
    canvas.tag_bind(rendimento3, "<Button-1>",adicionarrendimento)

    adicionar.mainloop()