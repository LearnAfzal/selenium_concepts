import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.oracle.com/in/database/")
driver.maximize_window()
driver.implicitly_wait(30)