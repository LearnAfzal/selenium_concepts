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
driver.find_element(By.NAME,"DOB").click()
#driver.find_element(By.ID,"agree").click()
select_year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']")).select_by_value("2022")
select_month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']")).select_by_value("3")
driver.find_element(By.LINK_TEXT,"14").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='button']").click()
time.sleep(5)
Text=driver.find_element(By.XPATH,"//li[contains(text(),'Please accept Terms and Conditions ')]").text
print(Text)
time.sleep(5)
driver.quit()