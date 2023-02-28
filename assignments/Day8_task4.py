import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("https://www.automationworld.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Subscribe").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.ID,"id24_344").click()
driver.find_element(By.ID,"id1").send_keys("afzal")
driver.find_element(By.ID,"id2").send_keys("khan")
driver.find_element(By.ID,"id10").send_keys("engineer")
driver.find_element(By.ID,"id195").send_keys("www.abcd.com")
driver.find_element(By.ID,"id3").send_keys("abcd")
driver.find_element(By.ID,"id11").send_keys("1234567890")
select_country=Select(driver.find_element(By.ID,"id7")).select_by_value("189")
driver.find_element(By.ID,"id6").send_keys("chennai")
driver.find_element(By.ID,"id339_2327").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
alert_text=driver.find_element(By.XPATH,"//li[contains(text(),'Email Address is required.')]").text
print(alert_text)
time.sleep(5)
driver.quit()