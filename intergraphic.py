#encoding: utf-8
# import pandas as pd

# tabela = pd.read_csv("infos_contato.csv", sep=',', encoding= "utf-8")
# ver opção = Opção desejada
#  nome = Nome
# E-mail
#Cidade
import csv
import email
import opcrud

e = opcrud.exist
cadastro = opcrud.Cadastrar()
dados = []
with open ('infos_contato.csv', 'r', encoding='utf-8') as arquivo_csv:
    tabela = csv.reader(arquivo_csv)
    next(tabela)
    
    for a in tabela:
        dados.append(a)
        
   
   
    # for linha in tabela:
    #     print(linha)
    #     # dados.append(linha[1]) #opcao
    #     # dados.append(linha[2]) # nome
    #     # dados.append(linha[3]) # email
    #     # dados.append(linha[4]) #cidade
            
for i in dados:
    if i[1] == 'Criar':
        if not exist(i[1]):
            print(f'criar usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
            cadastro.criar(nome= i[2], email= i[3], cidade=[4])
        print('')
    elif i[1] == 'Alterar':
        print(f'Alterar usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
        cadastro.alter_dados(nome=i[2], email=i[3], Cidade=i[4])
        print('')
    elif i[1] == 'Excluir':
        print(f' Excluir usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
        cadastro.Deletar(email=i[3])