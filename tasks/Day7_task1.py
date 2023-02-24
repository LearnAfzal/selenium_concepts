import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://github.com/login")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.ID,"login_field").send_keys("afzalit003@gmail.com")
driver.find_element(By.ID,"password").send_keys("afzal003")
driver.find_element(By.NAME,"commit").click()
time.sleep(5)
driver.quit()