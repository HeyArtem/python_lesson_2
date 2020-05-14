import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data = json.loads(response.text)
print(data)
print("Дата курса ", data['Timestamp'])
print('Hello wodrld!')
print('Простите, что взял вашу ссылку, много времени потратил и ненашел рабочую.\nВозможно не знал, где искать.')







