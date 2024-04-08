from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

URL = "https://jsms-pokedex-with-pokeapi.netlify.app"

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()

    #grass type
    driver.find_element(By.XPATH, "/html/body/header/nav/ul/li[5]/button").click()
    time.sleep(5)
    #flying type
    driver.find_element(By.XPATH, "/html/body/header/nav/ul/li[11]/button").click()
    time.sleep(5)
    #fighting tipe
    driver.find_element(By.XPATH, "/html/body/header/nav/ul/li[8]/button").click()

except:
    print("Connection error")
finally:
    input("Tests ended")
    driver.close()