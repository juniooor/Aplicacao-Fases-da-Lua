import requests, json

Token =  'ef660f491907bb9049a03d59868ea9d8'
cidade = str(input('digite o nome da cidade: '))
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={Token}&units=metric&lang=pt_br'

requisicao = requests.get(link)

requisicao_dict = requisicao.json()

description = requisicao_dict['weather'][0]['description']
temperatura = requisicao_dict['main']['temp']


print(description, f'{temperatura}°C' )