from bs4 import BeautifulSoup
import requests
import smtplib

URL = 'https://www.amazon.in/Logitech-Hero-Gaming-Mouse-Black/dp/B07GBZ4Q68/ref=sr_1_3?keywords=logitech+g502&qid=1562920159&s=computers&sr=1-3'

source = requests.get(URL).text

soup = BeautifulSoup(source, 'lxml')

def check_price():
    # Scraping the title and price tag of the product
    title = soup.find(id='productTitle').text.strip()
    price = soup.find('span', id='priceblock_ourprice').text

    # Removing the symbol and the comma from the scraped price and converting the string to float to float
    price = price[2:7].replace(',','')
    converted_price = float(price)

    print(title)
    print(converted_price)
    # Check if price is lower than desired price.
    if (converted_price < 30000.0):
        print("Price is lower than Rs.30,000")
        return;

    print(converted_price)
    print("Price is higher than Rs.30,000")

check_price()