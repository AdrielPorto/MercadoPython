from view import View, MainView


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
        self.criar_botao('BUSCAR', 240, 180, None)

    def cancelar(self):
        self.init_frame(title_h1="Informar Compras")
        self.buttons(self.informarCompra,
                     self.excluirCompra, self.buscarCompra)

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
