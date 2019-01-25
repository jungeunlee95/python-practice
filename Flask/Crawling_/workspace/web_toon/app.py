from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("Nice To Meet You")
    return """
           <h1>얘 귀엽다.</h1>
           <img src = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIALoAiwMBIgACEQEDEQH/xAAbAAABBQEBAAAAAAAAAAAAAAADAAIEBQYBB//EADsQAAICAQMCAwUFBgQHAAAAAAECAAMRBBIhBTEiQVEGEzJhcVKBkaHRFSMzQrHBBxQl4SQ1YnJzgvD/xAAYAQADAQEAAAAAAAAAAAAAAAAAAQIDBP/EAB0RAQEBAQEAAgMAAAAAAAAAAAABEQIxEkEDITL/2gAMAwEAAhEDEQA/APcYoooAooooAooooAoooj2gELqDcYmd1TcnEuOo2+IgSi1B5PMVVEG5pGcZGYe0iRLX7zOrgVjASLY+Y+1pGdpJg2895HIhrDmCMRhkRhEIY2Ae7RTgOe07OhgUUUUAUUUUAUFfYK6ySYrrlqXJIz6Sj6hry54OIAPW6hc4Xue8p77c5A/GP1F/JJMr7bpFq3LX+ciWvO2WcyNY8iqhjtAO3Mc7QLGIzWMGZ1jGExGRjTETOZgHsGj1+BgnIljXqa3/AJgJj6dRiSk1RE21neWq3D1EW4eomb/aBAxkwba9/tQ0saZrq1+JxIOp6kqZFf4yhs1zH+aRbtSTFoxO1evLZJaVN+q3ecBbdmRnsi08Fsuz5yK9kY1kC7xGc7wDtEzQTGSbjNBMZ1mgyYjImMMRMaTAOkxpM4TGkwNt63wO8KLvnICvHh5olMNvzg2u+cjGyMZ4EkG4+sE9vzgC/p5xtq2J8aMOcZxxFpOvZ84B3jWaCZ4GczcwTNGs0YTECZo1VaxtqDJx2jWaZz2j6gbX/ZtDEKebiOAw8l+kQaHwPWz1W1WhW2t7tw2D90CzSp9nq2TWjaBsdCjj1B7fmFP3SyLfjEeOkxpM4TGkwPXSY3M4TGk8wLWtDYnfeQG6cLSwMXjGsgS0Yz4gSXo3/wCMqz9oS16jpVqQOp8pnUu2Wo/2SD+c1mqcanTBB3C8zL8lzGnE1mLR3A74zt/SRWaA68lqqTS5SxOVYeRgdJrV1dC24CN/Omex/TvK4uxPfOVJZowvGlxkjI4kTU6/TacZtuQc4+ISsQfr9UNJo7dQe1a5H18vzmQ01bte1tzFnJ8/P1P45lv1TW1aytK9OTYocu2O3Hr92T+Eq9Nem8Acj+YnzMLFcrTR6kae6o453Ann08pb3+G11BOAxxmZprhbqRtPhUYl+5OeTmTFdOkxpMYXxG7iYIPLRm+NJjMwNrSYwtHGCYxgi8EzRMYJjGRxaW2m6k9dSuBnC5YfaHnKQtFfey9PsC5yGByByv0kd87F/j6yh+0/VtMoNqDCnsf9piG6lapd9OzV85Vj554I/wDvnO9c1p1D7Ub91nAOO5kOjTtqERd3Kurdu+PKPjnIO+vlVnUmrNtlOo1FrWModWVsZyD3E1On6B07U9L0S3Ba7FYNc2MlgM5EqOlaQvqn1NxOVwol0WbZwe0v5I+LO9Z0NGi1mpopTZQyhq8E9vP+gmfLCnLV2sSR8PfJmg9qdb7miskb7WO1VmPruvtYsjrlc+HyMfpeL3puqVdSucYPDDE0+/eAwPBEwKJdaouTbWvf0zLnofU33e4vOAPCCfWTYetITiMLTm7iMLRB0tGlo1mgy0A2rQLmGeAeBhOYJjHuZHdsQDpMuer9F/y3s17t2ZNRq03ZUfCp7DmVXTQbOoaatQGZrAAD27zW+2tvvOoFAfCigDHYSp4X28G6x0zUdPZEsZvclsBzK/Te8W9vdWMmz4SDPU9bpq7VZLFDI3dSMgyjb2f0CMWSjaPQE4MPkd5Sej6v3/TaLWxuK+LHr5yxpuVvCSOZVabSJo9Oy1AqpYtgduYWrV1ISpIziCpNiv8Aafp+p1Gs0x0tRtAV88gY7YlPpPZvXvcd9fuEbuWIJH0Am70pFtQZSCMd4XAHpC1GMrqegWlNmmP7sLgDtA19DvrZGRSSPiM2asMEER9e0nsMRadjP2V2UBVtzuxAl5b9frASt1GPLiUZMCOZozdGlvnGboB6A4ka04kmy+tX2Al7D2RBuMidSo1yaRrkrrqb+VG5c/2ElSNY8ju0AuqF1at2zEXlEtfZytr+uaNVXIFoOSOOOZde0Vh/aVwYjIY8TO9DuFPUaLSpIVx2Uf1MvuugHVM5VRu5yvOfvjv8lPVVYiuOO8h2147wrXAN2Pedt2uNwzIaK/WU2W0FdOyq3nu7GZ68ahN9Viqt5yFZQcfIzVdpS9VvQ3odu5kORiNXPWJ/SdMuiq3WuXub4nMnFlc8MMyr0uvRxjcUPo0sKrGLfGfwgzvoloZFXPJPnO0ucjGPxgr394wwwO2doGWBPHyiB/V1ZtF9DkzLs5+Q+6a3qTf6fZ9Jjy+RnaMfLmUki588GN3/AEjWI8/yMZ/7CBPYdDptNShXT1DAbaSq9z9ZW9Zs95bhPgU4HpNFq8abTYXG5uF+QmN9ptY2kpro04BusPvGyM7UH6mCvVBrKzpdUXyFqtPOeyt/vG+8VT4U3H1b9JIvKa7Tk87XHn3BlVW7KzU2Hxp+Y8jGE73rsQXbwj17TX3X16zp9D1BcIoXw9sTDbvXknsJteiaU0+zj6jUL/FfwHP9oewfanvHiOJH9/sOAeIXWM3ITgSBZu8hM1i3WtcNiMAT5yKdIig+ZHmYNxaDkDEEX1IHC5EAlmmru4GD5+kdU+HCUEtAUad7CBbbn1QQ+P8ALX+A4rP5Rkm16W1/iQ5hq1ZW2kfjC6S4nGTmTTUlg3A4MAi6yhrtBaqjJx2MxFi7XIB5HlmejVLjvMX7S9P/AMrrWdFIWw7gT2J/tKiaqN+Zw4PnGs2Sd3B9YMk5jS9u6hqN97M5C1ICST2CjvMBR1EdV6hr9UUwNwCkngJ2AH4TS+1d7LTV06k4v1nNmO61D9f7TN9I6UmkR6LGYrks7HuQO2YuquRDydFqivai08f9JgupU4UalFy6fy/aHpJmop97U9bg4B+IyJpri6NVaP3lfhwYQVzp9D62+pK8s9p+8Z9PnPUet6ddH0jS6NQVFVYXae/bz+cy/wDhj0pv25bq7a91KAsnn4jNT7Uajdayuw79sy/In2sNqANxxIrLJ2oA3GRSJjWgDADuI0qvYgYkjaD3E7gekDNXS0sp8IVvIjvB0qSTTackHwsfOTEVR8X4xmpo3OGU4A7GBH0HaeMy007eHmV1G5cCxefUSXW2DHCT1xIfW9Cmu0TofiUZUw6PxDZBHPaVCx5XcGVyrDBHeC3Y4yZce1GibSa9mGPducjEo959Y0vSKrn6jrdT1OwYNp2VD7KDyg9TY9aWbPhf4xjkwuqsTSaTanAA2LIGn1XvkwTlx+cjWuHaz93RVSeGANj/APcefyGBKXVKd66irg1/ECM8S3tZtTqBvPNj5b+p/pG6bTDWamzHBawLgH4ic/pHPUVvv8OdP/pd+tsB22YC5HaQ/aDN17Pkkepmi01VXSuiJpK8AIgGB5mY7q+osssKngCadeFzFJcfEfSBzCW94EHnmYtI7nBjj3jSMn1nCcHmIxc5HJjkYE7T5SPlkX1EDZbZv3LyoGePSIlshV+IULxwZDocMu4GSa7OZUKpSN4fniER+IJWXueBHqQewlwlB7ZbG0leQN+ePXExP1OPlibb2yQHpiucgh+CJhiTmUit11PU+8sPHgU7R/cyJWfdbmHw54IndT/D++No5rP0Myb7g4tFyblOD5/KaT2N6e92opuKr7qrNrnb3PZRn7pj+mfG33f1npvsYoHRbsAD95L49Z9/qrHqjlqyM/eZktflmziajqP8IDymW6h2ldlyqbcEmAYA94Vu0EZkuEp2g+kH7+q0siuN3pCH4ZR6wka6og4OfKI1rS7C1qn7DlT6wqJhvlGJ/EWGXv8AfEBhWNpGOJ1SEUADmP8AI/SNHcSiPFdj4JsA+Qk6hWUYJBkdZJXtKiVZ7U1b+j2YGcEGecknJ+s9O65/yjVf+Mzzez4zNEV//9k=">
           """
    
@app.route('/naver_toon')
def naver_toon():
    today = time.strftime("%a").lower()
    
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
        "img_urgigl" : item.select('.thumb img')[0]["src"]
      }
      toons.append(toon)     
      
      
    return render_template('naver_toon.html', t = toons)
      
      
@app.route('/daum_toon')
def daum_toon():
    
    return render_template('naver_toon.html')