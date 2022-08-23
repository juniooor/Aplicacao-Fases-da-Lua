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
        
        
            