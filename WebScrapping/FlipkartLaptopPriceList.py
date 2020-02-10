from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Some additional functionality with Chrome browser options
option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

try:
    driver = webdriver.Chrome("D:/Testing Purpose/Pycharm Testing/DemoProject/Driver/chromedriver.exe", options=option)

    products = []  # List to store name of the product
    prices = []  # List to store price of the product
    # ratings = []  # List to store rating of the product

    page = requests.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())

    for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
        name = a.find('div', attrs={'class': '_3wU53n'})
        price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
        rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
        products.append(name.text)
        prices.append(price.text)
        # ratings.append(rating.text)

    df = pd.DataFrame(
        {
            'Product Name': products,
            'Price': prices,
            # 'Rating': ratings
        })
    df.to_csv('Results/products.csv', index=False, encoding='utf-8')

except Exception:
    print(Exception.with_traceback())

finally:
    driver.close()