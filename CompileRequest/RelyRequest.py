from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Testing Purpose\Pycharm Testing\CompileRequest\Driver\chromedriver.exe")
# driver = webdriver.Firefox("..\Driver\geckodriver.exe")
# driver = webdriver.Edge("..\Driver\msedgedriver.exe")

driver.set_page_load_timeout(4)
time.sleep(2)

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
        print("NBW Compile requested successfully..")

    except Exception:
        print("Error in compiletime..")

except ConnectionError:
    print("Exception..")

finally:
    driver.quit()
