import tkinter as tk
from PIL import Image, ImageTk
import datetime
import time
from setup_coinly import *
from configparser import ConfigParser 
import sys 

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
    canvas.create_image(40, 201, image=rendimento2, anchor="nw")
    
    despesa = Image.open("assets\\despesa_Grande.png")
    despesa2 = ImageTk.PhotoImage(despesa)
    canvas.create_image(40, 312, image=despesa2, anchor="nw")
    
    btnAnterior = Image.open("assets\\btn_anterior.png")
    btnAnterior2 = ImageTk.PhotoImage(btnAnterior)
    canvas.create_image(235, 445, image=btnAnterior2, anchor="nw")


    adicionar.mainloop()