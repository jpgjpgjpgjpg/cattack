#!/usr/bin/env python3
import requests
import random
import time
from bs4 import BeautifulSoup

def generate_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.37',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.37',
        'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36 EdgA/46.6.2.5140',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Mozilla/5.0 (Android 11; Mobile; rv:89.0) Gecko/89.0 Firefox/89.0',
        'Mozilla/5.0 (Android 11; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0'
    ]
    accept_languages = [
        'en-US,en;q=0.5',
        'en-US,en;q=0.9,es;q=0.8',
        'en-US,en;q=0.8,fr;q=0.5',
        'pt-BR,pt;q=0.9,en;q=0.8',
        'ru-RU,ru;q=0.9,en;q=0.8',
        'fr-FR,fr;q=0.9,en;q=0.8',
        'de-DE,de;q=0.9,en;q=0.8',
    ]
    referers = [
        'https://developer.mozilla.org/testpage.html',
        'https://www.google.com/',
        'https://www.bing.com/',
        'https://www.yahoo.com/',
        'https://github.com/',
        'https://www.google.co.uk/',
        'https://www.google.com.br/',
        'https://search.yahoo.com/',
        'https://br.search.yahoo.com/',
        'https://www.bing.co.uk/',  
        'https://www.bing.com.br/',
    ]
    
    return {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': random.choice(accept_languages),
        'Connection': 'keep-alive',
        'Referer': random.choice(referers),
    }
    
def req(proxies,url):
    headers = generate_headers()
    proxy = random.choice(proxies)
    response = requests.get(url, proxies=proxy, headers=headers)
    return response, headers

def ua_response(proxies, url_ua):
    response, _ = req(proxies, url_ua)
    if response:
        print(f"Código de resposta: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
        ua_element = soup.find("textarea", {"id": "custom-ua-string"})
        ua = ua_element.text.strip()
        print(f'\nUser-Agent detectado: {ua}')
    
def ip_response(proxies, url_padrao):
    response, _ = req(proxies, url_padrao)
    if response:
        print(f'\nCódigo de resposta: {response.status_code}')
        print(f'IP detectado: {response.text}')

def main():

    url_ip = "http://httpbin.org/ip"  # Checar IP
    url_ua = "https://www.whatsmyua.info/"  # Checar UA

    proxies = [
        {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'},
        {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'},
        {'http': 'socks5h://127.0.0.1:9250', 'https': 'socks5h://127.0.0.1:9250'},
        {'http': 'socks5h://127.0.0.1:9350', 'https': 'socks5h://127.0.0.1:9350'},
        {'http': 'socks5h://127.0.0.1:9450', 'https': 'socks5h://127.0.0.1:9450'}
    ]

    print("Escolha a opção:")
    print("1 - Iniciar ataque")
    print("2 - Checagem")
    choice = input("Digite sua escolha (1 ou 2): ")

    if choice == '1':
        intervals = [2, 4, 5, 7,]
        num_requests = [1, 3, 5, 7, 10]

        url_padrao = input("Digte a URL desejada (Ex: https://google.com/): ")

        for interval, num_req in zip(intervals, num_requests):
            for _ in range(num_req):
                response, headers = req(proxies, url_padrao)
                print(f'\nURL da página: {response.url}')
                print(f'Código de resposta: {response.status_code}')
                print(f'User-Agent utilizado: {headers["User-Agent"]}')
                time.sleep(interval)

    elif choice == '2':
        print(f"\nEscolha a checagem:")
        print("1 - Checar IP")
        print("2 - Checar User-Agent")
        print("3 - Checar Headers")
        sub_choice = input("Digite sua escolha (1, 2 ou 3): ")

        if sub_choice == "1":
            print("Iniciando checagem de IP...")
            for _ in range(8):
                ip_response(proxies, url_ip)

        elif sub_choice == "2":
            print("Iniciando checagem de User-Agent...")
            for _ in range(5):
                ua_response(proxies, url_ua)
            
        elif sub_choice == "3":
            print("Iniciando checagem de Headers...")
            for _ in range(5):
                response, headers = req(proxies, url_ip)
                print(f'\nCódigo de resposta: {response.status_code}')
                print(f'Headers utilizados: {headers}')

main()
