from View.view import *
from View.compra import *
from View.financeiro import *
from View.cadastrar import *
from Controller.controller import *


class MainView(View):
    def __init__(self, btn_name1, btn_name2, btn_name3, title_h1):
        super(MainView, self).__init__(
            btn_name1, btn_name2, btn_name3, title_h1=title_h1
        )
        self.buttons(self.cadastrar, self.comprar, self.financeiro)
        self.botao_fechar.config(command=self.root.destroy)

        self.root.mainloop()

    def cadastrar(self):
        cadastro = CadastrarView("Inserir cliente", "Excluir cliente",
                                 "Buscar cliente", "Controle de clientes")

    def comprar(self):
        compra = CompraView("Informar compra", "Excluir compra",
                            "Buscar compra", "Controle de compras")

    def financeiro(self):
        financeiro = FinanceiroView(
            "Informar Pagamento", "Relatório", None, "Controle de pagamentos")


teste = MainView("Cadastrar", "Comprar", "Financeiro", 'Controle De Vendas')
