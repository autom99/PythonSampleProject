from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

# firefoxOptions = webdriver.FirefoxOptions()
# firefoxOptions.add_argument("--no-sandbox")
# firefoxOptions.add_argument("--headless")

# firefoxOptions.add_argument("--start-maximized")
# firefoxOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
# firefoxOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Firefox(executable_path="D:/Testing Purpose/Pycharm Testing/DemoProject/Driver/geckodriver.exe")
# driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chromeOptions)
driver.maximize_window()
driver.get("https://www.autom99.blogspot.com/")

print(driver.page_source)

driver.quit()