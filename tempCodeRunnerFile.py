# CRIAR
nome = "Junior"
numero = "81996316701" 

comando = f'INSERT INTO dados (nome,numero) VALUES ("{nome}", "{numero}")'
cursor.execute(comando)
conexao.commit()