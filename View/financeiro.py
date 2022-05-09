from view import View, MainView


class FinanceiroView(View):
    def __init__(self, btn_name1, btn_name2, btn_name3, title_h1):
        super(FinanceiroView, self).__init__(
            btn_name1, btn_name2, btn_name3, title_h1=title_h1
        )
        self.buttons(self.informarPagamento, self.relatorio)
        self.root.mainloop()

    def informarPagamento(self):
        print("Informando pagamento")

    def relatorio(self):
        print("Gerando relatorio")
