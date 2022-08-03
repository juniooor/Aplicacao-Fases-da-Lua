from distutils.log import error
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
        comando = f'UPDATE dados SET numero = "{numero}" WHERE nome = "{nome}" '
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()

    def alter_Name(self, nome, numero):
        comando = f'UPDATE dados SET nome = "{nome}" WHERE numero = "{numero}"'
        self.cursor.execute(comando)
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()


        



if __name__ == '__main__':
    try:
        cadastro = Cadastrar()
        cadastro.criar(nome='jujunior', numero='99979777')
    except:
        print('ALÔ KLEITINHO A CASA CAIU')
    
    finally:
        print('positivo e operante')
