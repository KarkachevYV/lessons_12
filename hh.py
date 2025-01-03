import requests
from bs4 import BeautifulSoup
import csv
import re

# URL страницы с вакансиями
url = "https://tomsk.hh.ru/vacancies/programmist"

# Заголовки для имитации запроса из браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# Выполнение GET-запроса
response = requests.get(url, headers=headers)
response.raise_for_status()  # Вызываем исключение в случае ошибки

# Создание объекта BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск всех карточек вакансий
vacancies = soup.find_all('div', class_='magritte-text-dynamic_stretched___wzj-Q_3-0-22')

# Открытие CSV-файла для записи
with open('vacancies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Запись заголовков столбцов
    writer.writerow(['Вакансия', 'Работодатель', 'Зарплата', 'Ссылка'])

    # Извлечение информации из каждой карточки
    for vacancy in vacancies:
        # Название вакансии
        title_tag = vacancy.find('span', class_='magritte-text___tkzIl_4-3-16')
        title = title_tag.text if title_tag else 'Не указано'
        
        # Ссылка на вакансию
        link_tag = vacancy.find('a', class_='magritte-link_style_neutral___iqoW0_4-3-16')
        link = link_tag['href'] if link_tag else 'Не указана'

        # Имя работодателя
        employer_tag = vacancy.find('div', class_='company-name-badges-container--ofqQHaTYRFg0JM18')
        employer = employer_tag.text.strip() if employer_tag else 'Не указан'

        # Зарплата
        salary_tag = vacancy.find('div', class_='compensation-labels--vwum2s12fQUurc2J')
        salary = salary_tag.text.strip() if salary_tag else 'Не указана'

        # Запись информации в CSV-файл
        writer.writerow([title, employer, salary, link])

print("Данные сохранены в файл vacancies.csv")
print(f"Найдено {len(vacancies)} вакансий")