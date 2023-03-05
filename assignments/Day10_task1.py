import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
time.sleep(5)
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//i[@id='i-icon-profile']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//li[@id='signInLink']").click()
time.sleep(5)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='mobileNoInp']").send_keys("7898")
Msg=driver.find_element(By.XPATH,"//span[contains(text(),'Please enter valid mobile number')]").text
print(Msg)
driver.switch_to.default_content()
time.sleep(5)
driver.quit()