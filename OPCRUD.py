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

    def criar(self, nome, numero):
        #NA Função criar() passar os parametros nome e numero do usuario
        comando = f'INSERT INTO dados(nome, numero) VALUES ("{nome}", "{numero}")'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alter_Number(self, nome, numero):
        #alterar numero na base de dados passa  o nome correto e o numero novo para atualizar
        comando = f'UPDATE dados SET numero = "{numero}" WHERE nome = "{nome}" LIMIT 1 '
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alter_Name(self, nome, numero):
        #alterar nome na base dados passa o numero correto e o nome novo para cadastro
        comando = f'UPDATE dados SET nome = "{nome}" WHERE numero = "{numero}" LIMIT 1'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


    def Deletar(self, numero):
        #deletar usuario usando o numero de celular
        comando = f'DELETE FROM dados WHERE numero = "{numero}"'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

        



if __name__ == '__main__':
    try:
        cadastro = Cadastrar()
        cadastro.Deletar(numero='99595959555')
    except:
        print('ALÔ KLEITINHO A CASA CAIU')
    
    finally:
        print('positivo e operante')
