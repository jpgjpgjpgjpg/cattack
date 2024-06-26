# CATATTACK
Ainda em desenvolvimento e contém alguns erros conhecidos.

Este código usa Selenium para automatizar a interação com um navegador, permitindo abrir páginas da web e analisá-las. O BeautifulSoup auxilia nessa análise, extraindo elementos como inputs e botões do conteúdo HTML.

Há uma função para testar APIs, medindo a resposta HTTP e o tempo de resposta para uma URL específica. A paralelização com threading permite testar várias APIs ao mesmo tempo, aumentando a eficiência do código.

Além disso, o código contém uma função para testar SQL Injection, utilizando uma wordlist que contém várias tentativas de injeção. A wordlist é lida de um arquivo, e cada entrada é inserida em um input, seguida de um clique no botão de envio. O código coleta os resultados dessas tentativas para posterior análise.

Com esse conjunto de funcionalidades, o código é útil para testar e analisar páginas da web, APIs, e explorar potenciais vulnerabilidades de segurança por meio de SQL Injection.

O código também inclui uma função para ofuscar o IP ao fazer requisições usando proxies, o que pode ser útil para evitar bloqueios ou monitoramento.

# SCREENSHOTS

![image](https://github.com/jpgjpgjpgjpg/cattack/assets/163206473/48ba4d23-f6ab-4045-8a8c-0150364e0c9d)

# COMO INSTALAR

Instale a versão mais recente do webdriver neste link:
`https://googlechromelabs.github.io/chrome-for-testing/`

Instale os requerimentos para a ferramenta:
`pip install -r requirements.txt`

`git clone https://github.com/jpgjpgjpgjpg/cattack`

# COMO USAR
Para iniciar a ferramenta utilize o python3:
`python3 cattack.py`
