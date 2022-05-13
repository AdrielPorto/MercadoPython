from View.view import *


class CompraView(View):
    __dropdown = ""
    __frame_dropdown = ""

    def __init__(self, btn_name1, btn_name2, btn_name3, title_h1):
        super(CompraView, self).__init__(
            btn_name1, btn_name2, btn_name3, title_h1=title_h1
        )
        self.buttons(self.informarCompra,
                     self.excluirCompra, self.buscarCompra)
        self.entradas = {}
        self.botaos = {}
        self.root.mainloop()

    def informarCompra(self):
        self.init_frame('Informar Compra')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas

        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('SALVAR', 240, 180, None)

    def excluirCompra(self):
        self.init_frame('Excluir Compra')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas

        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('EXCLUIR', 240, 180, None)

    def buscarCompra(self):
        self.init_frame('Buscar Compra')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas
        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('BUSCAR', 240, 180, self.busca)

    def criar_botao(self, nome, posicaoY, posicaoX, funcao):
        botao = Button(
            self.frame_down,
            text=nome,
            width=15,
            height=1,
            anchor="center",
            font="Ubuntu 10 bold",
            bg=self.co0,
            fg=self.co1,
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
        self.init_frame(title_h1="Controle de compra")
        self.buttons(
            self.informarCompra, self.excluirCompra, self.buscarCompra)

    def area_busca(self):
        self.__frame_dropdown = LabelFrame(
            self.root, height=300, width=280, text="::::::::::::::: Cliente buscado :::::::::::::::")
        self.__frame_dropdown.place(x=10, y=120)

        label_id = Label(self.__frame_dropdown, text="ID: ",
                         width=10, anchor='w').grid(row=1, column=1)
        id = Label(self.__frame_dropdown, text="#01",
                   width=30, anchor='w').grid(row=1, column=2)

        label_nome = Label(self.__frame_dropdown, text="Nome: ",
                           width=10, anchor="w").grid(row=2, column=1)
        nome = Label(self.__frame_dropdown, text="Vinicius de Abreu Massena",
                     width=30, anchor='w').grid(row=2, column=2)

        label_local = Label(self.__frame_dropdown, text="Local: ",
                            width=10, anchor="w").grid(row=3, column=1)
        local = Label(self.__frame_dropdown, text="Rio de Janeiro",

                      width=30, anchor='w').grid(row=3, column=2)
        label_email = Label(self.__frame_dropdown, text="E-mail: ",
                            width=10, anchor="w").grid(row=4, column=1)
        email = Label(self.__frame_dropdown, text="vinicius.massena@soulasalle.com.br",
                      width=30, anchor='w').grid(row=4, column=2)

        label_celular = Label(self.__frame_dropdown, text="Celular: ",
                              width=10, anchor="w").grid(row=5, column=1)
        celular = Label(self.__frame_dropdown, text="21 99999-9999",
                        width=30, anchor='w').grid(row=5, column=2)

        self.__frame_dropdown.pack_forget()

    def busca(self):
        valor = self.__dropdown.get()
        print(valor)
        if (valor):
            self.area_busca()
