from builtins import print

from selenium import webdriver
import time

# Some additional functionality with Chrome browser options
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome("D:\Testing Purpose\Pycharm Testing\TriptaFirewallTesting\Driver\chromedriver.exe")
# driver = webdriver.Firefox("..\Driver\geckodriver.exe")
# driver = webdriver.Edge("..\Driver\msedgedriver.exe")

driver.set_page_load_timeout(4)
time.sleep(2)

# Is_url_flag = ""
# LogOut_url = "http://192.168.0.99:1000/keepalive?0d07030705031f99"
Login_url = "http://192.168.0.99:1000/login?020c1eab957d0891"

try:
    # if Is_url_flag is LogOut_url:
    # if Is_url_flag == str("keepalive"):
    driver.get(Login_url)
    time.sleep(2)
    driver.find_element_by_id("ft_un").send_keys("Developer")
    time.sleep(2)
    driver.find_element_by_id("ft_pd").send_keys("Developer")
    time.sleep(2)

except ConnectionError:
    print("Exception..")

finally:
    print("You have successfully login to TRIPTA FIREWALL SECURITY..!!")
    driver.quit()
