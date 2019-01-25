# 인식시킬 사진을 Clova API를 통해 요청을 보내, 인식 결과를 받아온다.
# req(파일)   : 파일 데이터 전송 

# 1. requests를 통해 Clova API 주소에 요청을 보낸다.
# 2. 응답 받은 json을 파싱하여 원하는 결과를 출력한다.

import requests
import os 
from pprint import pprint as pp

naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_SECRET')

url = "https://openapi.naver.com/v1/vision/celebrity"

headers = {
    'X-Naver-Client-Id': naver_id ,
    'X-Naver-Client-Secret': naver_secret
}   

# 1. 해당하는 image_url에 요청을 보낸다\
image_url = "http://www.kbstve.com/news/photo/201604/681_616_1746.jpg"
image_res = requests.get(image_url, stream=True)  # 옵션 아는 법 google : python requests 문서 찾아보기
# print(image_res.raw.read())

# 2. 파일 데이터를 받아 저장해둔다
files = {
    'image': open('ho.jpg', 'rb')   # open : 파일을 열때 쓰는 함수 = image에 파일을 넣어줌
    #'image' : image_res.raw.read()
}

res = requests.post(url, headers=headers, files=files)
result = res.json()

name = result['faces'][0]['celebrity']['value']
percent =  round(result['faces'][0]['celebrity']['confidence']*100)

print("닮은 연예인은 {}입니다.\n{}% 확신할 수 있습니다.".format(name,percent))





