import requests
import json
import os

# print(os.getenv('TELEGRAM_TOKEN'))

token = os.getenv('TELEGRAM_TOKEN')
url = 'https://api.hphk.io/telegram/bot{}/getUpdates'.format(token)
response = json.loads(requests.get(url).text)  #dict형으로 변경

"""
"message":{"message_id":3,"from":{"id":748290634,"is_bot":false,"first_name":"Jungjung",
"language_code":"ko"},"chat":{"id":748290634,"first_name":"Jungjung","type":"private"},
"date":1545281599,"text":"\u314e\u3147\u314e\u3147"}}]}

"""

url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(token)

chat_id = response["result"][-1]["message"]["from"]["id"]
msg = response["result"][-1]["message"]["text"]

requests.get(url, params = {"chat_id" : chat_id, "text" : msg})


print(chat_id)
print(msg)