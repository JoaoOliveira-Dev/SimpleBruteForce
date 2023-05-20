import requests
from bs4 import BeautifulSoup
import re

url_teste = "https://www.gtfoods.com.br/wp-login.php"

def get(url):
    r = requests.get(url)
    return r

def post(url, data):
    # Se quiser que esteja no body da requisição, precisa ser um json
    # Se quiser que esteja na url como um parâmetro, precisar usar o params
    # data é igual a qualquer coisa
    r = requests.post(url, data=data)
    soup = BeautifulSoup(r.content, 'html.parser')
    div_login_error = soup.find("div", id="login_error")
    if div_login_error:
        content = div_login_error.get_text()
        print("Erro de login:", content)

    return r

def get_params(url, params):
    r = requests.get(url, params=params)
    return r

response = post(url_teste, {"log": "gtfoods", "pwd": "asdas", "wp-submit": "Acessar", "redirect_to": "https://www.gtfoods.com.br/wp-admin/", "testcookie": "1"})
