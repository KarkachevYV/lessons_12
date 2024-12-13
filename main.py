import requests
#import pprint

#params = {
#    'q' : 'javascript'
#}
# = requests.get('https://api.github.com/search/repositories', params=params)
#response_json = response.json()
#pprint.pprint(response_json)

#if response.ok:
#   print('Запрос успешно выполнен')
#else:
#    print('Произошла ошибка')
#print (response.text)
#print(response.content)
#response_json = response.json()
#print(f"Количество репозиториев с использованием js: {response_json['total_count']}")
#response = requests.get('https://api.example.com/data')
#data = response.json()  # Преобразуем ответ в словарь

# Предположим, что JSON-объект содержит ключ 'count'
#ount = data.get('count')  # Извлекаем количество
#print(count)
img = ""

response = requests.get(img)
with open("test.jpg" "wb") as file:
  file.write(response.content)