import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging

i = 0

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Info! ')

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options=options)

browser.get('https://servicos.compesa.com.br/calendario-de-abastecimento-da-compesa/')

actions = ActionChains(browser)

wait = WebDriverWait(browser, 30)

input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="advanced_iframe"]')))

browser.switch_to.frame(input)

search = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search_input"]')))
focus = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="map_gc"]')))

browser.execute_script("arguments[0].scrollIntoView();", focus)

search.send_keys("51240-490", Keys.RETURN) # 51220-230

#search.clear()

card = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cellTableViewdemoChart2"]/tbody')))

disponibility = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jqx-tooltip-text')))

#ACHOU!!!
elementsA = browser.find_elements(By.CLASS_NAME, 'intervensao-a')
elementsI = browser.find_elements(By.CLASS_NAME, 'intervensao')
#elementsV = browser.find_elements(By.CLASS_NAME, 'jqx-calendar-cell-month')
elementsD = browser.find_elements(By.CLASS_NAME, 'jqx-calendar-cell-specialDate')

elementsAll = elementsA + elementsI + elementsD # + elementsV

def get_text_content(element):
    text = element.get_attribute('textContent')
    try:
        return float(text)
    except ValueError:
        return float('inf')  # Definindo um valor infinito para tratar casos inválidos

elementsAllSorted = sorted(elementsAll, key=get_text_content)

for day, situation in zip(elementsAllSorted, disponibility):
    
    mensagem = " É dia de água "

    if ('linear-gradient' in day.value_of_css_property('background')):
        mensagem = " Chegará água parcialmente "    

    elif 'rgba(218, 41, 47, 0.5)' in day.value_of_css_property('background'):
        mensagem = " Não chegará água "
    
    print('Dia '+ str(day.get_attribute('textContent')) + mensagem + situation.get_attribute('textContent').lower())
    


print("End")
time.sleep(20)

browser.quit()