from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import csv
import os

tickersymbol = str(input("Enter Your Company as a TickerSymbol"))
dayammount = int(input("How many days worth of data do you need"))

options = webdriver.FirefoxOptions()
options.add_argument("--headless=new")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

url = (f'https://www.nasdaq.com/market-activity/stocks/{tickersymbol}/historical?page=1&rows_per_page={dayammount}&timeline=y5')
driver.set_window_size(1800, 1020)

driver.get(url)

table_XPath = '//*[@class="historical-table-container"]/table/tbody/'
num_rows = len(driver.find_elements(By.XPATH, table_XPath + 'tr')) + 1
num_cols = len(driver.find_elements(By.XPATH, table_XPath + 'tr[1]/td'))

stringelement = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[2]/article/div/div[2]/div/div[2]/div[1]/div[1]/div[3]/div/div[1]/div[2]").text
element = stringelement.replace(',','').replace(' ',',').replace('$','')

if os.stat('stocks.csv').st_size == 0:
    with open('stocks.csv', 'a') as file:
        file.write(f'{element}')
        
else:
    clear = open('stocks.csv', 'w')
    clear.truncate()
    clear.close()
    with open('stocks.csv', 'a') as file:
        file.write(f'{element}')
        
driver.quit()
