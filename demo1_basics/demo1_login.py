import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.ID,"email").send_keys("afzalit003@gmail.com")
driver.find_element(By.ID,"pass").send_keys("afzal003")
driver.find_element(By.NAME,"login").click()
time.sleep(5)
driver.quit()

