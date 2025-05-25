import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from setup_coinly import *
from coinly_extra import *
from configparser import ConfigParser 
import sys 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

database = mydb = mysql.connector.connect(
   host = "localhost",
   user="root",
  password="password",
    database="coinly"
)

cursor = database.cursor()






def definicoess(event):
    sys.exit()

def impexps(event):
    impexp = tk.Toplevel()
    impexp.title("Coinly > Importar ou Exportar....")
    impexp.geometry("500x500")
    impexp.resizable(False, False)
    canvas = tk.Canvas(impexp, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    bgimpexp = Image.open("assets\\impexp_bg.png")
    bgimpexp2 = ImageTk.PhotoImage(bgimpexp)
    canvas.create_image(0, 0, image=bgimpexp2, anchor="nw")

    btn_imp = Image.open("assets\\importar.png")
    btn_imp2 = ImageTk.PhotoImage(btn_imp)
    canvas.create_image(40, 201, image=btn_imp2, anchor="nw")

    btn_exp = Image.open("assets\\exportar.png")
    btn_exp2 = ImageTk.PhotoImage(btn_exp)
    canvas.create_image(40, 312, image=btn_exp2, anchor="nw")

    impexp.mainloop()


def sair(event):
    sys.exit()

def adicionarcenas(event):
    adicionar_item()


def coinly_receitas():
    coinlyreceitas = tk.Tk()
    coinlyreceitas.title("Coinly > Software de Gestão Financeira Pessoal")
    coinlyreceitas.geometry("500x500")
    coinlyreceitas.resizable(False, False)
    canvas = tk.Canvas(coinlyreceitas, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    def trocarvoltar(event):
        coinlyreceitas.destroy()

    ###### Gráfico #############################

    fig = plt.Figure(figsize=(4.18, 2.34), dpi=100)  
    ax = fig.add_subplot(111)

    labels = ['Pessoais', 'Financeiras', 'Contas da Casa', 'Rendas']
    sizes = [300, 600, 200, 500]
    colors = ['red', 'yellow', 'pink', 'brown']
    
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title(' ')
    ax.set_facecolor('lightblue')

    fig_canvas = FigureCanvasTkAgg(fig, master=coinlyreceitas)
    fig_widget = fig_canvas.get_tk_widget()
    fig_canvas.draw()

    canvas.create_window(270, 245, window=fig_widget)








    ###### Gráfico #############################



    temapreto = ConfigParser()
    temapreto.read('coinly.conf')  
    conf_temapreto = temapreto['CoinlyUser']['darkmode']

    checkdados = ConfigParser()
    checkdados.read('coinly.conf')  
    checkdados_conf = checkdados['CoinlyUser']['estado_adicionar']

    if conf_temapreto == "1":
        bg_image = Image.open("assets\\background_dark.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        temafg = "#141414"
        tematxt = "skyblue"
        tematxt2 = "white"
        temabg2="#2C2C2C"
        temadata="#0F3945"
        tematxt3 = "white"
    else:
        if checkdados_conf == "1":
            bg_image = Image.open("assets\\background_light_empty.png")
            bg_photo = ImageTk.PhotoImage(bg_image)
            temafg = "white"
            tematxt = "black"
            tematxt2 = "white"
            temabg2 = "#DEDEDE"
            temadata="#124958"
            tematxt3 = "black"

        else:
            bg_image = Image.open("assets\\background_light.png")
            bg_photo = ImageTk.PhotoImage(bg_image)
            temafg = "white"
            tematxt = "black"
            tematxt2 = "white"
            temabg2 = "#DEDEDE"
            temadata="#124958"
            tematxt3 = "black"


    logotipo = Image.open("assets\\logo.png")
    img_logo = ImageTk.PhotoImage(logotipo)

    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    btn_trocar = Image.open("assets\\btn_trocar.png")
    btn_trocar2 = ImageTk.PhotoImage(btn_trocar)
    trocarmodo = canvas.create_image(7, 200, image=btn_trocar2, anchor="nw")
    canvas.tag_bind(trocarmodo, "<Button-1>",trocarvoltar)


    btn_mais = Image.open("assets\\adicionar.png")
    btn_mais2 = ImageTk.PhotoImage(btn_mais)
    mais = canvas.create_image(7, 338, image=btn_mais2, anchor="nw")
    canvas.tag_bind(mais, "<Button-1>", adicionarcenas)


    canvas.create_image(15, 0, image=img_logo, anchor="nw")

    nomeuser = ConfigParser()
    nomeuser.read('coinly.conf')  
    nutilizador = nomeuser['CoinlyUser']['nutilizador'] 


    string_user = tk.Label(coinlyreceitas, text="Olá, "+nutilizador, bg=temafg,font=("Product Sans", 25),fg=tematxt)
    canvas.create_window(160, 90, window=string_user)


    receitas = tk.Label(coinlyreceitas, text="Eis as Suas Receitas:", bg=temabg2,font=("Product Sans", 15),fg=tematxt3)
    canvas.create_window(170, 155, window=receitas)

    data_atual = datetime.datetime.now()
    data_extenso = data_atual.strftime("%A, %d  %B  %Y")

    string_data = tk.Label(coinlyreceitas,text=data_extenso,bg=temadata,font=("Product Sans", 15),fg=tematxt2)
    canvas.create_window(380, 23, window=string_data)

    btn_ficheiro = Image.open("assets\\btn_ficheiros.png")
    btn_ficheiro2 = ImageTk.PhotoImage(btn_ficheiro)
    impexp = canvas.create_image(7, 415, image=btn_ficheiro2, anchor="nw")
    canvas.tag_bind(impexp, "<Button-1>",impexps)

    btn_definicoes = Image.open("assets\\btn_defs.png")
    btn_definicoes2 = ImageTk.PhotoImage(btn_definicoes)
    definicoes = canvas.create_image(7, 375, image=btn_definicoes2, anchor="nw")
    canvas.tag_bind(definicoes, "<Button-1>",definicoess)


    btn_sair = Image.open("assets\\sair.png")
    btn_sair2 = ImageTk.PhotoImage(btn_sair)
    sairbtn = canvas.create_image(7, 452, image=btn_sair2, anchor="nw")
    canvas.tag_bind(sairbtn, "<Button-1>",sair)

    porcategoria = tk.Label(coinlyreceitas, text="Por Categoria:", bg=temabg2,font=("Product Sans", 10),fg=tematxt3)
    canvas.create_window(105, 390, window=porcategoria)

    saldoatual = tk.Label(coinlyreceitas, text="Em Resumo:", bg=temabg2,font=("Product Sans", 12),fg=tematxt3)
    canvas.create_window(385, 390, window=saldoatual)


    cursor.execute("SELECT SUM(quantidade) AS total_geral FROM rendimentos")
    resultado = cursor.fetchone()
    resultado1 = resultado[0]
    resultadomesmo = "+ " + str(resultado1) + "€"

    totalrendimento = tk.Label(coinlyreceitas, text=resultadomesmo, bg=temabg2,font=("Product Sans", 15),fg="green")
    canvas.create_window(400, 425, window=totalrendimento)


    cursor.execute("SELECT SUM(quantidade) AS total_geral FROM despesas")
    resultad = cursor.fetchone()
    resultad1 = resultad[0]
    resultadmesmo = "- " + str(resultad1) + "€"

    totalrendimento = tk.Label(coinlyreceitas, text=resultadmesmo, bg=temabg2,font=("Product Sans", 15),fg="red")
    canvas.create_window(400, 463, window=totalrendimento)

    coinlyreceitas.mainloop()
