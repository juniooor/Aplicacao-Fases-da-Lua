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


    def criar(self, nome, email, cidade):
        #NA Função criar() passar os parametros nome e email do usuario
        comando = f'INSERT INTO dados(nome, email, cidade) VALUES ("{nome}", "{email}", "{cidade}")'
        self.cursor.execute(comando)
        self.conexao.commit()
        # self.cursor.close()
        # self.conexao.close()

        
        
    def alter_dados(self, Nome, email, Cidade):
        #alterar cidade na base dados passa o email correto e o nome da cidade para cadastro
        comando = f'UPDATE dados SET cidade = "{Cidade}", nome = "{Nome}"  WHERE email = "{email}" LIMIT 1'
        self.cursor.execute(comando)
        self.conexao.commit()
        # self.cursor.close()
        # self.conexao.close()

    

    def Deletar(self, email):
        #deletar usuario usando o email do usuario
        comando = f'DELETE FROM dados WHERE email = "{email}"'
        self.cursor.execute(comando)
        self.conexao.commit()
        # self.cursor.close()
        # self.conexao.close()

        




