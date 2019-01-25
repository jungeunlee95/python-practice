### - bootstrap site

https://startbootstrap.com/template-categories/all/

![1545178726222](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545178726222.png)



![1545178742680](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545178742680.png)

- **다운 -> 전체를 붙여넣기**

![1545179019907](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179019907.png)

​     

- **new repository**

![1545179174616](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179174616.png)

- **git push**

![1545179322980](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179322980.png)



![1545179357817](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179357817.png)



![1545179393861](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179393861.png)



![1545179470438](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179470438.png)

- **확인**

  github repository 주소 치면 나옴

  ![1545179639547](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179639547.png)



- **repository -> Settings**

![1545179993210](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545179993210.png)

**custom domain으로 도메인 바꿀 수 있음**



- **index파일 수정**

![1545180195930](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545180195930.png)

vscode 로 열기 -> modify



- **아이콘 찾기** - Font Awesome

  ![1545181791190](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545181791190.png)





![1545181860446](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545181860446.png)



- **수정 후**

 `git add . /  git commit -m "my profile"  / git push                                           `



- **c9.io**

![1545183909774](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545183909774.png)



![1545183964400](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545183964400.png)

**--> workspace 생성**



- **파이썬 설치**

  ## pyenv

  #### install

  ```
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

  #### 환경변수 설정

  ```
  $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  $ source ~/.bashrc
  ```

  ### 환경변수 추가후 bashrc 실행 => 터미널 새로고침

  ### Install python

  ```
  $ pyenv install 3.6.1 # pyenv를 통해서 python 3.6.1을 설치 
  $ pyenv global 3.6.1 # 전역으로 버전 설정
  $ python -V # 파이썬 버전 확인
  $ pyenv versions # 사용가능한 파이썬 버전 리스트 출력
  ```

  ### Install packages

  ```
  $ pip install flask
  $ pip install bs4 # beautiful soup
  $ pip install requests
  ```

  ### flask setting

  ```
  $ echo 'export FLASK_ENV=development' >> ~/.bashrc
  ```



- **c9.io 터미널 창에 붙여넣기**

![1545185271958](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545185271958.png)

![1545185375008](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545185375008.png)

**$ vi ~/.bashrc        확인**

**$ :q     			종료**

![1545185553906](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545185553906.png)



- **파이썬설치**

![1545185711867](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545185711867.png)



- ​	**설치 기다리면서 폴더 만들어보기** 

![1545185878865](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545185878865.png)

![1545185959298](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545185959298.png)

- 설치 된 후 

  ```
  $ pyenv global 3.6.7  # 3.6.7버전으로
  $ pyenv versions	  # 버전 확인
  ```

  ```
  $ pip install flask
  $ pip install bs4 # beautiful soup
  $ pip install requests 
  ```

  ```
  $ echo 'export FLASK_ENV=development' >> ~/.bashrc
  ```







- **만들어보기**

  ![1545187104677](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545187104677.png)

![1545187290858](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545187290858.png)

![1545187298377](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545187298377.png)



# 2018-12-19

- **Flask**

```
$ touch app2.py

```

![1545192518423](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545192518423.png)

- 파일 복사 

  ```
  $ mv app2.py app.py
  
  ```

- Flask 실행

![1545193265033](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545193265033.png)

```
$ flask run --host 0.0.0.0 --port 8080

```

![1545193140357](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545193140357.png)

![1545193149932](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545193149932.png)

### flask setting

```
$ echo 'export FLASK_ENV=development' >> ~/.bashrc

```

![1545193766730](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545193766730.png)

![1545193894333](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545193894333.png)

 



- 네이버 웹툰 넣어보기

  **app.y**

  ```python
  from flask import Flask
  import requests
  import time
  from bs4 import BeautifulSoup as bs
  
  app = Flask(__name__)
  
  @app.route('/index')
  def index():
      print("hi")
      print("Nice To Meet You")
      return """
             <h1>얘 귀엽다</h1>
             <img src = "data:image/jpeg;base64,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">
             """
      
  @app.route('/naver_toon')
  def naver_toon():
      today = time.strftime("%a").lower()
      
      naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
      response = requests.get(naver_url).text
      soup = bs(response, 'html.parser')
      
      # 강사님 코드
      toons =  []
      li = soup.select('.img_list li')
      for item in li:
        toon = {
          # "title" : item.select('dt a')[0].text,    # 아래와 같은 코드
          "title" : item.select_one('dt a').text,
          "url" : "https://comic.naver.com/" + item.select('dt a')[0]["href"],
          "img_ul" : item.select('.thumb img')[0]["src"]
        }
        toons.append(toon)
        
        
      return "{}".format(toons)
        
  
  
  ```



- **import 변경**

  ```python
  from flask import Flask
  -> from flask import Flask, render_template
  
  ```

  - **return 값 변경 후 html파일 작성**

  ```python
    return render_template('naver_toon.html')
  
  ```

  ![1545196680610](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545196680610.png)

![1545196688807](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545196688807.png)



- **naver_toon.html**

```html
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <h1>naver webtoon 모아보기</h1>
    </body>
</html>

```

![1545197002104](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545197002104.png)



- python 코드 html에서 받기

**app.py**

```python
 return render_template('naver_toon.html', t = toons)

