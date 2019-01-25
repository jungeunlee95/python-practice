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
        
    return theme_list


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
    
    # print(cafe_list)
    return cafe_list
    
# 사용자로부터 '마스터키 ****점'이라는 메세지를 받으면,
print(master_key_info("강남점"))

# 해당 지점에 대한 오늘의 정보를 요청(크롤링)하고, 
# 메세지(예약정보)를 return한다.
for cafe in master_key_list():
    print('{} : {}'.format(cafe["title"], cafe["link"].split('=')[1]))
    
