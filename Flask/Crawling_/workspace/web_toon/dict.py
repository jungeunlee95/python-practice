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

  
      