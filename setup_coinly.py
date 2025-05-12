import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from configparser import ConfigParser

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
        rendimentoadd.destroy()

        config = ConfigParser()
        config.read('coinly.conf')
        config.set("CoinlyUser","estado_adicionar","1")

        with open('coinly.conf', 'w') as f:
            config.write(f)

    btn_concluir = Image.open("assets\\btn_concluir.png")
    btn_concluir2 = ImageTk.PhotoImage(btn_concluir)
    btnconcluir3 = canvas.create_image(187, 444, image=btn_concluir2, anchor="nw")
    canvas.tag_bind(btnconcluir3, "<Button-1>",concluir)


    rendimentoadd.mainloop()



def continuarOOBE(event):
    confirmar = ConfigParser()
    confirmar.read('coinly.conf')  
    check = confirmar['CoinlyUser']['estado_adicionar']

    if check == '0':
        erro = tk.Tk()
        erro.title("Coinly > Erro")
        msg_erro = tk.Label(erro,text="Por favor, Adicione pelo menos um item.",font=20)
        msg_erro.pack(padx=20,pady=20)
        erro.mainloop()
    elif check == '1':
        print("OK")


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




    opcoes = ["                                     ", "Renda / Prestação da casa", "Contas da Casa", "Seguros","Transporte","Alimentação ","Pessoais","Lazer","Financeiras"]
    opcao_var = tk.StringVar()
    opcao_var.set(opcoes[0])

    rendimentotipo = tk.OptionMenu(despesaadd, opcao_var, *opcoes,)
    rendimentotipo.config(bg="#0B313C", fg="white", font=("Arial", 15))
    rendimentotipo.pack(pady=20)

    canvas.create_window(250, 263, window=rendimentotipo)

    def concluir(event):
        despesaadd.destroy()

    btn_concluir = Image.open("assets\\btn_concluir.png")
    btn_concluir2 = ImageTk.PhotoImage(btn_concluir)
    btnconcluir3 = canvas.create_image(187, 444, image=btn_concluir2, anchor="nw")
    canvas.tag_bind(btnconcluir3, "<Button-1>",concluir)
    

    despesaadd.mainloop()


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

            rendimentobtn = Image.open("assets\\btn_rendimento_pequeno.png")
            rendimentobtn2 = ImageTk.PhotoImage(rendimentobtn)
            rendimentobtn3 = canvas.create_image(136, 379, image=rendimentobtn2, anchor="nw")

            despesabtn = Image.open("assets\\btn_despesa_pequeno.png")
            despesabtn2 = ImageTk.PhotoImage(despesabtn)
            despesabtn3 = canvas.create_image(136, 430, image=despesabtn2, anchor="nw")

            string_user = tk.Label(pag2setup, text="Bem-Vindo, "+nome +"!", bg="#174552",font=("Product Sans", 30),fg="white",anchor="center")
            canvas.create_window(250, 219, window=string_user)

            canvas.tag_bind(rendimentobtn3, "<Button-1>",adicionarrendimento)
            canvas.tag_bind(despesabtn3, "<Button-1>",adicionardespesa)

            avancar = Image.open("assets\\avancar_grande.png")
            avancar2 = ImageTk.PhotoImage(avancar)
            avancar3 = canvas.create_image(420, 400, image=avancar2, anchor="nw")
            canvas.tag_bind(avancar3, "<Button-1>",continuarOOBE)

            pag2setup.mainloop()
            
    otalbotao = canvas.create_image(236, 445, image=btn_proximo2, anchor="nw")
    canvas.tag_bind(otalbotao, "<Button-1>",updateNome)

    config = ConfigParser()
    config.read('coinly.conf')
    config.set("CoinlyUser","estado_adicionar","0")   #RESET

    with open('coinly.conf', 'w') as f:
        config.write(f)
    
    pag_nome.mainloop()

