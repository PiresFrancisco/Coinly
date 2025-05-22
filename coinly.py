import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from setup_coinly import *
from coinly_extra import *
from configparser import ConfigParser 
import sys 

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


    btn_mais = Image.open("assets\\adicionar.png")
    btn_mais2 = ImageTk.PhotoImage(btn_mais)
    mais = canvas.create_image(7, 338, image=btn_mais2, anchor="nw")
    canvas.tag_bind(mais, "<Button-1>", adicionarcenas)


    canvas.create_image(15, 0, image=img_logo, anchor="nw")

    nomeuser = ConfigParser()
    nomeuser.read('coinly.conf')  
    nutilizador = nomeuser['CoinlyUser']['nutilizador'] 


    string_user = tk.Label(coinly, text="Olá, "+nutilizador, bg=temafg,font=("Product Sans", 25),fg=tematxt)
    canvas.create_window(160, 90, window=string_user)


    receitas = tk.Label(coinly, text="Receitas / Despesas", bg=temabg2,font=("Product Sans", 15),fg=tematxt3)
    canvas.create_window(170, 155, window=receitas)

    data_atual = datetime.datetime.now()
    data_extenso = data_atual.strftime("%A, %d  %B  %Y")

    string_data = tk.Label(coinly,text=data_extenso,bg=temadata,font=("Product Sans", 15),fg=tematxt2)
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

    porcategoria = tk.Label(coinly, text="Por Categoria:", bg=temabg2,font=("Product Sans", 10),fg=tematxt3)
    canvas.create_window(105, 390, window=porcategoria)

    saldoatual = tk.Label(coinly, text="Em Resumo:", bg=temabg2,font=("Product Sans", 12),fg=tematxt3)
    canvas.create_window(385, 390, window=saldoatual)


    cursor.execute("SELECT SUM(quantidade) AS total_geral FROM rendimentos")
    resultado = cursor.fetchone()
    resultado1 = resultado[0]
    resultadomesmo = "+ " + str(resultado1) + "€"

    totalrendimento = tk.Label(coinly, text=resultadomesmo, bg=temabg2,font=("Product Sans", 15),fg="green")
    canvas.create_window(400, 425, window=totalrendimento)


    cursor.execute("SELECT SUM(quantidade) AS total_geral FROM despesas")
    resultad = cursor.fetchone()
    resultad1 = resultad[0]
    resultadmesmo = "- " + str(resultad1) + "€"

    totalrendimento = tk.Label(coinly, text=resultadmesmo, bg=temabg2,font=("Product Sans", 15),fg="red")
    canvas.create_window(400, 463, window=totalrendimento)

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