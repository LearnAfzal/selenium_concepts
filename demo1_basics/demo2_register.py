import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
#time.sleep(5)
driver.find_element(By.NAME,"firstname").send_keys("Afzal")
driver.find_element(By.NAME,"lastname").send_keys("I")
driver.find_element(By.ID,"password_step_input").send_keys("Welcome123")
driver.find_element(By.XPATH,"//input[@value='-1']").click()
driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)