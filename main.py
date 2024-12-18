import requests

params = {
    'q' : 'html'
}
response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.status_code)

print(f"ответ - {response.json()}")
