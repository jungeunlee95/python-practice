import requests
import json
import os 
from pprint import pprint as pp
import csv
date2 = ["20181111","20181118","20181125","20181202","20181209","20181216","20181223","20181230","20190106","20190113"]
movie_key = os.getenv('MOVIE_TOKEN')
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
movie_list = []
for targetDt in date2 : 
    params = {
        'key': movie_key,
        'targetDt':targetDt,
        'weekGb':"0"
    }
    res = requests.get(url, params=params).text
    document = json.loads(res)
    movie_info = document['boxOfficeResult']['weeklyBoxOfficeList']
    for i in movie_info:
        b = {"movie_code" : i["movieCd"], "title" : i["movieNm"], 
              "audience": int(i["audiAcc"]), "recorded_at" : document['boxOfficeResult']['showRange'].split("~")[1]}
        movie_list.append(b)

check = []    

# 누적 관객 수로 정렬
movie_list = sorted(movie_list, key=lambda k: k['해당일누적관객수']) 

with open('boxoffice.csv','a') as f:
    field = ("영화대표코드", "영화명", "해당일누적관객수", "해당일")
    writer = csv.DictWriter(f, fieldnames=field)
    writer.writeheader()
    
    for movie in movie_list:
        if(movie["영화명"] not in check):
            writer.writerow(movie)
            check.append(movie["영화명"])
        #### 여기에 관객수 더 크면 넣어주는 코드 작성해야해!!!!!

# 영화 대표 코드 movieCd , 영화명 movieNm, 해당일 누적관색수 audiAcc, 해당일 showRange
# 해당일 누적관객수 중복 -> 최신정보 반영