#encoding: utf-8
import csv

nomes_cadastro = []
opcadastro = []
emails_cadastro = []
cidades_cadastro = []
with open("infos_contato.csv", "r", encoding="utf-8") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter= ",")
    for linha in arquivo_csv:
        #linha 1 -  OPÇÃO
        #linha 2 - NOMES
        #linha 3 - Emails
        #linha 4 - Cidade
        print(linha[2])
print(dados)