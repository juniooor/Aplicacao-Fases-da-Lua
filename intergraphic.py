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
import dadosbd

linhasbd = dadosbd.linhas

# e = opcrud.exist
cadastro = opcrud.Cadastrar()
dados = []
with open ('info_contato.csv', 'r', encoding='utf-8') as arquivo_csv:
    tabela = csv.reader(arquivo_csv)
    next(tabela)
    
    for a in tabela:
        dados.append(a)
        

        
            
for i in dados:
    if i[1] == 'Criar':
        # for l in linhasbd:
        #     if l[2] == i[3]:
        #         print(f'ja foi cadastrado: {l[2]} == {i[3]}')
        #     else:
        #         print(f'VOU CADASTRAR: {l[2]} != {i[3]}')
        #         # print(f'criar usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')    
        cadastro.criar(nome= i[2], email= i[3], cidade= i[4])
    elif i[1] == 'Alterar':
        print(f'Alterar usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
        cadastro.alter_dados(nome=i[2], email=i[3], Cidade=i[4])
        print('')
    elif i[1] == 'Excluir':
        print(f' Excluir usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
        cadastro.Deletar(email=i[3])
