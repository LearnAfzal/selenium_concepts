import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.maximize_window()
driver.implicitly_wait(30)
#first of all switch to the frame then find the element
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']")) # if name is not available then we can go with src because its mandatory one in frame
driver.find_element(By.NAME,"fldLoginUserId").send_keys("test123")
driver.find_element(By.LINK_TEXT,"CONTINUE").click() #if the text font is different(Upper & lower case) then go with XPATH
# once we done inside a frame we should switch back to the main content.
# to switch back to main html
driver.switch_to.default_content()
time.sleep(5)