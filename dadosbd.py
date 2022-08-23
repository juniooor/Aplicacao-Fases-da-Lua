import mysql.connector
from mysql.connector import Error

#AQUI IREI PEGAR AS LINHAS DA TABELA DO BANCO DE DADOS E RETORNAR PARA FUNÇÃO ENVIAR
# podendo usar ex:  linhas[3] = que retornar o email do usuario

try:
    conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_crud', 
        )
    
    consulta_sql = "select * from dados"
    cursor = conexao.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    total_de_dados = cursor.rowcount 
    
        
except Error as err:
    print("error na tabela ", err)
    
finally:
    if conexao.is_connected():
        conexao.close()
        cursor.close()