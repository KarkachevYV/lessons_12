#import matplotlib.pyplot as plt

# x = [2, 6, 8, 14, 15]
# y = [6, 8, 10, 15,20]

# plt.plot(x, y)

# plt.title("Пример простого линейного графика")

# plt.xlabel("х ось")
# plt.ylabel("у ось")

# plt.show()
#----------------------------------------------
# data = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6]

# plt.hist(data, bins=6)

# plt.xlabel("х ось")
# plt.xlabel("у ось")
# plt.title("Тестовая гистограма")

# plt.show()
#--------------------------------------------
# x = [2, 6, 8, 14, 15]
# y = [7, 9, 60, 13,20]

# plt.scatter(x, y)

# plt.xlabel("х ось")
# plt.xlabel("у ось")
# plt.title("Тестовая гистограма рассеяния")

# plt.show()
#-------------------------------------------
#import numpy as np

# a = np.array([1, 2, 3, 4])
# print(a)
#------------------------------------------------------
# a = np.zeros((3, 3))
# print(a)
#------------------------------------------------------
# a = np.ones((2,5))
# print(a)
#------------------------------------------------------
# a = np.random.random((2, 5))
# print(a)
#------------------------------------------------------
# a = np.arange(0, 10, 2)
# print(a)
#----------------------------------------------------
# a = np.linspace(0, 1, 10)
# print(a)
#----------------------------------------------------
# x = np.linspace(-10, 10, 100)

# y = x**2

# plt.plot(x, y)
# plt.xlabel("х ось")
# plt.xlabel("у ось")
# plt.title("График функции y = x**2")

# plt.grid(True)
# plt.show()
#------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Инициализация веб-драйвера
driver = webdriver.Chrome()


# Открывает сайт
driver.get('https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/')

# Даем странице время на загрузку
time.sleep(5)

# Находим элементы, содержащие цены
# Обратите внимание, что структура сайта может измениться, и вам может потребоваться обновить селекторы
price_elements = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Открываем файл CSV для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Пишем заголовок (если необходимо)
    writer.writerow(['Цена'])

    # Пишем каждую цену в файл
    for price in price_elements:
        writer.writerow([price.text])
# Закрываем браузер
driver.quit()
#------------------------------------------------------