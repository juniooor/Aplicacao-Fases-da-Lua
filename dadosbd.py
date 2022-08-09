import mysql.connector
from mysql.connector import Error


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
    print("numero total de registro retornados", cursor.rowcount )
    
    print("\n Mostrando os dados cadastrados")
    for linha in linhas:
        print(f"id: {linha[0]}")
        print(f"nome: {linha[1]}")
        print(f"email: {linha[2]} \n")
        
except Error as err:
    print("error na tabela ", err)
    
finally:
    if conexao.is_connected():
        conexao.close()
        cursor.close()
        print('fechou')