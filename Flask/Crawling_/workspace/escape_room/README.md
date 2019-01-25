# 2018-12-21

### 마스터키 

- google 특정 문자 제거: python how to eliminate string from string

http://www.master-key.co.kr/home/office     - 지점안내/예약  - 페이지 소스 보기

```html
<ul class="escape_list">
    	<li class='escape_view' id='booking15'>
		<div class='escape_Info_wrap clearfix'>
			<div class='slider-wrapper'>
				<div class='slider-box' style='background-image: url(/upload/store/15_img1.jpg);'></div>
				<div class='slider-box' style='background-image: url(/upload/store/15_img2.jpg);'></div>
				<div class='slider-box' style='background-image: url(/upload/store/15_img3.jpg);'></div>
				<div class='slider-box' style='background-image: url(/upload/store/15_img4.jpg);'></div>
			</div>
			<div class='escape_text'>
				<p>부천점<span class="new">NEW</span></p>
				<dl>
					<dt>- 주소 : &nbsp;</dt>
					<dd><span> 경기도 부천시 원미구 심곡동 175-9 6층</span> </dd>
				</dl>
				<dl>
					<dt>- 연락처  : &nbsp;</dt>
					<dd><span>050-7457-5485</span></dd>
				</dl>
			</div>
		</div>
		<a href='/booking/bk_detail?bid=15'><span class='detail_btn'>예약하기 </span></a>
	</li>
```

--> ul 밑의 <li class='escape_view' ...> 를 긁어야겠구나

![1545355643406](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545355643406.png)

->  Network -> office -> Headers - > Request URL 복사

**Terminal**

```cmd
juneun:~/workspace $ cd day5
juneun:~/workspace/day5 (master) $ touch master_key.py
```



- ### 지점 이름 가져오기

**master_key.py**

```python
from bs4 import BeautifulSoup as bs
import requests

def master_key_list():
    url = 'http://www.master-key.co.kr/home/office'
    
    response = requests.get(url).text
    
    document = bs(response, 'html.parser')
    
    # class = .class이름  /  id = #id이름
    ul = document.select('.escape_list')
    
    lis = document.select('.escape_list .escape_view')
    
    cafe_list = []
    for li in lis :
        #print(li.select_one('p').text)
        #print(li.select('dd'))
        #print(li.select_one('a')["href"])
        
        # python how to eliminate string from string
        title = li.select_one('p').text
        if(title.endswith('NEW')) :
            title = title[:-3]
            
        address = li.select('dd')[0].text
        tel = li.select('dd')[1].text
            
        link = 'http://www.master-key.co.kr' + li.select_one('a')["href"]    
        
        cafe = {
            'title' : title,
            'tel' : tel,
            'address' : address,
            'link' : link
        }
        cafe_list.append(cafe)
    
    print(cafe_list)


```



- ### 예약 가능 정보 데이터 

![1545358979729](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545358979729.png)

http://www.master-key.co.kr/booking/bk_detail?bid=7

->  Network -> booking_list_new-> Headers - > Request URL 복사  -> post 방식

-> Headers 맨 밑에 Form Data로 날짜정보 날려야함 

->  Response의 html태그 

```html
<ul class='reserve'>
	<li class='escape_view'>
		<div class='escape_Info_wrap clearfix'>
		<div class='escape_Img' data-title='시크릿가든' data-img='/upload/room/65_img1.jpg' data-text='＂세상에서 가장 아름다운 꽃을 보여드립니다.“>
			<img src='/upload/room/65_img1.jpg' alt='시크릿가든' />
		</div>

		<div class='res_box_wrap'>

			<div class='escape_text clearfix'>
				<p>시크릿가든</p>
				<p>
					<span>테마유형 : 감성</span>
					<span>난이도:
				<i class='fa fa-key' aria-hidden='true'></i>
                <i class='fa fa-key' aria-hidden='true'></i>
                <i class='fa fa-key' aria-hidden='true'></i>
                <i class='fa fa-key' aria-hidden='true'></i>	</span>
					<span>인원:  2~4</span>
				</p>
			</div>

			<div class='col_wrap clearfix'>

		<div class='col true c_pointer' onclick='modal_show("1020", "65","시크릿가든")'>
			<div>
				<p class='time'>10:20</p>
				<p class='state'>예약가능</p>
			</div>
		</div>

		<div class='col false' >
			<div>
				<p class='time'>11:40</p>
				<p class='state'>예약완료</p>
			</div>
		</div>
```



