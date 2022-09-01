import csv, opcrud, dadosbd  
import itertools


linhasbd = dadosbd.linhas
#cadastro = função para cadastrar cada dado do CSV que vem do fomulário
cadastro = opcrud.Cadastrar()

dados = []
with open ('info_contato.csv', 'r', encoding='utf-8') as arquivo_csv:
    tabela = csv.reader(arquivo_csv)
    next(tabela)
    
    for a in tabela:
        dados.append(a)
        
                    
for i in dados:
    if i[1] == 'Criar':
      for d, b in itertools.zip_longest(dados, linhasbd,fillvalue='none'):
        if d[3] != b[2]:
            cadastro.criar(nome= i[2], email= i[3], cidade= i[4])
            print(f'criar usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')    
        else:
            print(f'são IGUAIS dadosCSV: {d[3]} e BDsql: {b[2]} \n ')  
    elif i[1] == 'Alterar':
        print(f'Alterar usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
        cadastro.alterar_dados(nome=i[2], email=i[3], cidade=i[4])
            
    elif i[1] == 'Excluir':
        print(f' Excluir usuario: {i[2]}\n com email: {i[3]} \n cidade: {i[4]} ')
        cadastro.deletar(email=i[3])
