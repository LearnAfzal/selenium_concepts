from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from datetime import date
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://demo.openemr.io/b/openemr/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"authUser").send_keys("admin")
driver.find_element(By.ID,"clearPass").send_keys("pass")
# select_lang=Select(driver.find_element(By.NAME,"languageChoice")) -> By Name we cant abe to steer in webpage
select_lang=Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lang.select_by_value('18') # instead of single quote if we make use of double quote then it throws error
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.XPATH,"//div[contains(text(),'Patient')]").click()
driver.find_element(By.XPATH,"//div[contains(text(),'New/Search')]").click()
driver.switch_to.frame(driver.find_element(By.NAME,"pat"))
driver.find_element(By.XPATH,"//input[@name='form_fname']").send_keys("afzal")
driver.find_element(By.XPATH,"//input[@name='form_lname']").send_keys("khan")
driver.find_element(By.ID,"form_DOB")
currentdate=date.today()
print(currentdate)
# how to pass the variable in script for date
driver.execute_script("document.querySelector('#form_DOB').value='2023-03-05'")
select_gender=Select(driver.find_element(By.ID,"form_sex"))
select_gender.select_by_value('Male')
driver.find_element(By.ID,"create").click()
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.ID,"modalframe"))
driver.find_element(By.XPATH,"//input[@value='Confirm Create New Patient']").click()
driver.switch_to.default_content()

# Explicit wait is recommended

wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.alert_is_present())

alert_text=driver.switch_to.alert.text
print(alert_text)
driver.switch_to.alert.accept()
driver.find_element(By.XPATH,"//div[@data-dismiss='modal']").click()
patient_name=driver.find_element(By.XPATH,"//a[@class='ptName  ']").text
print(patient_name)
time.sleep(5)
driver.quit()