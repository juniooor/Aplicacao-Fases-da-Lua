import opcrud as op
import pandas as pd

tabela = pd.read_csv("infos_contato.csv", sep=',', encoding= "utf-8")

for dados in tabela:
    print(dados)    

    
# try:
#     cadastro = op.Cadastrar()
#     cadastro.criar(nome='Vania', email="jvaniacosta@hotmail.com")
# except:
#     print('ALÔ KLEITINHO A CASA CAIU')

# finally:
#     print('positivo e operante')

# print(tabela["Opção desejada"][0])
