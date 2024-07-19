
# -*- coding: utf-8 -*-
import requests
import random
import time

def req(url, proxies):
    user_agents = [
    # Chrome on Windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    # Chrome on macOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    # Chrome on Linux
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    # Chrome on Android
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',

    # Edge on Windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.37',
    # Edge on macOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.37',
    # Edge on Android
    'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36 EdgA/46.6.2.5140',

    # Firefox on Windows
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    # Firefox on macOS
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
    # Firefox on Linux
    'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
    # Firefox on Android
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

    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': random.choice(accept_languages),
        'Connection': 'keep-alive',
        'Referer': random.choice(referers),
    }
    
    proxy = random.choice(proxies)

    response = requests.get(url, headers=headers, proxies=proxy)
    print(f'Código de resposta para {url}: {response.status_code}')
    print(response.text)

def main():
    url = "http://httpbin.org/ip"
    #url = "https://prostactive.online/"

    proxies = [
        {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'},
        {'http': 'socks5h://127.0.0.1:9150', 'https': 'socks5h://127.0.0.1:9150'},
        {'http': 'socks5h://127.0.0.1:9250', 'https': 'socks5h://127.0.0.1:9250'},
        {'http': 'socks5h://127.0.0.1:9350', 'https': 'socks5h://127.0.0.1:9350'},
        {'http': 'socks5h://127.0.0.1:9450', 'https': 'socks5h://127.0.0.1:9450'}
    ]

    intervals = [2,4,5,7]
    num_requests = [1, 3, 5, 7, 10]

    for interval, num_req in zip(intervals, num_requests):
        for _ in range(num_req):
            req(url, proxies)
        time.sleep(interval)


main()
