import os
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

URL = "https://demoqa.com/automation-practice-form"

try:
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input").send_keys("John")
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[4]/input").send_keys("Doe")
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div[2]/input").send_keys("JohnDoe@gmail.com")
    except:
        print("Name and email input failed")

    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[1]/label").click()
    except:
        print("Gender picking failed")
    
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/input").send_keys("1234567890")
    except:
        print("email input failed")

    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[1]/div/input").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select"))
        ).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[5]"))
        ).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select"))
        ).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[97]"))
        ).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[7]"))
        ).click()
    except:
        print("Calendar picking failed")

    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[1]/label").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[3]/label").click()
    except:
        print("Hobby picking failed")

    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div[2]/div/div/div[1]/div[2]/div/input").send_keys("Maths")
        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div[2]/div/div[2]/div/div[2]").click()
            '''
            auto_complete = driver.find_elements(By.CLASS_NAME("subjects-auto-complete__option"))
            print("auto complete size: " + auto_complete.__len__)
            auto_complete[0].click()
            print(auto_complete[0].get_attribute("value"))
            '''
        except NoSuchElementException:
            print("no such element exception")
        except:
            print("different exception")
    except:
        print("Subject picking failed")

    
    
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[8]/div[2]/div/input").send_keys(os.getcwd()+"/fine.png")
    except:
        print("Failed to upload image")
    
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]/div[1]"))
        ).click()
        select = Select(driver.findElement(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div[1]/div[1]"))
        select.select_by_index(1)
    except:
        print("State and city selection failed")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[9]/div[2]/textarea").send_keys("A real address" + Keys.TAB + "NCR" + Keys.TAB + Keys.TAB + "Gurgaon" + Keys.TAB + Keys.TAB + Keys.ENTER)
    

    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[11]/div/button").click()
    except:
        print("Submit button click failed")
     
except:
    print("Connection error")
finally:
    input("input anything to end the test\n")
    print("Testing ended, closing driver")
    driver.close()
