import mysql.connector

class Cadastrar:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_crud',
        )
        self.cursor = self.conexao.cursor()

    def criar(self, nome, email):
        #NA Função criar() passar os parametros nome e email do usuario
        comando = f'INSERT INTO dados(nome, email) VALUES ("{nome}", "{email}")'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alter_Number(self, nome, email):
        #alterar email na base de dados passa  o nome correto e o email novo para atualizar
        comando = f'UPDATE dados SET email = "{email}" WHERE nome = "{nome}" LIMIT 1 '
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alter_Name(self, nome, email):
        #alterar nome na base dados passa o email correto e o nome novo para cadastro
        comando = f'UPDATE dados SET nome = "{nome}" WHERE email = "{email}" LIMIT 1'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def Deletar(self, email):
        #deletar usuario usando o email do usuario
        comando = f'DELETE FROM dados WHERE email = "{email}"'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

        



if __name__ == '__main__':
    try:
        cadastro = Cadastrar()
        cadastro.criar(nome='Vania', email="jvaniacosta@hotmail.com")
    except:
        print('ALÔ KLEITINHO A CASA CAIU')
    
    finally:
        print('positivo e operante')
