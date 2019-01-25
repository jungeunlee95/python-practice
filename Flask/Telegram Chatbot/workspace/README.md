

- **내가입 :**   https://web.telegram.org/ 
- **Linux crontab** 

**내 key값 넣기 Terminal**

```
touch telegram.py


vi ~/.bashrc
o 누르면 --INSERT-- 뜸
```

```
ESC연타 =>
:wq 로 나오기
```

**잘 들어갔는지 확인하기**



**telegram.py**

```python
import requests
import json
import os

# print(os.getenv('TELEGRAM_TOKEN'))

token = os.getenv('TELEGRAM_TOKEN')
url = 'https://api.hphk.io/telegram/bot{}/getUpdates'.format(token)
response = requests.get(url).text
print(response)
```

​	**--이렇게 짜고 telegram가서 채팅치고 실행하면**  "text" : "내가 쓴 글" 날라옴



**telegram.py**

```python
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
```







# TELEGRAM 에서 자동 답장

**day5 - app.py**

```python
from flask import Flask, request
import requests
import time
import json
import os
from bs4 import BeautifulSoup

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')), methods=['POST'])
def telegram() :
    # 텔레그램으로부터 요청이 들어 올 경우, 해당 요청을 처리하는 코드
    print(request.get_json())
    return '', 200
    
@app.route('/set_webhook')    # alert창 띄우기 
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url' : 'https://sspy-week2-juneun.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    response = requests.get(url, params = params).text
    return response
```



### 자동 답장 오게 하기

**app.py**

```python
from flask import Flask, request
import requests
import time
import json
import os
from bs4 import BeautifulSoup

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')), methods=['POST'])
def telegram() :
    # 텔레그램으로부터 요청이 들어 올 경우, 해당 요청을 처리하는 코드
    #print(request.get_json()["message"]["from"]["id"])
    #print(request.get_json()["message"]["text"])
    response = request.get_json()
    
    """
    {'update_id': 693359414, 'message': {'message_id': 22, 'from': {'id': 748290634, 
    'is_bot': False, 'first_name': 'Jungjung', 'language_code': 'ko'}, 'chat': {'id': 748290634, 
    'first_name': 'Jungjung', 'type': 'private'}, 'date': 1545292109, 'text': '하이하이'}}
    """

    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)

    chat_id = response["message"]["from"]["id"]
    msg = response["message"]["text"]
    
    requests.get(url, params = {"chat_id" : chat_id, "text" : msg})

    return '', 200
    
    
@app.route('/set_webhook')    # alert창 띄우기 
def set_webhook():
    url = TELEGRAM_URL + '/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url' : 'https://sspy-week2-juneun.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    response = requests.get(url, params = params).text
    return response
    

```