**master_key.py**

```python
from bs4 import BeautifulSoup as bs
import requests

def master_key_info(cd):
    url = 'http://www.master-key.co.kr/booking/booking_list_new'
    params = {
        'date' : '2018-12-22',
        'store' : cd,
        'room' : ''
        
    }
    response = requests.post(url, params).text
    document= bs(response, 'html.parser')
    ul = document.select('.reserve')
    lis = document.select('.reserve .escape_view')
    
    theme_list = []
    for li in lis:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col'):
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        
        theme = {
            'title' : title,
            'info' : info
        }
        
        theme_list.append(theme)
        
    print(theme_list)
```





## Telegram에 적용

```python
from flask import Flask, request, render_template
import requests
import time
import json
import os
from bs4 import BeautifulSoup as bs

app = Flask(__name__)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram'
CAFE_LIST = {
    '전체' : -1,
    '부천점' : 15,
    '안양점' : 13,
    '대구동성로2호점' : 14,
    '대구동성로점' : 9,
    '궁동직영점' : 1,
    '은행직영점' : 2,
    '부산서면점' : 19,
    '홍대상수점' : 20,
    '강남점' : 16,
    '건대점' : 10,
    '홍대점' : 11,
    '신촌점' : 6,
    '잠실점' : 21,
    '부평점' : 17,
    '익산점' : 12,
    '전주고사점' : 8,
    '천안신부점' : 18,
    '천안점' : 3,
    '천안두정점' : 7,
    '청주점' : 4
}
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
    chat_id = response["message"]["from"]["id"]
    #msg = response["message"]["text"]
    txt = response["message"]["text"]

    
    if(txt.startswith('마스터키')) :
        cafe_name = txt.split(' ')[1]
        
        cd = CAFE_LIST[cafe_name]
        
        if(cd > 0):
            data = master_key_info(cd)
        else :
            data = master_key_list()
        msg = []
        for d in data:
            msg.append('\n'.join(d.values()))
        msg = '\n'.join(msg)

    else:
        msg = '등록되지 않은 메세지입니다.'
    
    
        
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)

    
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
    
    
    
def master_key_info(cd):
    url = 'http://www.master-key.co.kr/booking/booking_list_new'
    params = {
        'date' : '2018-12-22',
        'store' : cd,
        'room' : ''
        
    }
    response = requests.post(url, params).text
    document= bs(response, 'html.parser')
    ul = document.select('.reserve')
    lis = document.select('.reserve .escape_view')
    
    theme_list = []
    for li in lis:
        title = li.select('p')[0].text
        info = ''
        for col in li.select('.col'):
            info = info + '{} - {}\n'.format(col.select_one('.time').text, col.select_one('.state').text)
        
        theme = {
            'title' : title,
            'info' : info
        }
        
        theme_list.append(theme)
        
    return theme_list


def master_key_list():
    url = 'http://www.master-key.co.kr/home/office'
    
    response = requests.get(url).text
    
    document = bs(response, 'html.parser')
    
    # class = .class이름  /  id = #id이름
    ul = document.select('.escape_list')
    
    lis = document.select('.escape_list .escape_view')
    
    CAFE_LIST = []
    for li in lis :
        #print(li.select_one('p').text)
        #print(li.select('dd'))
        #print(li.select_one('a')["href"])
        
        # python how to eliminate string from string
        title = li.select_one('p').text
        if(title.endswith('NEW')) :
            title = title[:-3]
            
        address = li.select('dd')[0].text
        tel = li.select('dd')[1].text
            
        link = 'http://www.master-key.co.kr' + li.select_one('a')["href"]    
        
        cafe = {
            'title' : title,
            'tel' : tel,
            'address' : address,
            'link' : link
        }
        CAFE_LIST.append(cafe)
    
    # print(CAFE_LIST)
    return CAFE_LIST



```

