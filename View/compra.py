from textwrap import fill
import tkinter

from View.view import *
import tk_tools


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
        self.botao_fechar.config(command=self.root.destroy)

    def informarCompra(self):
        self.init_frame('Informar Compra')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas
        entry_grid = tk_tools.EntryGrid(
            self.root, 4, ['QTD', 'ITEM', 'DESCRICAO', 'VALOR'])
        entry_grid.place(x=50, y=110)
        for i in range(0, 10):
            entry_grid.add_row()
        print(entry_grid)
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
        botao = customtkinter.CTkButton(
            self.frame_down,
            text=nome,
            width=150,
            height=10,
            # anchor="center",
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
        self.__dropdown.configure(width=60)
        self.__dropdown.place(x=50, y=80)

    def cancelar(self):
        self.init_frame(title_h1="Controle de compra")
        self.buttons(
            self.informarCompra, self.excluirCompra, self.buscarCompra)

    def area_busca(self):
        self.__frame_dropdown = LabelFrame(
            master=self.root, font="Tahoma 13 bold", text="::::::::::::::: Cliente buscado :::::::::::::::",
            bg=self.co1,
            fg=self.co0,
            # scrollbar_tk = ttk.Scrollbar(self.__frame_dropdown, orient="vertical")
        )
        # scrollbar_tk.pack(side=RIGHT, fill="y")
        self.__frame_dropdown.place(x=50, y=120, height=150, width=380)

        label_id = Label(self.__frame_dropdown, text="ID: ", bg=self.co1,
                         width=10, anchor='w').grid(row=1, column=1)
        id = Label(self.__frame_dropdown, text="#01", bg=self.co1,
                   width=30, anchor='w').grid(row=1, column=2)

        label_nome = Label(self.__frame_dropdown, text="Nome: ", bg=self.co1,
                           width=10, anchor="w").grid(row=2, column=1)
        nome = Label(self.__frame_dropdown, text="Vinicius de Abreu Massena", bg=self.co1,
                     width=30, anchor='w').grid(row=2, column=2)

        label_produto = Label(self.__frame_dropdown, text="Produto: ", bg=self.co1,
                              width=10, anchor="w").grid(row=3, column=1)
        produto = Label(self.__frame_dropdown, text="Produto 1", bg=self.co1,

                        width=30, anchor='w').grid(row=3, column=2)
        label_quantidade = Label(self.__frame_dropdown, text="Quantidade: ", bg=self.co1,
                                 width=10, anchor="w").grid(row=4, column=1)
        quantidade = Label(self.__frame_dropdown, text="2", bg=self.co1,
                           width=30, anchor='w').grid(row=4, column=2)

        label_valor = Label(self.__frame_dropdown, text="Valor: ", bg=self.co1,
                            width=10, anchor="w").grid(row=5, column=1)
        valor = Label(self.__frame_dropdown, text="R$50,00", bg=self.co1,
                      width=30, anchor='w').grid(row=5, column=2)

        label_total = Label(self.__frame_dropdown, text="Total: ", bg=self.co1,
                            width=10, anchor="w").grid(row=5, column=1)
        total = Label(self.__frame_dropdown, text="R$100,00", bg=self.co1,
                      width=30, anchor='w').grid(row=5, column=2)

        self.__frame_dropdown.pack_forget()

    def busca(self):
        valor = self.__dropdown.get()
        print(valor)
        if (valor):
            self.area_busca()
