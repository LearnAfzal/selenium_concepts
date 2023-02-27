import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//img[@alt='Go']").click()
alert_text=driver.switch_to.alert.text
print(alert_text)
driver.switch_to.alert.accept()
time.sleep(5)