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
                'title' : book["branch"],
                'time' : book["hour"],
                'room' : book["room"],
                'booked' : booked
            }   
            CAFE_LIST.append(cafe)
            #print("{} - {} : {} = {} ".format(book["branch"],book["hour"], book["room"], booked))
    #print(CAFE_LIST)
    return CAFE_LIST

seoul_escape_list("홍대2호점")


