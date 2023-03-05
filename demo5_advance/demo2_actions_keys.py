import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://google.com/")
driver.maximize_window()
driver.implicitly_wait(30)
action=webdriver.ActionChains(driver)
action.key_down(webdriver.Keys.SHIFT)\
    .send_keys("hello world").key_up(webdriver.Keys.SHIFT).pause(2)\
    .send_keys(webdriver.Keys.ARROW_DOWN).send_keys(webdriver.Keys.ARROW_DOWN)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(2).send_keys(webdriver.Keys.ENTER).perform()


time.sleep(5)
driver.quit()