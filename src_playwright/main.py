from playwright.sync_api import sync_playwright, Page
from bs4 import BeautifulSoup
from math import ceil
from datetime import datetime
import json
import csv


class SearchPlaywright:
    def search_page_playwright(page:Page):
        try:
            
            region = input("Digite o país: ")
            
            with sync_playwright() as p:
                # Instânciamos o browser Utils.str_to_bool()
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("https://finance.yahoo.com/screener/new")
                page.wait_for_timeout(30000)
                
                current_time = datetime.now().strftime("%H:%M:%S")
                print(f"Iniciando funcionamento com Playwright. Horario: {current_time}")
                
                page.get_by_role("button", name="United States").click()
                page.get_by_role("button", name="Add Region").click()
                page.get_by_placeholder("Find filters").fill(region)
                page.wait_for_timeout(2000)
                page.locator("[data-test=\"itm-menu-cntr\"]").get_by_role("listitem").click()
                page.locator("#dropdown-menu > div > div.Pstart\(16px\).Pend\(20px\).Mah\(230px\).Ovy\(a\) > ul > li > label > input[type=checkbox]").click()
                page.wait_for_timeout(2000)
                page.locator("[data-test=\"find-stock\"]").click()

                # Aguarda o carregamento dos dados
                page.wait_for_selector('table.W\\(100\\%\\)', timeout=360000)

                # Extrai o número de resultados estimados
                html = page.content()
                soup = BeautifulSoup(html, 'html.parser')
                estimated_results = page.locator("#screener-criteria > div.Pos\(r\).Pt\(16px\).Pb\(20px\).Bd.Bdc\(\$seperatorColor\).W\(100\%\).Bgc\(\$headerBgColor\).Bdrs\(3px\) > div.Mstart\(22px\).Pend\(25px\).Mstart\(10px\)--mobp.Pend\(10px\)--mobp.Mstart\(10px\)--mobl.Pend\(10px\)--mobl > div.Fl\(start\).D\(ib\).D\(n\)--tab768.Mstart\(6\%\)--scrm.Mstart\(2\.2\%\)--scrl.Mb\(20px\)--mobp.Mb\(20px\)--mobl > div > div.Mt\(5px\) > div").inner_html()
                estimated_results_number = int(estimated_results)
                num_pages = ceil(estimated_results_number / 25)

                try:
                # Extrai os dados de todas as páginas
                    dados = []
                    for page_num in range(num_pages):
                        if page_num > 0:
                            if page.locator('#scr-res-table > div.W\(100\%\).Mt\(15px\).Ta\(end\) > button.Va\(m\).H\(20px\).Bd\(0\).M\(0\).P\(0\).Fz\(s\).Pstart\(10px\).O\(n\)\:f.Fw\(500\).C\(\$linkColor\) > span').is_visible():
                                page.locator("#scr-res-table > div.W\(100\%\).Mt\(15px\).Ta\(end\) > button.Va\(m\).H\(20px\).Bd\(0\).M\(0\).P\(0\).Fz\(s\).Pstart\(10px\).O\(n\)\:f.Fw\(500\).C\(\$linkColor\) > span").click()
                                page_num+1
                            else:
                                raise Exception

                        # Aguarda o carregamento dos dados
                        page.wait_for_selector('table.W\\(100\\%\\)', timeout=30000)

                        # Extrai os dados da tabela
                        html = page.content()
                        soup = BeautifulSoup(html, 'html.parser')
                        tabela = soup.find('table', {'class': 'W(100%)'})
                        for tr in tabela.find_all('tr')[1:]:
                            dados.append({
                                'name': tr.find('td', {'aria-label': 'Name'}).text.strip(),
                                'symbol': tr.find('td', {'aria-label': 'Symbol'}).text.strip(),
                                'price (intraday)': tr.find('td', {'aria-label': 'Price (Intraday)'}).text.strip()
                            })
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
                except:
                    
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
            print(f'Não foi possível acessar o site! {err}')

init = SearchPlaywright
init.search_page_playwright(page=Page)
