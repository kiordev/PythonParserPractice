import requests
from bs4 import BeautifulSoup

# Настройки
url = "https://uastal.com/forges"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# Поиск названия
data = soup.find("li", class_="show-up")
name = data.find("div", class_="cat").text

# Поиск цены + преобразование 2.350.00 в 2350 и целочисленный тип
price = data.find("span", class_="price").text.replace(".", "0").replace(",", '.').replace(".", "")
slice_price = price[:-3]
final_price = int(slice_price)
