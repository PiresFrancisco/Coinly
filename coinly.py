import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from setup_coinly import *
from coinly_extra import *
from configparser import ConfigParser 
import sys 

def sair(event):
    sys.exit()

def adicionarcenas(event):
    adicionar_item()


def coinly():
    splash.destroy()
    coinly = tk.Tk()
    coinly.title("Coinly > Software de Gestão Financeira Pessoal")
    coinly.geometry("500x500")
    coinly.resizable(False, False)
    canvas = tk.Canvas(coinly, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)

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
    else:
        if checkdados_conf == "1":
            bg_image = Image.open("assets\\background_light_empty.png")
            bg_photo = ImageTk.PhotoImage(bg_image)
            temafg = "white"
        else:
            bg_image = Image.open("assets\\background_light.png")
            bg_photo = ImageTk.PhotoImage(bg_image)
            temafg = "white"

    logotipo = Image.open("assets\\logo.png")
    img_logo = ImageTk.PhotoImage(logotipo)

    canvas.create_image(0, 0, image=bg_photo, anchor="nw")


    btn_mais = Image.open("assets\\adicionar.png")
    btn_mais2 = ImageTk.PhotoImage(btn_mais)
    mais = canvas.create_image(7, 301, image=btn_mais2, anchor="nw")
    canvas.tag_bind(mais, "<Button-1>", adicionarcenas)


    canvas.create_image(15, 0, image=img_logo, anchor="nw")

    nomeuser = ConfigParser()
    nomeuser.read('coinly.conf')  
    nutilizador = nomeuser['CoinlyUser']['nutilizador']


    string_user = tk.Label(coinly, text="Olá, "+nutilizador, bg=temafg,font=("Product Sans", 25),fg="#124958")
    canvas.create_window(160, 90, window=string_user)


    receitas = tk.Label(coinly, text="Receitas / Despesas (Maio)", bg="#DEDEDE",font=("Product Sans", 15),fg="#124958")
    canvas.create_window(185, 160, window=receitas)

    data_atual = datetime.datetime.now()
    data_extenso = data_atual.strftime("%A, %d  %B  %Y")

    string_data = tk.Label(coinly,text=data_extenso,bg="#124958",font=("Product Sans", 15),fg=temafg)
    canvas.create_window(380, 23, window=string_data)


    btn_sair = Image.open("assets\\sair.png")
    btn_sair2 = ImageTk.PhotoImage(btn_sair)
    sairbtn = canvas.create_image(7, 452, image=btn_sair2, anchor="nw")
    canvas.tag_bind(sairbtn, "<Button-1>",sair)

    porcategoria = tk.Label(coinly, text="Por Categoria:", bg="#DEDEDE",font=("Product Sans", 10),fg="#124958")
    canvas.create_window(105, 390, window=porcategoria)

    saldoatual = tk.Label(coinly, text="Saldo Atual:", bg="#DEDEDE",font=("Product Sans", 10),fg="#124958")
    canvas.create_window(375, 390, window=saldoatual)

    coinly.mainloop()








def OOBE():
    
    checkoobe = ConfigParser()
    checkoobe.read('coinly.conf')  
    check = checkoobe['CoinlyUser']['faseoobe']

    if check == '1':
        coinly()
    elif check == '0':
        splash.destroy()
        pag_nome()






time.sleep(1)
splash = tk.Tk()
splash.overrideredirect(True)
splash.attributes("-topmost", True)

#####################################################################################
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
splash_width = 550                                                                      #ChatGPT
splash_height = 200                                                       #Calcular Centro Ecrã para o splash
x = (screen_width // 2) - (splash_width // 2)
y = (screen_height // 2) - (splash_height // 2)
splash.geometry(f"{splash_width}x{splash_height}+{x}+{y}")
#######################################################################################

logotipo = tk.Canvas(splash, width=550, height=200, bg="#124958",bd=0, highlightthickness=0)
logotipo.pack(fill="both", expand=True)
    
imagemsplash = Image.open("assets\\splash.png")
imagemsplash2 = ImageTk.PhotoImage(imagemsplash)
logotipo.create_image(0, 0, image=imagemsplash2, anchor="nw")
splash.after(1000, OOBE)

splash.mainloop()