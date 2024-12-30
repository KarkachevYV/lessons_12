import csv
import matplotlib.pyplot as plt

# Чтение данных из файла CSV
prices = []
with open('cleaned_prices.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        prices.append(int(row[0]))

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
plt.title('Распределение цен на аренду квартир')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.75)

# Отображение графика
plt.show()