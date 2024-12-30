import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Получение HTML-кода страницы
url = 'https://www.divan.ru/category/divany'  # Замените на точный URL с диванами
response = requests.get(url)
html_content = response.text

# Парсинг HTML-кода
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение данных о диванах
# Предположим, что цены хранятся в элементах с классом 'price'
prices = []
for price_tag in soup.find_all(class_='ui-LD-ZU'):  # Замените 'price' на фактический класс
    price_text = price_tag.get_text()

    # Очистка строки от текстовых символов
    price_text = price_text.replace('₽', '').replace('руб.', '').replace(' ', '').strip()

    try:
        price = float(price_text)
        prices.append(price)
    except ValueError:
        # Если невозможно преобразовать в float, выведите предупреждение и продолжите
        print(f"Не удалось преобразовать {price_text} в число.")

# Сохранение данных в CSV
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

# Вычисление и вывод средней цены
average_price = df['Price'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Построение гистограммы
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.show()