from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.db4free.net/")
driver.maximize_window()
driver.implicitly_wait(30)
# to switch new tab in same window
driver.switch_to.new_window("tab")
driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"//a[@href='/phpMyAdmin']").click()
time.sleep(5)
print(driver.window_handles)

#for each -> to fetch the session id, url, title
for window in driver.window_handles:
    print(window)
    driver.switch_to.window(window)
    print(driver.current_url)
    print(driver.title)
    print("--------------")

# break the loop once we got the expected tab/title
for window in driver.window_handles:
    print(window)
    driver.switch_to.window(window)
    print(driver.title)
    if "phpMy" in driver.title:
        break
    print("-------")

#driver will point to tab with title phpMyAdmin
driver.find_element(By.ID,"input_username").send_keys("afzal")

time.sleep(5)
"""driver.close() # it will close the current session id/tab"""
driver.quit()