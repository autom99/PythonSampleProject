from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.alert import Alert

import time

driver = webdriver.Chrome("..\Driver\chromedriver.exe")
# driver = webdriver.Firefox("..\Driver\geckodriver.exe")
# driver = webdriver.Edge("..\Driver\msedgedriver.exe")

driver.set_page_load_timeout(4)
time.sleep(2)
driver.get("https://google.com")

driver.find_element_by_name("q").send_keys("Automation Step by Step")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
# driver.find_element_by_name("btnK").click()

time.sleep(2)
driver.quit()

#------------------------ Example -2: Website for testing ------------------------------
# driver.get("http://demo.automationtesting.in/Index.html")
# time.sleep(4)
#
# driver.find_element_by_xpath("//input[@type='text'][@id='email']").send_keys("test@gmail.com")
# time.sleep(2)
# driver.find_element_by_xpath("//img[@id='enterimg']").click()
# driver.back()
#
# driver.find_element_by_xpath("//button[text()='Sign In']").click()
# driver.back()
#
# driver.find_element_by_xpath("//button[text()='Skip Sign In']").click()
# driver.back()
# driver.quit()