#!/usr/bin/env python3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random


def setup_webdriver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("window-size=1200,1200")
    navegador = webdriver.Chrome(service=service, options=options)
    navegador.get("http://testphp.vulnweb.com/login.php")
    sleep(3)
   # accept_cookies(navegador)
    interactions(navegador)

#def accept_cookies(navegador):
   # try:
      #  navegador.find_element(By.XPATH, "//button[contains(text(), 'OK')]").click()
   # except:
      #  print("Erro ao acessar o botão de Cookies!")

def carregar_wordlist(filepath):
    with open (filepath, 'r') as file:
        return [line.strip() for line in file]

def interactions(navegador):
    try:
        wordlist = carregar_wordlist("caminho/para/sua/wordlist")
        inputs = navegador.find_elements(By.TAG_NAME, "input")
        for input in inputs:
            #input.send_keys("admin' '1' or '1") Você pode escolher ou automatizar.
            #input.send_keys("<script>alert()</script>")
            word = random.choice(wordlist)
            input.send_keys(word)

            attributes_to_check = [
                input.get_attribute("placeholder"),
                input.get_attribute("id"),
                input.get_attribute("class"),
                input.get_attribute("name"),
                input.get_attribute("type")
            ]
            if any(attr and ("email" in attr or "e-mail" in attr) for attr in attributes_to_check):
                input.send_keys("exemplo" + "@gmail.com")
        
        sleep(4)
        input.submit()
        sleep(4)

    except Exception as error:
        print(f"Erro ao fazer busca! {error}")

    finally:
        print("Navegador Fechado!")
        sleep(4)
        navegador.quit()    

def main():
    setup_webdriver()

main()
