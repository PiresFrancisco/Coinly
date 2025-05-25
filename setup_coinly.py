import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from configparser import ConfigParser
import os
import sys
import mysql.connector


database = mydb = mysql.connector.connect(
   host = "localhost",
   user="root",
  password="password",
    database="coinly"
)

cursor = database.cursor(buffered=True)

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
    
    aviso = tk.Label(pag_nome, text="(Max 10 Caracteres)", bg="#174552",font=("Product Sans", 10),fg="white",anchor="center")
    canvas.create_window(250, 353, window=aviso)

    nomeuser = tk.Entry(pag_nome, width=30,font=("Arial", 12))
    canvas.create_window(250, 380, window=nomeuser)

    def updateNome(event):
        if len(nomeuser.get()) == 0:
            erro = tk.Tk()
            erro.title("Coinly > Erro")
            msg_erro = tk.Label(erro,text="Por favor, insira um nome.",font=20)
            msg_erro.pack(padx=20,pady=20)
            erro.mainloop()
        else:
            nome = nomeuser.get()
            config = ConfigParser()
            config.read('coinly.conf')
            config.set("CoinlyUser","Nutilizador",nome)

            with open('coinly.conf', 'w') as f:
                config.write(f)

            pag_nome.destroy()

            pag2setup = tk.Tk()

            pag2setup.geometry("500x500")
            pag2setup.title("Bem-Vindo ao Coinly!")

            pag2setup.resizable(False, False)
            canvas = tk.Canvas(pag2setup, width=500, height=500, bg="#124958",bd=0, highlightthickness=0)
            canvas.pack(fill="both", expand=True)

            pag2 = Image.open("assets\setup_pag2.png")
            pag2stp = ImageTk.PhotoImage(pag2)
            canvas.create_image(0, 0, image=pag2stp, anchor="nw")
            
            string_user = tk.Label(pag2setup, text="Bem-Vindo, "+nome +"!", bg="#174552",font=("Product Sans", 30),fg="white",anchor="center")
            canvas.create_window(250, 219, window=string_user)

       
            avancar = Image.open("assets\\btn_proximo.png")
            avancar2 = ImageTk.PhotoImage(avancar)
            avancar3 = canvas.create_image(236, 445, image=avancar2, anchor="nw")
           

            def continuarOOBE(event):
                pag2setup.withdraw()

                pag_tema = tk.Toplevel()
                pag_tema.geometry("500x500")
                pag_tema.title("Bem-Vindo ao Coinly!")
                pag_tema.resizable(False, False)

                canvas_tema = tk.Canvas(pag_tema, width=500, height=500, bg="#124958", bd=0, highlightthickness=0)
                canvas_tema.pack(fill="both", expand=True)

                seltema = Image.open("assets\\bg_selTema.png")
                seltema2 = ImageTk.PhotoImage(seltema)

                canvas_tema.bg_image = seltema2

                canvas_tema.create_image(0, 0, image=seltema2, anchor="nw")

                canvas_tema.bg_image = seltema2
                canvas_tema.avancar_img = avancar2
                preto = canvas_tema.create_image(350, 420, image=canvas_tema.avancar_img, anchor="nw")
                
                def temabranco(event):
                    print("TEMA BRANCO")
                    pag_tema.withdraw()
                    fim_OOBE = tk.Toplevel()
                    fim_OOBE.geometry("500x500")
                    fim_OOBE.title("Bem-Vindo ao Coinly!")
                    fim_OOBE.resizable(False, False)
                    canvas = tk.Canvas(fim_OOBE, width=500, height=500, bg="#124958", bd=0, highlightthickness=0)
                    canvas.pack(fill="both", expand=True)

                    def reniciar():
                        config = ConfigParser()
                        config.read('coinly.conf')
                        config.set("CoinlyUser","faseoobe","1")
                        with open('coinly.conf', 'w') as f:
                            config.write(f)

                        cursor.execute("""
                            CREATE TABLE IF NOT EXISTS despesas (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                tipo VARCHAR(255) UNIQUE,
                                quantidade FLOAT DEFAULT 0
                            )""")
                        
                        dadosZero = [
                            ('pessoais', 0),
                            ('financeiras', 0),
                            ('seguros', 0),
                            ('contas_casa', 0),
                            ('alimentacao', 0),
                            ('renda_prestacao', 0),
                            ('transporte', 0),
                            ('lazer', 0),
                        ]

                        for tipo, quantidade in dadosZero:
                            cursor.execute("""
                            INSERT INTO despesas (tipo, quantidade) VALUES (%s, %s)
                            ON DUPLICATE KEY UPDATE quantidade = quantidade
                            """, (tipo, quantidade))


                        database.commit()
                        cursor.close()
                        database.close()


                        os.execl(sys.executable, sys.executable, *sys.argv)

                    oobemsg = Image.open("assets\\oobeFim.png")
                    oobemsg2 = ImageTk.PhotoImage(oobemsg)
                    canvas.create_image(0, 0, image=oobemsg2, anchor="nw")
                    
                    fim_OOBE.after(6000, reniciar)
                    fim_OOBE.mainloop()

                def temapreto(event): 
                    print("TEMA BRANCO")

                
                branco = canvas_tema.create_image(120, 420, image=canvas_tema.avancar_img, anchor="nw")

                canvas_tema.tag_bind(preto, "<Button-1>",temapreto)
                canvas_tema.tag_bind(branco, "<Button-1>",temabranco)


            canvas.tag_bind(avancar3, "<Button-1>",continuarOOBE)

            pag2setup.mainloop()
            
    otalbotao = canvas.create_image(236, 445, image=btn_proximo2, anchor="nw")
    canvas.tag_bind(otalbotao, "<Button-1>",updateNome)

    config = ConfigParser()
    config.read('coinly.conf')

    config.set("CoinlyUser","nutilizador","")   #RESET
    config.set("CoinlyUser","darkmode","0")


    with open('coinly.conf', 'w') as f:
        config.write(f)
    
    pag_nome.mainloop()

