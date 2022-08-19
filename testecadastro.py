import email
import opcrud as op
import pandas as pd

ddnome = [] # feito 
ddemail = []
ddcidade = []
ddopcao = []
tabela = pd.read_csv("infos_contato.csv", sep=',', encoding= "utf-8")

for n in tabela['Nome']:
    ddnome.append(n)
for e in tabela['E-mail']:
    ddemail.append(e)
for c in tabela['Cidade']:
    ddcidade.append(c)
for o in tabela['Opcao']:
    ddopcao.append(o)
    
tabela_cert = tabela.iloc[1:, 1:5]

 
    
 
# for o, n, e, c in zip(ddopcao,ddnome, ddemail, ddcidade ):
#     print(f'Opção- {o}, Nome - {n}, email - {e}, cidade - {c}')
   
    


    
# for i in dados:
#     if i[0] == 'Criar':
#         cadastro.criar(nome=i[1], email= i[2], cidade=i[3])









# try:
#     for 
#     cadastro = op.Cadastrar()
    
# except:
#     print('ALÔ KLEITINHO A CASA CAIU')

# finally:
#     print('positivo e operante')

