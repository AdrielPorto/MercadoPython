import sqlite3


class ConectBD:

    def __init__(self):
        self.conectar = sqlite3.connect('VENDAS.db')
        self.c = self.conectar.cursor()
        self.cria_cliente()
        self.cria_produtos()
        self.cria_financeiro()

    def cria_financeiro(self):
        try:
            self.c.execute(
                ''' CREATE TABLE IF NOT EXISTS FINANCEIRO
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DATA TEXT,
                DATA_1 TEXT,
                DATA_2 TEXT,
                ID_CLIENTE,
                FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTE(ID)
                )''')
        except Exception as e:
            return f'Falha o criar tabela: {e}'
        else:
            return 'Tabela criada com sucesso'

    def insere_financa(self):
        try:
            self.c.execute(
                '''INSERT INTO FINANCEIRO(
                    DATA,
                    DATA_1,
                    DATA_2)
                    VALUES (?,?,?)''')

        except Exception as e:
            return f'Falaha ao inserir dados:{e}'
        else:
            self.conectar.commit()
            return 'Dados inseridos com sucesso!'

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
                FORMA_PGT TEXT,
                QNTD_PARCELA INTEGER,
                VL_PARCELA REAL,
                ID_CLIENTE INTEGER,
                FOREIGN KEY(ID_CLIENTE) REFERENCES CLIENTE(ID)
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
                FORMA_PGT,
                QNTD_PARCELA,
                VL_PARCELA,
                ID_CLIENTE
                ) 
                VALUES (?,?,?,?,?,?,?,?)''', produto)

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

    def join_produto(self, rowid):
        self.c.execute('''
                    SELECT DISTINCT C.ID,
                   C.NOME,
                    I.ID_PRODUTO,
                   I.DESCRICAO,
                   I.FORMA_PGT,
                   I.QNTD_PARCELA,
                   I.PRECO,
                   F.DATA,
                   F.DATA_1,
                   F.DATA_2,
                   I.QUANTIDADE_PRODUTO,
                   I.TOTAL_PRODUTO
            FROM CLIENTE as C
                     LEFT JOIN INFOCOMPRA as I
                                ON I.ID_PRODUTO = C.ID
                     LEFT JOIN FINANCEIRO as F
                                ON F.ID = C.ID
            WHERE c.ID = rowid=?;''', (rowid,))

        resultado = self.c.fetchall()
        for row in resultado:
            print(row)
