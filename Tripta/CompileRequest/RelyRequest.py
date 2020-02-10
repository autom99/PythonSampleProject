from lib2to3.pgen2 import driver
from telnetlib import EC
from pymsgbox import *
from selenium import webdriver
import time

# Code for disable notification of automation in browser
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Some additional functionality with Chrome browser options
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome("D:\Testing Purpose\Pycharm Testing\DemoProject\Tripta\CompileRequest\Driver\chromedriver.exe", options=option)

# driver = webdriver.Firefox("..\Driver\geckodriver.exe")
# driver = webdriver.Edge("..\Driver\msedgedriver.exe")

driver.maximize_window()
time.sleep(1)
driver.set_page_load_timeout(2)

try:
    driver.get("http://192.168.0.10:8082/")

    try:
        driver.find_element_by_xpath("//a[text()='Add Request [RELY]']").click()
        compile_name = input("Enter Compile name : ")
        time.sleep(2)
        driver.find_element_by_id("ContentPlaceHolder1_txtName").send_keys(compile_name)
        time.sleep(2)
        # driver.find_element_by_xpath("//input[@type='text'][@name='ctl00$ContentPlaceHolder1$txtName']").send_keys("NBW")
        driver.find_element_by_id("ContentPlaceHolder1_btnSubmit").click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        alert(text='NBW Compile requested successfully..', title='Compile request', button='OK')
        print("NBW Compile requested successfully..")

        # if driver.find_element("//*[contains(., 'Puffy')]"):


    except InterruptedError:
        print("Error in compilation..")

except ConnectionError:
    print("Exception..")

finally:
    driver.quit()
