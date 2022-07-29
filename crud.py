import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_crud',
)


cursor = conexao.cursor()

nome = "Layla"
numero = "81987899167"
        

comando = f'INSERT INTO dados (nome,numero) VALUES ("{nome}", "{numero}")'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()