https://web.telegram.org/#/im?p=@mmyy_apartment_bot

--------------------------------------------------------------------------------------
# 2018-12-21

### 서이룸

![1545372659244](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545372659244.png)

http://www.seoul-escape.com/reservation/

Network - Headers - Request URL 복사 -> parameter빼고 params로 변수 따로 줄거임

**Terminal**

```cmd
juneun:~/workspace/day5 (master) $ touch seoul.py
```



**seoul.py**- 내코드

```python
import requests
import json

def seoul_escape_list(cafe_name) :
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date' : "2018/12/21"
    }
    response = requests.get(url, params = params).text
    document = json.loads(response)
    
    cafe_code = {}
    #{'강남1호점': 3, '홍대2호점': 10, '강남2호점': 11, '홍대1호점': 1, '인천 부평점': 4, '부산 서면점': 5 }
    for book in document["bookList"]:
        cafe_code[book["branch"]]=book["branch_id"]
    # for key, value in cafe_code.items():
    #     print(key)
    
    
    txt = cafe_name
    
    for book in document["bookList"]:
        if(book["branch"] == txt):
            booked = book["booked"]
            
            if(booked == False):
                booked = "예약가능"
            elif(booked == True):
                booked = "예약불가"
            else:
                booked = "홈페이지에서 확인해주세요."
                
            print("{} - {} : {} = {} ".format(book["branch"],book["hour"], book["room"], booked))


seoul_escape_list("홍대2호점")



```





### Telegram에 적용하기



**app.py**

```python
...

    elif(txt.startswith('서이룸')) :
        cafe_name = txt.replace("서이룸", "").lstrip()
        
        if(cafe_name == "부산서면점"):
            cafe_name = "부산 서면점"
        elif(cafe_name == "인천부평점"):
            cafe_name = "인천 부평점"
            
        data = seoul_escape_list(cafe_name)
        
        msg = []
        for d in data:
            msg.append('\n'.join(d.values()))
        msg = '\n'.join(msg)

        
    else:
        msg = '등록되지 않은 메세지입니다.'
    
    
        
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(TELEGRAM_TOKEN)

    
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
    
    
    
def seoul_escape_list(cafe_name) :
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date' : "2018/12/21"
    }
    response = requests.get(url, params = params).text
    document = json.loads(response)
    
    cafe_code = {}
    #{'강남1호점': 3, '홍대2호점': 10, '강남2호점': 11, '홍대1호점': 1, '인천 부평점': 4, '부산 서면점': 5 }
    for book in document["bookList"]:
        cafe_code[book["branch"]]=book["branch_id"]
    
    txt = cafe_name
    CAFE_LIST = []
    for book in document["bookList"]:
        if(book["branch"] == txt):
            booked = book["booked"]
            
            if(booked == False):
                booked = "예약가능"
            elif(booked == True):
                booked = "예약불가"
            else:
                booked = "홈페이지에서 확인해주세요."
            
            cafe = {
                'title' : '---------' + book["branch"] + '---------',
                'time' : book["hour"],
                'room' : book["room"],
                'booked' : '<'+booked+'>'
            }   
            CAFE_LIST.append(cafe)
            #print("{} - {} : {} = {} ".format(book["branch"],book["hour"], book["room"], booked))
    #print(CAFE_LIST)
    return CAFE_LIST

```



![1545379591850](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545379591850.png)