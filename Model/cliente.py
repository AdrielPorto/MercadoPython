import sqlite3


class ConectBD:

    def __init__(self):
        self.conectar = sqlite3.connect('VENDAS.db')
        self.c = self.conectar.cursor()
        self.cria_cliente()
        self.cria_produtos()

    def cria_cliente(self):

        try:
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS CLIENTE 
                (ID INTEGER PRIMARY KEY   AUTOINCREMENT, 
                NOME TEXT NOT NULL,
                LOCAL TEXT NOT NULL,
                EMAIL TEXT NOT NULL,
                CONTATO TEXT NOT NULL,
                CONSTRAINT FK_CLIENTE 
                FOREIGN KEY(ID) 
                REFERENCES INFOCOMPRA(ID_PRODUTO))''')
        except Exception as e:
            print(f'Falha ao criar tabela: {e}')
        else:
            return 'Tabela criada com sucesso'

    def insere_cliente(self, user):
        try:
            self.c.execute('''INSERT INTO CLIENTE (NOME,LOCAL,EMAIL,CONTATO) VALUES (?, ?, ?, ?)''', user)
        except Exception as e:
            print(f'Falha ao inserir dados: {e}')
            self.conectar.rollback()

        else:
            self.conectar.commit()
            return 'Dados inseridos com sucesso!'

    def Get_cliente(self):
        return self.c.execute(''' SELECT * FROM CLIENTE''').fetchall()

    def remove_cliente(self, rowid):
        try:
            self.c.execute('''DELETE FROM CLIENTE WHERE rowid=?''', (rowid,))
        except Exception as e:
            print(f'Falha ao remover valores: {e}')
            self.conectar.rollback()
        else:
            self.conectar.commit()
            return 'Dados removidos com sucesso'

    def cria_produtos(self):
        try:
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS INFOCOMPRA
                (ID_PRODUTO INTEGER PRIMARY KEY AUTOINCREMENT,
                QUANTIDADE_PRODUTO INTEGER,
                DESCRICAO TEXT,
                PRECO REAL,
                TOTAL_PRODUTO NUMERIC,
                PRECO_TOTAL INTEGER,
                FORMA_PGT TEXT,
                QNTD_PARCELA INTEGER,
                VL_PARCELA REAL,
                CONSTRAINT FK_PRODUTO 
                FOREIGN KEY(ID_PRODUTO) 
                REFERENCES CLIENTE(ID))''')
        except Exception as e:
            print(f'Falha ao criar tabela: {e}')
        else:
            return 'Tabela criada com sucesso'

    def insere_produto(self, user):

        try:
            self.c.execute(
                '''INSERT INTO INFOCOMPRA
                (QUANTIDADE_PRODUTO,
                DESCRICAO,
                PRECO,
                TOTAL_PRODUTO,
                PRECO_TOTAL,
                FORMA_PGT,
                QNTD_PARCELA,
                VL_PARCELA) 
                VALUES (?,?,?,?,?,?,?,?)''', user)

        except Exception as e:
            print(f'Falha ao inserir dados: {e}')
            self.conectar.rollback()
        else:
            self.conectar.commit()
            return 'Dados inseridos com sucesso'

    def get_produto(self, limit=10):
        return self.c.execute(''' SELECT * FROM INFOCOMPRA ''', (limit,)).fetchall()

    def remove_produto(self, rowid):
        try:
            self.c.execute('''DELETE FROM INFOCOMPRA WHERE rowid=?''', (rowid,))
        except Exception as e:
            print(f'Falha ao remover valores: {e}')
            self.conectar.rollback()
        else:
            self.conectar.commit()
            return 'Dados removidos com sucesso!!!!'

    def join_tabela(self):
        self.c.execute('''SELECT ID,NOME,
                                 ID_PRODUTO,
                                 DESCRICAO
                          FROM CLIENTE
                          INNER JOIN INFOCOMPRA
                          ON CLIENTE.ID = INFOCOMPRA.ID_PRODUTO;''')
        resultado = self.c.fetchall()
        for row in resultado:
            print(row)


if __name__ == '__main__':
    banco = ConectBD()
    banco.join_tabela()

# cliente = ("thamires", "FACULDADE", "renanmix09@gmail.com", '111111111')
# banco.insere_cliente(user=cliente)
# produto = (2.5, 'nescau', 40.60, 5, 50.00, 'Prazo', 3, 12.50)
# banco.insere_produto(user=produto)
