from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.royalcaribbean.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//div[@class='notification-banner__close']").click()
driver.find_element(By.XPATH,"//span[text()='Sign In']").click()
driver.find_element(By.LINK_TEXT,"Create an account").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='First name/Given name']").send_keys("Dennis")
driver.find_element(By.XPATH,"//input[@data-placeholder='Last name/Surname']").send_keys("Rich")
driver.find_element(By.XPATH,"//span[text()='Month']").click()
driver.find_element(By.XPATH,"//span[normalize-space(text())='April']").click()
driver.find_element(By.XPATH,"//span[text()='Day']").click()
driver.find_element(By.XPATH,"//span[normalize-space(text())='4']").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='Year']").send_keys("1990")
driver.find_element(By.XPATH,"//span[text()='Country/Region of residence']").click()
driver.find_element(By.XPATH,"//span[normalize-space(text())='India']").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='Email address']").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//input[@data-placeholder='Create new password']").send_keys("Test@123")
#driver.find_element(By.XPATH,"//span[text()='Select one security question']").click()
#driver.find_element(By.XPATH,"//span[normalize-space(text())='What was your first car's make or model?']").click()
"""driver.find_element(By.XPATH,"//span[contains(@text(),'What was your first car\'s make or model?')]").click()
driver.find_element(By.XPATH,"//input[@data-placeholder='Answer']").send_keys("BMW")"""
driver.find_element(By.XPATH,"//input[@aria-labelledby='emailConsent']").click()
driver.find_element(By.XPATH,"//input[@aria-labelledby='agreements']").click()
driver.find_element(By.XPATH,"//button[normalize-space(text())='Done']").click()
time.sleep(5)
driver.quit()