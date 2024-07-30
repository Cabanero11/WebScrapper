import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CabaneroSearch(unittest.TestCase):

    def setUp(self):
        edge_options = Options()
        edge_options.add_argument("--start-maximized")
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

    def search_products(self, query):
        driver = self.driver
        driver.get('https://cabanero.es/')
        
        logging.info("Página cargada, buscando el elemento de búsqueda")

        # Espera explícita para asegurar que el campo de búsqueda esté disponible
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 's')))
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        logging.info(f"Búsqueda de '{query}' iniciada")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article.product-miniature')))

    def scrape_page(self, driver):
        products = driver.find_elements(By.CSS_SELECTOR, 'article.product-miniature')
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
                logging.warning(f"Error al procesar un producto: {e}")

        return resultados

    def scrape_all_pages(self, query):
        self.search_products(query)
        all_results = []

        while True:
            results = self.scrape_page(self.driver)
            all_results.extend(results)

            try:
                next_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.next.js-search-link'))
                )
                logging.info("Clic en el botón 'Siguiente' para cargar más productos")
                self.driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()

                WebDriverWait(self.driver, 10).until(
                    EC.staleness_of(next_button)  # Esperar hasta que el botón 'Siguiente' se vuelva obsoleto
                )
            except Exception as e:
                logging.info(f"No más páginas o error: {e}")
                break

        return all_results

    def save_results_to_json(self, results, filename='resultados-cabanero.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        logging.info(f"Datos guardados en '{filename}'")

    def test_cabanero(self):
        query = ('Tornillo').lower()
        results = self.scrape_all_pages(query)
        self.save_results_to_json(results)

    def tearDown(self):
        self.driver.quit()
        logging.info("Scraper terminado y navegador cerrado")

if __name__ == "__main__":
    unittest.main()
    logging.info('Scraping terminado !!!!')
