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

print("Find: ")
print(input)
print(search)
search.send_keys("Pina", Keys.RETURN)
time.sleep(5)
search.clear()
search.send_keys("Ibura", Keys.RETURN)


card = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="cellTableViewdemoChart2"]/tbody')))
print("card")
print(card)

disponibility = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'jqx-tooltip-text')))

print(disponibility[0].get_attribute('textContent'))

for e in disponibility:
    print(str(i) + ":")
    i+= 1
    print(e.get_attribute('textContent'))

print("End")
time.sleep(20)

browser.quit()