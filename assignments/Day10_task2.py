import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://phptravels.net/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[text()='flights']").click()
time.sleep(5)
driver.find_element(By.ID,"autocomplete").send_keys("LAX")
action=webdriver.ActionChains(driver)
action.send_keys(webdriver.Keys.ARROW_DOWN).pause(2).send_keys(webdriver.Keys.ENTER).perform()
driver.find_element(By.ID,"autocomplete2").send_keys("DAL")
action.send_keys(webdriver.Keys.ARROW_DOWN).pause(2).send_keys(webdriver.Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@id='departure']").clear()
driver.find_element(By.XPATH,"//input[@id='departure']").send_keys("30-05-2023")
driver.find_element(By.XPATH,"//a[@data-toggle='dropdown']").click()
# using sendkeys
"""driver.find_element(By.ID,"fadults").clear()
driver.find_element(By.ID,"fadults").send_keys("2")
action.send_keys(webdriver.Keys.ENTER).perform()"""
driver.find_element(By.XPATH,"//i[contains(@class,'la la-plus')]").click()
time.sleep(5)
driver.find_element(By.ID,"flights-search").click()
time.sleep(5)
driver.quit()