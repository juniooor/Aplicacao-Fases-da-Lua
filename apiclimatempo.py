from re import T
import requests, json

Token =  '338d8994a19bd99f4cdb5e4c735ac97d'
TypeConsult = 1

if TypeConsult == 1:
    city = input("Digite o nome da cidade: ")
    url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + city + "&token=" + Token
    response = requests.request("GET",url)
    return_response = json.loads(response.text)
    print(return_response)