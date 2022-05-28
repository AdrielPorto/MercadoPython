# MercadoPythonfrom view import *


class CadastrarView(View):
    __dropdown = ""
    __frame_dropdown = ""

    def __init__(self, btn_name1, btn_name2, btn_name3, title_h1):
        super(CadastrarView, self).__init__(
            btn_name1, btn_name2, btn_name3, title_h1=title_h1
        )
        self.entradas = {}
        self.botaos = {}
        self.buttons(self.inserirCliente,
                     self.excluirCliente, self.buscarCliente)
                     
        self.root.mainloop()

    def inserirCliente(self):
        self.init_frame('Inserindo cliente')  # Inicializa o frame
        self.criar_entrada('Nome', 60, 10, 85, tk.StringVar)  # Cria as entradas
        self.criar_entrada('Local', 115, 10, 140, tk.StringVar)  # Cria as entradas
        self.criar_entrada('E-mail', 170, 10, 195, tk.StringVar)  # Cria as entradas
        self.criar_entrada('DDD + Celular', 225, 10, 250,
                           tk.IntVar)  # Cria as entradas
        self.criar_botao('CANCELAR', 250, 10, self.cancelar)
        
        self.criar_botao('SALVAR', 250, 180, None)

    def excluirCliente(self):
        self.init_frame('Excluindo cliente')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas
        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('EXCLUIR', 240, 180, None)

    def buscarCliente(self):
        self.init_frame('Buscar cliente')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas
        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('BUSCAR', 240, 180, self.busca)

    def criar_entrada(self, label, posicaoY, posicaoX, posicaoYEntry, textvar):
        label = Label(self.root, text=label, bg=self.co0, fg=self.co1, font="Ubuntu 12 bold")
        label.place(x=10, y=posicaoY)
        self.entradas[label] = Entry(
            self.root, textvariable=textvar, width=30, bd=0, font="arial 12")
        self.entradas[label].place(x=posicaoX, y=posicaoYEntry)
        print(self.entradas)

    def criar_botao(self, nome, posicaoY, posicaoX, funcao):
        botao = customtkinter.CTkButton(
            self.frame_down,
            text=nome,
            width=150,
            height=10,
            text_font="Ubuntu 10 bold",
            fg_color=self.co1,
            hover_color=None,
            relief=RAISED,
            command=funcao,
        )

        botao.place(x=posicaoX, y=posicaoY)

    def criar_dropdown(self):
        options = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
        self.__dropdown = ttk.Combobox(
            self.root, state="readonly", values=options)
        self.__dropdown.current(0)
        self.__dropdown.configure(width=30)
        self.__dropdown.place(x=50, y=80)

    def cancelar(self):
        self.init_frame(title_h1="Controle de clientes")
        self.buttons(self.inserirCliente,
                     self.excluirCliente, self.buscarCliente)

    def area_busca(self):
        self.__frame_dropdown = LabelFrame(
            self.root,font="Tahoma 13 bold", height=300, width=280, text="::::::::::::::: Cliente buscado :::::::::::::::", bg=self.co1, fg=self.co0)
        self.__frame_dropdown.place(x=10, y=120, height=150, width=380)

        label_id = Label(self.__frame_dropdown, text="ID: ",bg=self.co1,
                         width=10, anchor='w').grid(row=1, column=1)
        id = Label(self.__frame_dropdown, text="#01",bg=self.co1,
                   width=30, anchor='w').grid(row=1, column=2)

        label_nome = Label(self.__frame_dropdown, text="Nome: ", bg=self.co1,
                           width=10, anchor="w").grid(row=2, column=1)
        nome = Label(self.__frame_dropdown, text="Vinicius de Abreu Massena", bg=self.co1,
                     width=30, anchor='w').grid(row=2, column=2)

        label_local = Label(self.__frame_dropdown, text="Local: ", bg=self.co1,
                            width=10, anchor="w").grid(row=3, column=1)
        local = Label(self.__frame_dropdown, text="Rio de Janeiro", bg=self.co1,

                      width=30, anchor='w').grid(row=3, column=2)
        label_email = Label(self.__frame_dropdown, text="E-mail: ", bg=self.co1,
                            width=10, anchor="w").grid(row=4, column=1)
        email = Label(self.__frame_dropdown, text="vinicius.massena@soulasalle.com.br", bg=self.co1,
                      width=30, anchor='w').grid(row=4, column=2)

        label_celular = Label(self.__frame_dropdown, text="Celular: ", bg=self.co1,
                              width=10, anchor="w").grid(row=5, column=1)
        celular = Label(self.__frame_dropdown, text="21 99999-9999", bg=self.co1,
                        width=30, anchor='w').grid(row=5, column=2)

        self.__frame_dropdown.pack_forget()

    def busca(self):
        valor = self.__dropdown.get()
        print(valor)
        if (valor):
            self.area_busca()

