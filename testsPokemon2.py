from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

URL = "https://curious-beijinho-ac8e5d.netlify.app/more"

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    
    selection_input = Select(driver.find_element(By.XPATH, "/html/body/section/form/select"))
    selection_input.select_by_value("50")
    time.sleep(10)
    pokemon_cards = driver.find_elements(By.CLASS_NAME, "pokemon__card")
    for element in pokemon_cards:
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()
        time.sleep(3)

except:
    print("Connection error")
finally:
    input("Tests ended")
    driver.close()