# CATATTACK

Este código usa Selenium para automatizar a interação com um navegador, permitindo abrir páginas da web e analisá-las. O BeautifulSoup auxilia nessa análise, extraindo elementos como inputs e botões do conteúdo HTML.

Há uma função para testar APIs, medindo a resposta HTTP e o tempo de resposta para uma URL específica. A paralelização com threading permite testar várias APIs ao mesmo tempo, aumentando a eficiência do código.

Além disso, o código contém uma função para testar SQL Injection, utilizando uma wordlist que contém várias tentativas de injeção. A wordlist é lida de um arquivo, e cada entrada é inserida em um input, seguida de um clique no botão de envio. O código coleta os resultados dessas tentativas para posterior análise.

Com esse conjunto de funcionalidades, o código é útil para testar e analisar páginas da web, APIs, e explorar potenciais vulnerabilidades de segurança por meio de SQL Injection.

O código também inclui uma função para ofuscar o IP ao fazer requisições usando proxies, o que pode ser útil para evitar bloqueios ou monitoramento.

#SCREENSHOTS

![image](https://github.com/jpgjpgjpgjpg/cattack/assets/163206473/206b8e1c-af30-4412-987e-ef75a2926fa3)

![cattack](https://github.com/jpgjpgjpgjpg/cattack/assets/163206473/82d71225-dc51-49ca-b8c5-3776d6637b06)

#COMO INSTALAR

`git clone https://github.com/jpgjpgjpgjpg/cattack`

#COMO USAR

`python3 cattack.py`
