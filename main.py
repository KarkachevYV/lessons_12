import requests
#import pprint

params = {
    'q' : 'html'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
#response_json = response.json()
#pprint.pprint(response_json)

#if response.ok:
#   print('Запрос успешно выполнен')
#else:
#    print('Произошла ошибка')
#print (response.text)
#print(response.content)
#response_json = response.json()
#print(f"Количество репозиториев с использованием html: {response_json['total_count']}")

#img = "https://i.pinimg.com/236x/75/91/08/759108b7ad69db854d9a6b9977324076.jpg"

#response = requests.get(img)
#with open("test.jpg", "wb") as file:
#  file.write(response.content)

#response = requests.get('https://google.com') # Запрос

#print(response.status_code)  # Вывод статус-кода

#print(response.headers)  # Вывод заголовка

#print(response.text)  # Вывод основного текста (тела)

#url= "https://jsonplaceholder.typicode.com/posts"

#data = {
#  "title" : "foo",
#  "body"  : "bar",
#  "userId" : 1
#}

#response = requests.post(url, data=data)

print(response.status_code)

print(f"ответ - {response.json()}")