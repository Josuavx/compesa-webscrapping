import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

i = 0

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

search.send_keys("Jordão", Keys.RETURN)
time.sleep(5)
#search.clear()

card = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cellTableViewdemoChart2"]/tbody')))


disponibility = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jqx-tooltip-text')))

print("Numero: ")
print(len(disponibility))

for e in disponibility:
    print(str(i) + ":")
    i+= 1
    print(e.get_attribute('textContent'))

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

for i in elementsAllSorted:
    print(i.get_attribute('textContent'))
#    print(i.value_of_css_property('background'))

elemento = elementsAllSorted[8].get_attribute("innerHTML")
print(elemento)

print("End")
time.sleep(20)

browser.quit()