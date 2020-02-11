from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--headless")

chromeOptions.add_argument("--start-maximized")
chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome("D:/Testing Purpose/Pycharm Testing/DemoProject/Driver/chromedriver.exe", options=chromeOptions)
# driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chromeOptions)
driver.get("https://www.autom99.blogspot.com/")

print(driver.page_source)