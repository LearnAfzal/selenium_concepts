import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.online.citibank.co.in/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[@title='Close']").click()
driver.find_element(By.XPATH,"//a[@title='Login']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//div[@onclick='ForgotUserID();']").click()
driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()
driver.find_element(By.ID,"citiCard1").send_keys("4545")
driver.find_element(By.ID,"citiCard2").send_keys("5656")
driver.find_element(By.ID,"citiCard3").send_keys("8887")
driver.find_element(By.ID,"citiCard4").send_keys("9998")
driver.find_element(By.ID,"cvvnumber").send_keys("123")

# javascript using css selector to inject date directly - approach 1
"""driver.execute_script("document.querySelector('#bill-date-long').value='14/04/2022'")"""

# javascript using arguments - approach 2
ele1=driver.find_element(By.NAME,"DOB")
driver.execute_script("arguments[0].value='14/04/2022'",ele1)
time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='button']").click()
time.sleep(5)
Text=driver.find_element(By.XPATH,"//li[contains(text(),'Please accept Terms and Conditions ')]").text
print(Text)
time.sleep(5)
driver.quit()