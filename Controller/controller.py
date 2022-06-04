from Model.model import ConectBD
try:
    import Tkinter as tk
except:
    import tkinter as tk


class Controller():
    def __init__(self):
        self.bd = ConectBD()

    def cadastrarCliente(self, entrada):
        clientes = ()
        print("Cadastrando cliente")
        for item, valor in entrada.items():
            if(valor.get().strip() == ""):
                return
            clientes += (valor.get(),)

        self.bd.insere_cliente(user=clientes)

    def excluirCliente(self, rowid):
        print("Excluindo cliente")
        self.bd.remove_cliente(rowid)

    def buscarCliente(self, rowid):
        print("Buscando cliente")
        return self.bd.Get_Cliente(rowid)

    def buscarNomeIdCliente(self):
        lista = []
        mapping = {}
        print("Buscando cliente")
        for item in self.bd.Get_nome_id():

            lista.append(item[1])
            mapping[item[1]] = item[0]

        return [lista, mapping]
