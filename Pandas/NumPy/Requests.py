import requests
response = requests.get('https://music.yandex.ru/')
print(response.headers)

