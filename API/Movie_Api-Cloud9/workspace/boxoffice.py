import requests
import json
import os 
from pprint import pprint as pp
import csv

date = ["20181111","20181118","20181125","20181202","20181209","20181216","20181223","20181230","20190106","20190113"]
movie_key = os.getenv('MOVIE_TOKEN')
movies = [ ]
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'

for d in date:
    params = {
        'key': movie_key,
        'targetDt':d,
        'weekGb':"0"
    }
    res = requests.get(url, params=params)
    movies.append(res.json().get('boxOfficeResult').get('weeklyBoxOfficeList'))
    

movie_d = {}
for i in range(len(movies)):
  for m in movies[i]:
      movie_d[m.get('movieCd')] = [m.get('movieCd'),m.get('movieNm'),m.get('audiAcc'),date[i]]

movie_l = list(movie_d.values())
# print(len(movie_l))

with open('boxoffice.csv','w') as f1:
  boxoffice = csv.writer(f1)
  boxoffice.writerow(['movieCd', 'movieNm', 'audiAcc', 'recordDt'])
  for li in movie_l:
    boxoffice.writerow(li)
    
f = open('boxoffice.csv','r')
print(len(f.read()))
f.close()   