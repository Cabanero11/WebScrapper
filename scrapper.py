import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    


    def tearDown(self):
        self.driver.close()

def backmarket():

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://www.backmarket.es',
            'Referer': 'https://www.backmarket.es/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-algolia-api-key': 'YzIzODlkOTJkZTk2NWI2NjA1NTUzNGY3ZTFjMTViMTcxNGRjZTRmZGU5ODk4NDJlMDYzZDY1ZWJiNzMzNDRhZmF0dHJpYnV0ZXNUb1JldHJpZXZlPWJhY2tib3hfZ3JhZGVfbGFiZWwlMkNiYWNrYm94X2dyYWRlX3ZhbHVlJTJDYmFja21hcmtldElEJTJDYnJhbmQlMkNicmFuZF9jbGVhbiUyQ2NhdGVnb3J5XzElMkNjYXRlZ29yeV8yJTJDY2F0ZWdvcnlfMyUyQ2NvbG9yJTJDY3VycmVuY3klMkNpZCUyQ2ltYWdlMSUyQ2xpbmtfZ3JhZGVfdjIlMkNsaXN0X3ZpZXclMkNsaXN0aW5nSUQlMkNtZXJjaGFudF9pZCUyQ21vZGVsJTJDbW9kZWxfY2xlYW4lMkNvYmplY3RJRCUyQ3ByaWNlJTJDcHJpY2VfbmV3JTJDcHJpY2Vfd2l0aF9jdXJyZW5jeSUyQ3ByaWNlX25ld193aXRoX2N1cnJlbmN5JTJDcmVmZXJlbmNlUHJpY2UlMkNyZXZpZXdSYXRpbmclMkNzaW1fbG9jayUyQ3NwZWNpYWxfb2ZmZXJfdHlwZSUyQ3N0b2NrUmF3JTJDc3ViX3RpdGxlX2VsZW1lbnRzJTJDdGl0bGUlMkN0aXRsZV9tb2RlbCUyQ3ZhcmlhbnRfZmllbGRzJTJDd2FycmFudHkmZmlsdGVycz1OT1QrYmFja2JveF9ncmFkZV92YWx1ZSUzRDkmcmVzdHJpY3RJbmRpY2VzPXByb2RfJTJB',
            'x-algolia-application-id': '9X8ZUDUNN9',
        }

        data = '{"query":"XIAOMI REDMI","distinct":1,"clickAnalytics":true,"filters":"(special_offer_type=0 OR special_offer_type=1 OR special_offer_type=2 OR special_offer_type=3 OR special_offer_type=4 OR special_offer_type=5 OR special_offer_type=6 OR special_offer_type=7)","facets":["price","page","q","sort","brand","model","backbox_grade","storage","color","year_date_release","shipping_delay","payment_methods","warranty_with_unit","keyboard_type_language","price_ranges.sm-1","price_ranges.sm-2","price_ranges.md-1","price_ranges.md-1b","price_ranges.md-1c","price_ranges.md-2","price_ranges.lg-1","price_ranges.lg-2","price_ranges.lg-3"],"page":0,"hitsPerPage":30}'

        response = requests.post(
            'https://9x8zudunn9-dsn.algolia.net/1/indexes/prod_index_backbox_es-es/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.22.1)%3B%20Browser',
            headers=headers,
            data=data,
        )
        a=response.json()
        print(a)

if __name__ == "__main__":
    #unittest.main()
    backmarket()
    