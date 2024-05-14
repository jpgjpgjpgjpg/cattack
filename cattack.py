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

pergunta = input("Deseja iniciar a busca? (sim/nao): ").lower()

if pergunta == "sim":
    # Pergunta ao usuário pelo URL alvo
    site_url = input("Por favor, insira o URL do site que deseja varrer: ")
    # Aqui você pode adicionar alguma validação para garantir que o URL seja válido
    
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

    driver.get(site_url)
    time.sleep(5)

    # Usar BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')

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
    button_elements = soup.find_all('button')
    box_elements = soup.find_all(class_='box')  # Elementos com a classe 'box'
    valores_omitir = ["1","0","","None","none","yes","no"]

    def varredura():
        for idx, input_element in enumerate(input_elements):
            value = input_element.get('value')  # Obtém o valor
           
            input_attributes = {}
            # Adiciona atributos apenas se eles existirem
            if input_element.get('id'):
                input_attributes['ID'] = input_element.get('id')
            if input_element.get('name'):
                input_attributes['NAME'] = input_element.get('name')
            if input_element.get('type'):
                input_attributes['TYPE'] = input_element.get('type')
            if input_element.get('placeholder'):
                input_attributes['placeholder'] = input_element.get('placeholder')
            
            if value is not None and value not in valores_omitir:
                input_attributes['value'] = value  # Só adiciona se não for indesejado

            print(f"Input {idx + 1}: {input_attributes}")
            
        for idx, button_element in enumerate(button_elements):
            button_text = button_element.get_text(strip=True)  # Pega o texto do botão
            if button_text and button_element != None:
                print(f"Botão {idx + 1}: {button_text}")     
                
    print("Dados coletados!\n\n")

    varredura()

    # Testar cada input encontrado para SQL Injection
    for input_element in input_elements:
        resultados = testar_sql_injection(input_element)
        for resultado in resultados:
            print(f"Palavra: {resultado[0]}, Resultado: {resultado[1]}")

    # Usar threads para paralelizar requisições GET para as APIs encontradas
    # Continuação do código anterior

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

elif pergunta == "nao":
    print("Programa encerrado.")
else:
    print("Opção inválida. Programa encerrado.")
