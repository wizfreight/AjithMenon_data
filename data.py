import csv
import itertools

import pandas as pd
from openpyxl.reader.excel import load_workbook
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import openpyxl
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 3})
chromeOptions.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--allow-running-insecure-content")
chromeOptions.add_argument("--disable-webgl")
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--remote-debugging-port=9222")
chromeOptions.add_argument("--window-size=1920,1080")
chromeOptions.add_argument("--proxy-server='direct://'")
chromeOptions.add_argument("--proxy-bypass-list=*")
s = Service(r'C:\Users\Bindu\PycharmProjects\big_schedules\chromedriver.exe')

url = 'https://agriexchange.apeda.gov.in/logistic/Freight_Forwarders.aspx?letter=i'
def getDriver():
    driver = webdriver.Chrome(service=s, options=chromeOptions)
# inputFile = r"C:\Users\Bindu\Desktop\freight_forward_Randeep's _Data.xlsx"
def task1():
    driver = getDriver()
    driver.get("https://app.volza.com/workspace/search/9441452")


row_group = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="dgpro"]/tbody')))
time.sleep(0.2)
with open('mango.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',', skipinitialspace=True)
    # wr.writerow(header)
    for row in row_group.find_elements(By.CSS_SELECTOR, 'tr'):
        wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])
    print(f"Processing page ..")
    time.sleep(4)
    print('complted')
