# robot_scraping

# Instalação de dependencias

Crie uma .venv:

- python3 -m venv .venv
- source .venv/bin/activate

Instale as dependencias

- pip install -r requirements.txt

# Sobre

Foram desenvolvidos dois robôs:

Na pasta src_selenium existe o robô com a biblioteca selenium

- Para iniciar o Robô basta entrar no arquivo main.py e clicar F5 que iniciará com DEBUG
- Uma input irá aparecer no seu terminal pedindo para definir a region desejada, lembre de colocar em inglês
- Ex: Brazil ou United States

Na pasta src_playwright existe o robô com a biblioteca playwright

- Para iniciar o Robô basta entrar no arquivo main.py e clicar F5 que iniciará com DEBUG
- Uma input irá aparecer no seu terminal pedindo para definir a region desejada, lembre de colocar em inglês
- Ex: Brazil ou United States

Como domino mais a biblioteca playwright preferi criar primeiramente com ela para depois
criar um em selenium.
Inseri um horário de inicio e fim em cada robo para ser testado a velocidade dos dois e definir qual faria
o processamento mais rápido.
Os dois foram criados com a mesma estrutura apenas alterando a biblioteca e algumas esperas de tempo.
