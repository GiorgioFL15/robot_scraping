from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from math import ceil
from datetime import datetime
import json
import csv
import time

class SearchSelenium:
    def search_page_selenium():
        try:
            
            region = input("Digite o país: ")
            
            driver = webdriver.Chrome()
            driver.get("https://finance.yahoo.com/screener/new")
            
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Iniciando funcionamento com Selenium. Horario: {current_time}")
            
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#screener-criteria > div.Pos\(r\).Pt\(16px\).Pb\(20px\).Bd.Bdc\(\$seperatorColor\).W\(100\%\).Bgc\(\$headerBgColor\).Bdrs\(3px\) > div.Mstart\(22px\).Pend\(25px\).Mstart\(10px\)--mobp.Pend\(10px\)--mobp.Mstart\(10px\)--mobl.Pend\(10px\)--mobl > div.D\(ib\).Fl\(start\).Mt\(10px\) > div:nth-child(1) > div > div.D\(ib\).W\(100\%\)--mobp.W\(100\%\)--mobl.W\(560px\)--scrm.W\(510px\)--scrl.W\(428px\)\!--tab768 > ul > li.Bgc\(\$hoverBgColor\).Mend\(5px\).D\(ib\).Bdrs\(3px\).filterItem.Mb\(3px\) > button > svg > path")))
            driver.find_element(By.CSS_SELECTOR, "#screener-criteria > div.Pos\(r\).Pt\(16px\).Pb\(20px\).Bd.Bdc\(\$seperatorColor\).W\(100\%\).Bgc\(\$headerBgColor\).Bdrs\(3px\) > div.Mstart\(22px\).Pend\(25px\).Mstart\(10px\)--mobp.Pend\(10px\)--mobp.Mstart\(10px\)--mobl.Pend\(10px\)--mobl > div.D\(ib\).Fl\(start\).Mt\(10px\) > div:nth-child(1) > div > div.D\(ib\).W\(100\%\)--mobp.W\(100\%\)--mobl.W\(560px\)--scrm.W\(510px\)--scrl.W\(428px\)\!--tab768 > ul > li.Bgc\(\$hoverBgColor\).Mend\(5px\).D\(ib\).Bdrs\(3px\).filterItem.Mb\(3px\) > button > svg > path").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#screener-criteria > div.Pos\(r\).Pt\(16px\).Pb\(20px\).Bd.Bdc\(\$seperatorColor\).W\(100\%\).Bgc\(\$headerBgColor\).Bdrs\(3px\) > div.Mstart\(22px\).Pend\(25px\).Mstart\(10px\)--mobp.Pend\(10px\)--mobp.Mstart\(10px\)--mobl.Pend\(10px\)--mobl > div.D\(ib\).Fl\(start\).Mt\(10px\) > div:nth-child(1) > div > div.D\(ib\).W\(100\%\)--mobp.W\(100\%\)--mobl.W\(560px\)--scrm.W\(510px\)--scrl.W\(428px\)\!--tab768 > ul > li > div > div").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#dropdown-menu > div > div.Mb\(16px\).Mstart\(16px\) > div > input").send_keys(region)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "#dropdown-menu > div > div.Pstart\(16px\).Pend\(20px\).Mah\(230px\).Ovy\(a\) > ul > li > label > input[type=checkbox]").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "#screener-criteria > div.Pos\(r\).Pt\(16px\).Pb\(20px\).Bd.Bdc\(\$seperatorColor\).W\(100\%\).Bgc\(\$headerBgColor\).Bdrs\(3px\) > div.Mstart\(22px\).Pend\(25px\).Mstart\(10px\)--mobp.Pend\(10px\)--mobp.Mstart\(10px\)--mobl.Pend\(10px\)--mobl > div.Mt\(20px\).Cl\(b\) > button.Bgc\(\$linkColor\).C\(white\).Fw\(500\).Px\(20px\).Py\(9px\).Bdrs\(3px\).Bd\(0\).Fz\(s\).D\(ib\).Whs\(nw\).Miw\(110px\).Bgc\(\$linkActiveColor\)\:h").click()

            # Aguarda o carregamento dos dados
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.W\\(100\\%\\)")))

            # Extrai o número de resultados estimados
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            estimated_results = driver.find_element(By.CSS_SELECTOR, "#screener-criteria > div.Pos\(r\).Pt\(16px\).Pb\(20px\).Bd.Bdc\(\$seperatorColor\).W\(100\%\).Bgc\(\$headerBgColor\).Bdrs\(3px\) > div.Mstart\(22px\).Pend\(25px\).Mstart\(10px\)--mobp.Pend\(10px\)--mobp.Mstart\(10px\)--mobl.Pend\(10px\)--mobl > div.Fl\(start\).D\(ib\).D\(n\)--tab768.Mstart\(6\%\)--scrm.Mstart\(2\.2\%\)--scrl.Mb\(20px\)--mobp.Mb\(20px\)--mobl > div > div.Mt\(5px\) > div").text
            estimated_results_number = int(estimated_results)
            num_pages = ceil(estimated_results_number / 25)

            # Extrai os dados de todas as páginas
            try:
                dados = []
                for page_num in range(num_pages):
                    if page_num > 0:
                        print("passei1")
                        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#scr-res-table > div.W\(100\%\).Mt\(15px\).Ta\(end\) > button.Va\(m\).H\(20px\).Bd\(0\).M\(0\).P\(0\).Fz\(s\).Pstart\(10px\).O\(n\)\:f.Fw\(500\).C\(\$linkColor\)")))
                        print("passei2")
                        time.sleep(1)
                        print("passei3")
                        driver.find_element(By.CSS_SELECTOR, "#scr-res-table > div.W\(100\%\).Mt\(15px\).Ta\(end\) > button.Va\(m\).H\(20px\).Bd\(0\).M\(0\).P\(0\).Fz\(s\).Pstart\(10px\).O\(n\)\:f.Fw\(500\).C\(\$linkColor\)").click()
                        print("passei4")
                        page_num+1

                    print("passei5")
                    # Aguarda o carregamento dos dados
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.W\\(100\\%\\)")))

                    # Extrai os dados da tabela
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    tabela = soup.find('table', {'class': 'W(100%)'})
                    for tr in tabela.find_all('tr')[1:]:
                        dados.append({
                            'name': tr.find('td', {'aria-label': 'Name'}).text.strip(),
                            'symbol': tr.find('td', {'aria-label': 'Symbol'}).text.strip(),
                            'price (intraday)': tr.find('td', {'aria-label': 'Price (Intraday)'}).text.strip()
                        })

                    # Grava os dados em um arquivo JSON
                    with open('dados_selenium.json', 'w') as f:
                        json.dump(dados, f)

                    # Salva os dados em um arquivo CSV
                    with open('dados_selenium.csv', 'w', newline='', encoding="utf-8") as f:
                        writer = csv.writer(f, delimiter=';')
                        writer.writerow(['Name', 'Symbol', 'Price (Intraday)'])
                        for d in dados:
                            writer.writerow([d['name'], d['symbol'], d['price (intraday)']])
                        
                end_time = datetime.now().strftime("%H:%M:%S")
                print(f"Finalizando funcionamento com Selenium. Horario: {end_time}")
            except Exception as err:
                print("Não foi possível carregar mais dados.")
                
                # Grava os dados em um arquivo JSON
                with open('dados_playwright.json', 'w') as f:
                    json.dump(dados, f)

                # Salva os dados em um arquivo CSV
                with open('dados_playwright.csv', 'w', newline='', encoding="utf-8") as f:
                    writer = csv.writer(f, delimiter=';')
                    writer.writerow(['Name', 'Symbol', 'Price (Intraday)'])
                    for d in dados:
                        writer.writerow([d['name'], d['symbol'], d['price (intraday)']])

                end_time = datetime.now().strftime("%H:%M:%S")
                print(f"Finalizando funcionamento com Playwright. Horario: {end_time}")
        except Exception as err:
            print(f"Página não encontrada {err}")

inicia = SearchSelenium
inicia.search_page_selenium()
