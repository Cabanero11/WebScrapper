import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import json
import time

# pip install webdriver_manager

class CabaneroSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    def search_products(self, query):
        driver = self.driver
        driver.get('https://cabanero.es/')
        driver.fullscreen_window() # Fullscreen que sino no busca xd
        
        time.sleep(5) # Esperar que inicie la pagina

        # Buscar el elemento de búsqueda y realizar la búsqueda
        search_box = driver.find_element(By.NAME, 's')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Esperar a que la página se cargue

        return driver
    

    def scrape_page(self, driver):
        products = driver.find_elements(By.CSS_SELECTOR, 'article.product-miniature')
        driver.fullscreen_window()
        resultados = []

        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, 'span.h3.product-title a').text
                price = product.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]').text
                description = product.find_element(By.CSS_SELECTOR, 'div.product-desc-short[itemprop="description"]').get_attribute('innerText')
                link = product.find_element(By.CSS_SELECTOR, 'span.h3.product-title a').get_attribute('href')

                resultados.append({
                    'Titulo': title,
                    'Descripcion': description,
                    'Precio': price,
                    'Enlace': link
                })
            except Exception as e:
                print(f"Error al procesar un producto: {e}")

        return resultados

    def scrape_all_pages(self, query):
        driver = self.search_products(query)
        all_results = []

        while True:
            results = self.scrape_page(driver)
            all_results.extend(results)

            try:
                next_button = driver.find_element(By.CSS_SELECTOR, 'a.next.js-search-link')
                # Desplazar hacia abajo xd
                driver.execute_script("arguments[0].scrollIntoView();", next_button)  

                time.sleep(1)  # Esperar un momento después de desplazar

                try:
                    next_button.click()
                except Exception:
                    # Usar JavaScript para hacer clic si el clic normal falla
                    driver.execute_script("arguments[0].click();", next_button)

                time.sleep(3)  # Esperar a que la siguiente página se cargue
            except Exception as e:
                print(f"No más páginas o error: {e}")
                break

        return all_results

    
    def save_results_to_json(self, results, filename='resultados-cabanero.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"Datos guardados en '{filename}'")

    def test_cabanero(self):
        query = 'tornillo'
        results = self.scrape_all_pages(query)
        self.save_results_to_json(results)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    print('Scrapping terminado !!!!')
