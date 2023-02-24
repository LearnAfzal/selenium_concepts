from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.db4free.net/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[@href='/phpMyAdmin']").click() #if there is any special character mostly go with contain or partial lnk text
title=driver.title
url=driver.current_url
print(title) # even the browser navigates to new tab in GUi but the script still remain in 1st tab itself
print(url)
driver.window_handles[1] # it will get the session id of tab, it works based on inde
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"input_username").send_keys("afzal")
driver.find_element(By.ID,"input_password").send_keys("welcome1234")
driver.find_element(By.ID,"input_go").click()
time.sleep(5)
driver.close() # closes the current tab
driver.quit() # kills the entire browser