```

![1545197586945](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545197586945.png)

**t라는 이름으로 toons를 보냄** 

​			naver_toon.html 에서 {{ t }} 이렇게 t를 받을 수 있음

​			python 문법은 {% %}

**naver_toon.html** 

```html
<!DOCTYPE html>
<html>
    <head> 
    </head>
    <body>
        <h1>naver webtoon 모아보기</h1>
        {% for i in range(5): %}     	<!--파이썬문법-->
            {{ t }}					 	<!--py에서 받는 값-->
        {% endfor %}
    </body>
</html>

```

![1545198155681](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545198155681.png)

​										+tab하면 td3개 생성





- 실습 - naver webtoon list 가져오기 

  **app.py**

  ```python
  from flask import Flask, render_template
  import requests
  import time
  from bs4 import BeautifulSoup as bs
  
  @app.route('/naver_toon')
  def naver_toon():
      today = time.strftime("%a").lower()
      
      naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
      response = requests.get(naver_url).text
      soup = bs(response, 'html.parser')
      
      # 강사님 코드
      toons =  []
      li = soup.select('.img_list li')
      for item in li:
        toon = {
          # "title" : item.select('dt a')[0].text,    # 아래와 같은 코드
          "title" : item.select_one('dt a').text,
          "url" : "https://comic.naver.com/" + item.select('dt a')[0]["href"],
          "img_url" : item.select('.thumb img')[0]["src"]
        }
        toons.append(toon)
        
        
      return render_template('naver_toon.html', t = toons)
  
  
  ```



  **naver_toon.html** - 내 코드

```html
  <!DOCTYPE html>
  <html>
      <head>
      </head>
      <body>
          <h1>naver webtoon 모아보기</h1>
          <table>
              <thead>
                  <tr>
                      <th>썸네일</th>
                      <th>웹툰 제목</th>
                      <th>웹툰 링크</th>
                  </tr>
              </thead>
              <tbody>
                  {% for i in range(t|length): %}
                  <tr>
                      <td>
                          <img src="{{ t[i]["img_url"] }}">
                          </img>
                      </td>
                      <td>&nbsp;&nbsp;&nbsp;&nbsp;{{ t[i]["title"] }}</td>
                      <td> <a href="{{ t[i]["url"] }}"> 보러가기</a></td>
                  </tr>
                  {% endfor %}
              </tbody>
          </table>
      </body>
  </html>

```

  **naver_toon.html** -강사님 코드

```html
  <!DOCTYPE html>
  <html>
      <head>
          
      </head>
      <body>
          
          <h1>naver webtoon 모아보기</h1>
          
          <table>
              <thead>
                  <tr>
                      <th>썸네일</th>
                      <th>웹툰 제목</th>
                      <th>웹툰 링크</th>
                  </tr>
              </thead>
              <tbody>
                  {% for toon in t: %}
                  <tr>
                      <td>
                          <img src="{{ toon["img_url"] }}">
                          </img>
                      </td>
                      <td>&nbsp;&nbsp;&nbsp;&nbsp;{{ toon["title"] }}</td>
                      <td> <a href="{{ toon["url"] }}"> 보러가기</a></td>
                  </tr>
                  {% endfor %}
  
                  
              </tbody>
          </table>
  
      </body>
  </html>

```

![1545199967331](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545199967331.png)





- dict 예제 문제

  https://gist.github.com/edutak/782b7c507931515ae550538c505ae9fb

  ![1545201925238](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545201925238.png)

**dict.py** - 내코드

```python
"""
파이썬 dictionary 활용 기초!
"""
# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
sum = 0
for key in iu_score.keys():
    sum += iu_score[key]
print("평균은 {}입니다.".format(sum/3))

# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
for key in score:
    print(key)
    for name in score[key]:
        print(name)

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.

print("=====Q3=====")
for name in city:
  sum2=0
  for deg in city[name]:
    sum2 += deg
  print("{} : {:.1f}".format(name,sum2/3))


# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")

# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
print(city['서울'])
if 2 in city['서울']:
    print("네")
else:
    print("아니요")

  
      

```



**dict.py** - 강사님 코드

```python
"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

print("=========================Q1=========================")
# 1
total_score = 0
count = 0 
for score in iu_score:
    #print(iu_score[score])
    total_score += iu_score[score]
    count += 1
#print(total_score/count)
        # 검색 : python get values in dict, python get sum of list, python get length of list 
# 2
scores = list(iu_score.values())
print(sum(scores)/len(scores))


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 110
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=========================Q2=========================")
for cl in score:
    #print(score[cl])
    tmp = list(score[cl].values())
    print("{} : {:.1f}".format(cl, sum(tmp)/len(tmp)))

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -12, 2],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 14],
    "부산": [2, -2, 9],
}

# 답변 코드는 아래에 작성해주세요.
print("=========================Q3========================")
for name in city:
    #print(cities[city])
    temp = city[name]
    print("{}의 평균기온 : {:.1f}".format(name, sum(temp)/len(temp)))

    
# 답변 코드는 아래에 작성해주세요.
print("=========================Q3-1======================")

ht = ["도시", 0]
lt = ["도시", 0]
for name in city:
    for temp in city[name]:
        if(ht[1] < temp):
            ht[0] = name
            ht[1] = temp
        elif(lt[1] > temp):
            lt[0] = name
            lt[1] = temp
print("최고 = {} : {},  최저 = {} : {}".format(ht[0], ht[1], lt[0], lt[1]))


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=========================Q4========================")
if 2 in city['서울']:
    print("네")
else:
    print("아니요")


```







- git 코드 올리기

  github - new repository 

  ![1545208607034](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545208607034.png)

![1545208751848](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1545208751848.png)







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

------

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





































