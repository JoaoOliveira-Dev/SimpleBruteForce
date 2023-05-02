import requests

url_teste = "http://127.0.0.1:3001/api/login"

def get(url):
    r = requests.get(url)
    return r

def post(url, data):
    # Se quiser que esteja no body da requisição, precisa ser um json
    # Se quiser que esteja na url como um parâmetro, precisar usar o params
    # data é igual a qualquer coisa
    r = requests.post(url, json=data)
    return r

def get_params(url, params):
    r = requests.get(url, params=params)
    return r

response = post(url_teste, {"user": "Admin", "password": "1234"})

print("respose text " + response.text)
print(response.json())