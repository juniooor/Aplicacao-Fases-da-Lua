import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_crud',
)


cursor = conexao.cursor()


# # CRIAR
# nome = "Junior"
# email = "81996316701" 

# comando = f'INSERT INTO dados (nome,email) VALUES ("{nome}", "{email}")'
# cursor.execute(comando)
# conexao.commit()



# #READ/LER
# comando = f'SELECT * FROM dados'
# cursor.execute(comando)
# resultado = cursor.fetchall() #ler banco de dados
# print(resultado)


#UPDATE
# if usuarioclick == "alterar email":
emaild = '8181818199'
nomed = 'leticya' 
comando = f'UPDATE dados SET email = "{emaild}" WHERE nome = "{nomed}" '
# elif usuarioclick=="alterar nome":
#     emaild = '81999999999'
#     nomed = 'jujunior' 
#     comando = f'UPDATE dados SET  nome = "{nomed}" WHERE email = "{emaild}" '

cursor.execute(comando)
conexao.commit()




#DELETE
# # if usuarioclick == "deletar usuario":
# emaild = '81999999999'
# comando = f'DELETE FROM  dados WHERE email = "{emaild}" '
# # # elif usuarioclick=="alterar nome":
# # #     emaild = '81999999999'
# # #     nomed = 'jujunior' 
# # #     comando = 'UPDATE dados SET  nome = "{nomed}" WHERE email = "{emaild}" '

# cursor.execute(comando)
# conexao.commit()






cursor.close()
conexao.close()