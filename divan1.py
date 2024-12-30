import csv

# Функция для очистки и конвертации строк цены в числовой формат
def clean_price(price_str):
    # Удаляем символ валюты и текст "/мес."
    cleaned_str = price_str.replace('₽/мес.', '').replace(' ', '')
    # Преобразуем в целое число
    return int(cleaned_str)

# Чтение и обработка данных из файла CSV
with open('prices.csv', mode='r', newline='', encoding='utf-8') as infile, \
     open('cleaned_prices.csv', mode='w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Читаем заголовок и пишем его в новый файл (если есть)
    header = next(reader)
    writer.writerow(header)

    # Обработка и запись каждой строки
    for row in reader:
        # Предполагаем, что цена находится в первом столбце
        original_price = row[0]
        cleaned_price = clean_price(original_price)
        writer.writerow([cleaned_price])

print("Обработка завершена. Результаты сохранены в 'cleaned_prices.csv'.")