import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_crud',
)


cursor = conexao.cursor()


# CRIAR
nome = "Junior"
numero = "81996316701" 

comando = f'INSERT INTO dados (nome,numero) VALUES ("{nome}", "{numero}")'
cursor.execute(comando)
conexao.commit()



#READ/LER
comando = f'SELECT * FROM dados'
cursor.execute(comando)
resultado = cursor.fetchall() #ler banco de dados
print(resultado)


#UPDATE
# if usuarioclick == "alterar numero":
numerod = '81999999999'
nomed = 'Junior' 
comando = f'UPDATE dados SET numero = "{numerod}" WHERE nome = "{nomed}" '
elif usuarioclick=="alterar nome":
    numerod = '81999999999'
    nomed = 'jujunior' 
    comando = f'UPDATE dados SET  nome = "{nomed}" WHERE numero = "{numerod}" '

cursor.execute(comando)
conexao.commit()




#DELETE
# # if usuarioclick == "deletar usuario":
# numerod = '81999999999'
# comando = f'DELETE FROM  dados WHERE numero = "{numerod}" '
# # # elif usuarioclick=="alterar nome":
# # #     numerod = '81999999999'
# # #     nomed = 'jujunior' 
# # #     comando = 'UPDATE dados SET  nome = "{nomed}" WHERE numero = "{numerod}" '

# cursor.execute(comando)
# conexao.commit()






cursor.close()
conexao.close()