import requests
from bs4 import BeautifulSoup

# Урок первый - Концепция парсинга

"""Загружаем ссылку в проект"""
url = "https://scrapingclub.com/exercise/list_basic/?page=1"

"""Загружаем сайт в переменную"""
response = requests.get(url)

"""Помогаем библиотеке Soup, в соуп загружаем обработанный сайт (код сайта, метод обработки)"""
soup = BeautifulSoup(response.text, "lxml")

"""В переменную загружаем результат поиска по парсингу. Аргументы - тег который искали, его класс"""
# Важно понимать, что парсер видит и выводит первый найденный по параметру тег (их может быть 6, выведит только первый
data = soup.find("div", class_="col-lg-4 col-md-6 mb-4")

"""Тут создали переменную имя, и вытащили и конкретного тега текст по атрибуту"""
# С помощью реплейса мы убрали пробелы и пересы в тексте (они всегда будут
name = data.find("h4", class_="card-title").text.replace("\n", "")

"""Нашли прайс в теге h5"""
price = data.find('h5').text
"""Тут мы используем метод гет для того, чтобы забрать значение атрибута"""
url_img = "https://scrapingclub.com"+data.find("img", class_="card-img-top img-fluid").get("src")

print(url_img)