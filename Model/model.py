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
                CONTATO TEXT NOT NULL
               )''')
        except Exception as e:
            print(f'Falha ao criar tabela: {e}')
        else:
            return 'Tabela criada com sucesso'

    def insere_cliente(self, user):
        try:
            self.c.execute(
                '''INSERT INTO CLIENTE (NOME,LOCAL,EMAIL,CONTATO) VALUES (?, ?, ?, ?)''', user)
        except Exception as e:
            print(f'Falha ao inserir dados: {e}')
            self.conectar.rollback()

        else:
            self.conectar.commit()
            return 'Dados inseridos com sucesso!'

    def Get_AllCliente(self):
        return self.c.execute(''' SELECT * FROM CLIENTE''').fetchall()

    def Get_Cliente(self, rowid):
        return self.c.execute(''' SELECT * FROM CLIENTE WHERE rowid=?''', (rowid,)).fetchone()

    def Get_nome_id(self):
        return self.c.execute(''' SELECT ID, Nome FROM CLIENTE ''').fetchall()

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
                ID_CLiente INTEGER,
                FOREIGN KEY(ID_Cliente) REFERENCES CLIENTE(ID)
                )''')
        except Exception as e:
            print(f'Falha ao criar tabela: {e}')
        else:
            return 'Tabela criada com sucesso'

    def insere_produto(self, produto):

        try:
            self.c.execute(
                '''INSERT INTO INFOCOMPRA
                (
                QUANTIDADE_PRODUTO,
                DESCRICAO,
                PRECO,
                TOTAL_PRODUTO,
                PRECO_TOTAL,
                FORMA_PGT,
                QNTD_PARCELA,
                VL_PARCELA,
                ID_CLiente
                ) 
                VALUES (?,?,?,?,?,?,?,?,?)''', produto)

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
            self.c.execute(
                '''DELETE FROM INFOCOMPRA WHERE rowid=?''', (rowid,))
        except Exception as e:
            print(f'Falha ao remover valores: {e}')
            self.conectar.rollback()
        else:
            self.conectar.commit()
            return 'Dados removidos com sucesso!!!!'

    def join_tabela(self):
        self.c.execute('''SELECT ID, NOME,
                                 DESCRICAO,
                                    QUANTIDADE_PRODUTO,
                                    PRECO,
                                    TOTAL_PRODUTO
                          FROM INFOCOMPRA
                          INNER JOIN CLIENTE
                          ON INFOCOMPRA.ID_Cliente = CLIENTE.ID;''')
        resultado = self.c.fetchall()
        for row in resultado:
            print(row)
