import requests
from bs4 import BeautifulSoup
from time import sleep

# Урок второй - Множественный парсинг + sleep, чтобы скрыть активность бота + маскировка
# Заголовок для маскировки
headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.117 Safari/537.36"}

"""Загружаем ссылку в проект"""
# Тут перебираем все страницы (на сайте page=1,2,3....)
for count in range(1, 8):
    sleep(1)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

    """Загружаем сайт в переменную"""
    # Передаем заголовок для маскировки
    response = requests.get(url, headers=headers)

    """Помогаем библиотеке Soup, в соуп загружаем обработанный сайт (код сайта, метод обработки)"""
    soup = BeautifulSoup(response.text, "lxml")

    """В переменную загружаем результат поиска по парсингу. Аргументы - тег который искали, его класс"""
    # Важно понимать, что парсер видит и выводит первый найденный по параметру тег (их может быть 6, выведит только первый
    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    """find_all - вместо одного блока присваивает в дату все"""
    # Блоки выводятся через запятую списком, а значит через них можно пройти:
    for i in data:
        name = i.find("h4", class_="card-title").text.replace("\n", "")
        price = i.find('h5').text
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
        print(name + "\n" + price + "\n" + url_img + "\n\n")



