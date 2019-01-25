from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
import time
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/lotto')
def lotto():
    return render_template('lotto.html')
    
    
@app.route('/toon')
def toon():
    cat = request.args.get('type') 
    today = time.strftime("%a").lower()
    
    if(cat == 'naver'):
        #print(request.args.get('type'))   
        
        naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=' + today
        response = requests.get(naver_url).text
        soup = bs(response, 'html.parser')
    
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
          
    elif(cat == 'daum') :
        # 1. 내가 원하는 정보를 얻을 수 있는 주소를 url 변수에 담는다.
        # 2. 해당 url에 요청을 보내 응답을 받아 저장한다.
        # 3. python으로 json을 파싱(딕셔너리 형으로 변환)해 가져오는 법
        
        url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{}?timeStamp=1545117404316'.format(today)
        response = requests.get(url).text
        #print(response)
        document = json.loads(response)
        
        data = document["data"]
        
        toons = []
        for toon in data:
            toons.append({
                "title" : toon["title"],
                "url" : "http://webtoon.daum.net/webtoon/view/{}".format(toon["nickname"]),
                "img_url" : toon["pcThumbnailImage"]["url"]
            })
            
        #print(toons)
    
    return render_template('toon.html', cat = cat, t = toons)
    
    
    
# @app.route('/apart')
# def apart():
#     # 1. 내가 원하는 정보를 얻을 수 있는 url을 url변수에 저장한다.
#     url = 'http://rt.molit.go.kr/new/gis/getDanjiInfoDetail.do?menuGubun=A&p_apt_code=724&p_house_cd=1&p_acc_year=2018&areaCode=&priceCode='
    
#     # 1-1 request header에 추가할 정보를 dictionary 형태로 저장한다.
#     headers = {
#         "Host": "rt.molit.go.kr",
#         "Referer": "http://rt.molit.go.kr/new/gis/srh.do?menuGubun=A&gubunCode=LAND"
#     }
    
#     # 2. requests의 get 기능을 이용해 해당 url에 header와 함께 요청을 보낸다.
#     response = requests.get(url, headers=headers).text
#     print(response)
#     # 3. 응답으로 온 코드의 형태를 살펴본다 (json, xml,html)
#     document = json.loads(response)
#     apartInfo = []
#     for dddd in document["result"]:
#         apartInfo.append({
#             "location" : dddd["JIBUN_NAME"],
#             "apart_name" : dddd["BLDG_NM"],
#             "apart_size" : dddd["BLDG_AREA"],
#             "apart_cost" : dddd["SUM_AMT"],
#             "month" : dddd["DEAL_MM"],
#             "date" : dddd["DEAL_DD"]
#         })
    
#     return render_template('/apart.html', t = apartInfo)

@app.route('/exchange')
def exchange():
    url = 'http://info.finance.naver.com/marketindex/exchangeList.nhn'
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    print(soup)
    soup = soup.find_all("td", {"class":{"tit", "sale"}})
    
    exchanges=[]
    for i in range(88):
        if(i == 0 or i % 2 == 0):
            exchange = {
                "con" : soup[i].text
            }
        else :
            exchange = {
                "cost" : soup[i].text
            }
        exchanges.append(exchange) 
    print(exchanges)
    
    return render_template('exchange.html', t = exchanges)
    
    #dasd