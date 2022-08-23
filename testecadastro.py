import dadosbd


dados = dadosbd.linhas


email = 'juniormodern@hotmail.com'


for i in dados:
    if i[2] == email:
        print('Tô aqui painho')
    else:
        print(i)