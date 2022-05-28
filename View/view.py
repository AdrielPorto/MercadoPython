try:
    import Tkinter as tk
except:
    import tkinter as tk
from logging import root
from tkinter import ttk
from tkinter import *
import customtkinter
 

class MoldView(tk.Frame):
    def __init__(self, title_h1):
        self.root = tk.Tk()

        self.co0 = "#1B7572"  # cor verde
        self.co1 = "#feffff"  # Cor branco
        self.co2 = "#4F4F4F"  # cor cinza
        self.frame_up = ""
        self.frame_down = ""
        self.title_h1 = title_h1
        #self.root.focus_force()
        #self.root.grab_set()
        self.root.title("Sistema Mercado")
        self.root.geometry(
            "%dx%d+%d+%d"
            % (
                650,
                350,
                ((self.root.winfo_screenwidth() / 2) - 100),
                ((self.root.winfo_screenheight() / 2) - 200),
            )
        )
        self.root.configure(background=self.co0)
        #self.root.resizable(False, False)
        self.init_framtry:
    import Tkinter as tk
except:
    import tkinter as tk
from logging import root
from tkinter import ttk
from tkinter import *
import customtkinter
 

class MoldView(tk.Frame):
    def __init__(self, title_h1):
        self.root = tk.Tk()

        self.co0 = "#1B7572"  # cor verde
        self.co1 = "#feffff"  # Cor branco
        self.co2 = "#4F4F4F"  # cor cinza
        self.frame_up = ""
        self.frame_down = ""
        self.title_h1 = title_h1
        #self.root.focus_force()
        #self.root.grab_set()
        self.root.title("Sistema Mercado")
        self.root.geometry(
            "%dx%d+%d+%d"
            % (
                650,
                350,
                ((self.root.winfo_screenwidth() / 2) - 100),
                ((self.root.winfo_screenheight() / 2) - 200),
            )
        )
        self.root.configure(background=self.co0)
        #self.root.resizable(False, False)
        self.init_frame(self.title_h1)

    def init_frame(self, title_h1):
        self.frame_up = Frame(
            self.root, width=650, height=50, bg=self.co1, relief="flat"
        )
        self.frame_up.grid(row=0, column=0, pady=1, padx=0, sticky=N)
        self.frame_down = Frame(
            self.root, width=650, height=350, bg=self.co0
            , relief="flat"
        )
        self.frame_down.grid(row=1, column=0, pady=1, padx=0, sticky=N)
        titulo_frameup = Label(
            self.frame_up,
            text=title_h1,
            anchor=N,
            font=("Ubuntu 18"),
            bg=self.co1,
            fg=self.co2,
        )
        titulo_frameup.place(x=200, y=7)


class View(MoldView):
    def __init__(self, btn_name1, btn_name2, btn_name3, title_h1):
        super(View, self).__init__(title_h1=title_h1)
        self.btn_name1 = btn_name1
        self.btn_name2 = btn_name2
        self.btn_name3 = btn_name3

    def buttons(self, funcao1, funcao2, funcao3=None):
        #self.btn_name1 = PhotoImage(file='View/imagens/btn-cadastrar.png', master=self.root)
        botao_cadastrar = customtkinter.CTkButton(
            master=self.frame_down,
            #image=self.btn_name1,
            text=self.btn_name1,
            corner_radius=30,
            width=250,
            height=40,
            text_font="Ubuntu 13 bold",
            fg_color=self.co1,
            text_color=self.co0,
            hover_color=None,
            relief=RAISED,
            command=funcao1,
        )
        botao_cadastrar.place(x=200, y=20)
        #botao_cadastrar.pack()

        botao_compra = customtkinter.CTkButton(
            self.frame_down,
            text=self.btn_name2,
            corner_radius=30,
            width=250,
            height=40,
            text_font="Ubuntu 13 bold",
            fg_color=self.co1,
            text_color=self.co0,
            hover_color=None,
            relief=RAISED,
            command=funcao2,

        )
        botao_compra.place(x=200, y=80)

        if (funcao3 != None):
            botao_financeiro = customtkinter.CTkButton(
                self.frame_down,
                text=self.btn_name3,
                corner_radius=30,
                width=250,
                height=40,
                text_font="Ubuntu 13 bold",
                fg_color=self.co1,
                text_color=self.co0,
                hover_color=None,
                relief=RAISED,
                command=funcao3,
            )
            botao_financeiro.place(x=200, y=140)

        botao_fechar = customtkinter.CTkButton(
            self.frame_down,
            text="Fechar",
            corner_radius=30,
            width=250,
            height=40,
            text_font="Ubuntu 13 bold",
            fg_color=self.co1,
            text_color=self.co0,
            hover_color=None,
            relief=RAISED,
            command=self.root.destroy,
        )
        botao_fechar.place(x=200, y=200)

