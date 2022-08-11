import json
import requests

TOKEN = 'abcdefghijklmnopqrstuvwxyz'

r = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
answer = json.loads(r.text)
chat_id = answer['result']['message']['chat']['id']
print(chat_id)

message = 'Hello'   # сообщение
chat_id = answer['result']['message']['chat']['id']   # id чата

params = {
    'chat_id' : chat_id,
    'text' : message
}

requests.post(
    f'https://api.telegram.org/bot{TOKEN}/sendMessage',   # отправляем сообщение
    data = params     # передаем параметры в метод post
)

URL = 'https://www.ikea.com/ru/ru/'

driver = open_page(URL)
page_source = get_ikea_html(URL, driver)
start_h1 = get_h1(page_source)[0].text
print(start_h1)