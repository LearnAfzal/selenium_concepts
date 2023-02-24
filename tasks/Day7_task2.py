import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"UserFirstName").send_keys("afzal")
driver.find_element(By.NAME,"UserLastName").send_keys("i")
driver.find_element(By.NAME,"UserEmail").send_keys("afzalit003@gmail.com")
#driver.find_element(By.NAME,"UserTitle").send_keys("IT Manager")
select_title=Select(driver.find_element(By.NAME,"UserTitle")).select_by_value("IT_Manager_AP") #dropdown values which we see in GUI would not be same as/equal to select_by_value
driver.find_element(By.NAME,"CompanyName").send_keys("afzalit003@gmail.com")
#driver.find_element(By.NAME,"CompanyEmployees").send_keys("1-15 employees")
#driver.find_element(By.NAME,"CompanyCountry").send_keys("United Kingdom")
select_employees=Select(driver.find_element(By.NAME,"CompanyEmployees")).select_by_value("9")
select_country=Select(driver.find_element(By.NAME,"CompanyCountry")).select_by_value("GB")
driver.find_element(By.CLASS_NAME,"checkbox-ui").click()
driver.find_element(By.XPATH,"//div[@class='form_submit_button submitButton buttonCTAItemComponent parbase']").click()
#driver.find_element(By.LINK_TEXT,"Enter a valid phone number").is_displayed()
time.sleep(5)
driver.quit()