import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30) #universal/global level - it means for entire case, no need to declare multiple times
driver.find_element(By.LINK_TEXT,"Create new account").click()
#time.sleep(5)
driver.find_element(By.NAME,"firstname").send_keys("Afzal")
driver.find_element(By.NAME,"lastname").send_keys("I")
driver.find_element(By.ID,"password_step_input").send_keys("Welcome123")
driver.find_element(By.XPATH,"//input[@value='-1']").click()
select_day=Select(driver.find_element(By.ID,"day")) #make use of Select class wherever you see select tag in script i.e, mostly in dropdown/combobox
select_day.select_by_value('10')
select_month = Select(driver.find_element(By.ID, "month")).select_by_value('8')
select_year = Select(driver.find_element(By.ID, "year")).select_by_value('1991')
driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)