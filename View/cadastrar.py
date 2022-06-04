from View.view import *
from Controller.controller import *


class CadastrarView(View):
    __dropdown = ""
    __frame_dropdown = ""
    __itemDropdown = None
    __valorId = None

    def __init__(self, btn_name1, btn_name2, btn_name3, title_h1):
        super(CadastrarView, self).__init__(
            btn_name1, btn_name2, btn_name3, title_h1=title_h1
        )
        self.entradas = {}
        self.botaos = {}
        self.controller = Controller()
        self.buttons(self.inserirCliente,
                     self.excluirCliente, self.buscarCliente)
        self.botao_fechar.config(command=self.root.destroy)

    def inserirCliente(self):
        self.init_frame('Inserindo cliente')  # Inicializa o frame
        # Cria as entradas
        self.criar_entrada('Nome', 60, 10, 85, tk.StringVar)
        self.criar_entrada('Local', 115, 10, 140,
                           tk.StringVar)  # Cria as entradas
        self.criar_entrada('E-mail', 170, 10, 195,
                           tk.StringVar)  # Cria as entradas
        self.criar_entrada('DDD + Celular', 225, 10, 250,
                           tk.IntVar)  # Cria as entradas
        self.criar_botao('CANCELAR', 250, 10, self.cancelar)
        self.criar_botao('SALVAR', 250, 180, self.salvarCliente)

    def excluirCliente(self):
        self.init_frame('Excluindo cliente')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas
        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('EXCLUIR', 240, 180, self.excluir)

    def buscarCliente(self):
        self.init_frame('Buscar cliente')  # Inicializa o frame
        self.criar_dropdown()  # Cria as entradas
        self.criar_botao('CANCELAR', 240, 10, self.cancelar)
        self.criar_botao('BUSCAR', 240, 180, self.busca)

    def criar_entrada(self, labelTxt, posicaoY, posicaoX, posicaoYEntry, textvar):
        label = Label(self.root, text=labelTxt, bg=self.co0,
                      fg=self.co1, font="Ubuntu 12 bold")
        label.place(x=10, y=posicaoY)
        self.entradas[labelTxt] = Entry(
            self.root, textvariable=textvar, width=30, bd=0, font="arial 12")
        self.entradas[labelTxt].place(x=posicaoX, y=posicaoYEntry)

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
        self.__itemDropdown = self.controller.buscarNomeIdCliente()

        options = sorted(self.__itemDropdown[0])

        self.__dropdown = ttk.Combobox(
            self.root, state="readonly", values=options)

        self.__dropdown.set(options[0])
        self.__valorId = self.__itemDropdown[1][options[0]]

        self.__dropdown.configure(width=30)
        self.__dropdown.place(x=50, y=80)
        self.__dropdown.bind('<<ComboboxSelected>>', lambda e: self.selecionarCliente(
            e, self.__itemDropdown[1]))

    def cancelar(self):
        self.init_frame(title_h1="Controle de clientes")
        self.buttons(self.inserirCliente,
                     self.excluirCliente, self.buscarCliente)

    def area_busca(self, valor):
        self.__frame_dropdown = LabelFrame(
            self.root, font="Tahoma 13 bold", height=300, width=280,
            text="::::::::::::::: Cliente buscado :::::::::::::::", bg=self.co1, fg=self.co0)
        self.__frame_dropdown.place(x=10, y=120, height=150, width=380)

        label_id = Label(self.__frame_dropdown, text="ID: ", bg=self.co1,
                         width=10, anchor='w').grid(row=1, column=1)
        id = Label(self.__frame_dropdown, text=valor[0], bg=self.co1,
                   width=30, anchor='w').grid(row=1, column=2)

        label_nome = Label(self.__frame_dropdown, text="Nome: ", bg=self.co1,
                           width=10, anchor="w").grid(row=2, column=1)
        nome = Label(self.__frame_dropdown, text=valor[1], bg=self.co1,
                     width=30, anchor='w').grid(row=2, column=2)

        label_local = Label(self.__frame_dropdown, text="Local: ", bg=self.co1,
                            width=10, anchor="w").grid(row=3, column=1)
        local = Label(self.__frame_dropdown, text=valor[2], bg=self.co1,

                      width=30, anchor='w').grid(row=3, column=2)
        label_email = Label(self.__frame_dropdown, text="E-mail: ", bg=self.co1,
                            width=10, anchor="w").grid(row=4, column=1)
        email = Label(self.__frame_dropdown, text=valor[3], bg=self.co1,
                      width=30, anchor='w').grid(row=4, column=2)

        label_celular = Label(self.__frame_dropdown, text="Celular: ", bg=self.co1,
                              width=10, anchor="w").grid(row=5, column=1)
        celular = Label(self.__frame_dropdown, text=valor[4], bg=self.co1,
                        width=30, anchor='w').grid(row=5, column=2)

        self.__frame_dropdown.pack_forget()

    def busca(self):
        print(f'clinte buscado: {self.__valorId}')
        valor = self.controller.buscarCliente(self.__valorId)
        if(valor):
            self.area_busca(valor)

    def salvarCliente(self):
        self.controller.cadastrarCliente(self.entradas)
        for item, valor in self.entradas.items():
            valor.delete(0, END)

    def selecionarCliente(self, event, item):
        self.__valorId = item[event.widget.get()]

    def excluir(self):
        self.controller.excluirCliente(self.__valorId)
        self.criar_dropdown()  # Cria as entradas
