import requests
import json
import os 
import urllib
import csv

naver_id = os.getenv('NAVER_MOVIE_ID')
naver_pw = os.getenv('NAVER_MOVIE_PW')

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


# ----------------------------------------영화 상세 ----------------------------------------
movie_c = list(movie_d.keys())

url_base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
movieinfo = [ ]
for c in movie_c:
    params = {
        'key': movie_key,
        'movieCd' : c
    }
    res = requests.get(url_base, params=params)
    movieinfo.append(res.json().get('movieInfoResult').get('movieInfo'))
    
info_d = []
for m in movieinfo:
  li = [m.get('movieCd'),m.get('movieNm'),m.get('movieNmEn'),m.get('movieNmOg'),
        m.get('openDt')[:4],m.get('openDt')[4:6],m.get('showTm'),'/'.join([g.get('genreNm') for g in m.get('genres')]),
        m.get('directors')[0].get('peopleNm'),m.get('audits')[0].get('watchGradeNm')]
  actors = m.get('actors')
  if len(actors) < 3:
    li.extend([actors[i].get('peopleNm') for i in range(len(actors))])
    li.extend([''*(3-len(actors))])
  else:
    li.extend([actors[i].get('peopleNm') for i in range(3)])
  info_d.append(li)
  
with open('movie.csv','w') as f2:
  fields = ()
  boxoffice = csv.writer(f2)
  boxoffice.writerow(['movieCd','movieNm','movieNmEn','movieNmOg','openY','openM','showTm',
                      'genre','director','watchGrade','actor1','actor2','actor3'])
  for li in info_d:
    boxoffice.writerow(li)
    
with open('movie.csv',newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)

# ------------------------------------네이버 api --------------------------------------
movie_nc = {}
for info in movieinfo:
    movie_nc[info.get('movieNm')] = info.get('movieCd')
# print(movie_nc)

header = {
    'X-Naver-Client-Id' : naver_id,
    'X-Naver-Client-Secret' : naver_pw
}

url_base = 'https://openapi.naver.com/v1/search/movie.json?'
nmovie = []
for name in movie_nc:
  url_sub = "query={}".format(name)
  res = requests.get(url_base + url_sub, headers = header)
  nmovie.append(res.json().get('items'))
 
movie_l = list(movie_nc.values())
movie_data = []
for i in range(len(nmovie)):
  m = nmovie[i][0]
  movie_data.append([movie_l[i],m.get('image'),m.get('link'),m.get('userRating')])
  
with open('movie_naver.csv','w') as f1:
  mnaver = csv.writer(f1)
  mnaver.writerow(['movieCd', 'movieInk', 'movieImg', 'userRat'])
  for li in movie_data:
      mnaver.writerow(li)
f = open('movie_naver.csv','r')
# print(f.read())
f.close()

for img in movie_data:
    with open("images/{}.jpg".format(img[0]),'wb') as f3:
        imgdata = requests.get(img[1]).content
        print("@@@", imgdata)
        f3.write(imgdata)