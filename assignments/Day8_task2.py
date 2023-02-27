import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.medibuddy.in/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[contains(text(),'I have a Corporate Account')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[contains(text(),'Login using Username & Password')]").click()
driver.find_element(By.NAME,"userName").send_keys("john")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("john123")
driver.find_element(By.XPATH,"//input[@ng-model='showMBLoginPassword']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
errormsg=driver.find_element(By.XPATH,"//div[contains(text(),'You have entered incorrect password.')]").text
print("ErrorMsg is:",errormsg)
time.sleep(5)
driver.quit()