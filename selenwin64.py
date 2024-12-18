from selenium import webdriver
from selenium.webdriver import Keys #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time
import random

#Создание экземпляра WebDriver
driver = webdriver.Chrome()

# Открытие нужного URL
driver.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")  # Замените на нужный URL

hatnotes = []
for element in driver.find_elements(By.TAG_NAME, 'div'): #Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable ts-main":
        hatnotes.append(element)

#print(hatnotes)
hatnote = random.choice(hatnotes)

#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
driver.get(link)
time.sleep(5)