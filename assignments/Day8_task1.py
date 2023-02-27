import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Edge()
driver.get("https://www.oracle.com/in/database/")
driver.maximize_window()
driver.implicitly_wait(30)
# to get entire script of current page
"""source=driver.page_source 
print(source)"""
driver.find_element(By.ID,"acctBtnLabel").click()
driver.find_element(By.LINK_TEXT,"Sign-In").click()
time.sleep(5)
print("Title is:",driver.title)
print("URL is:",driver.current_url)
actual_header=driver.find_element(By.XPATH,"//h2[contains(text(),'Oracle account')]").text
print("Header is:",actual_header)
driver.find_element(By.ID,"sso_username").send_keys("john")
driver.find_element(By.ID,"ssopassword").send_keys("john123")
driver.find_element(By.ID,"signin_button").click()
time.sleep(5)
errormsg=driver.find_element(By.XPATH,"//span[@id='errormsg']").text
print("ErrorMsg is:",errormsg)
time.sleep(5)
driver.quit()