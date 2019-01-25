import random
menu = ["순남시래기","20층","양자강","강남목장","시골집","몰라"]
menu_detail = {"순남시래기" : "시래기국, 보쌈", "20층" : "오늘메뉴",
               "양자강" : "차돌짬뽕", "강남목장" : "뚝불",
               "시골집" : "쌈밥정식", "몰라" : "아무거나"}
# () brackets
# {} curly brackets 
# [] square brackets 
# <> angle brackets 
lunch = random.choice(menu)
print(lunch + "에서는 " + menu_detail[lunch] + "이(가) 먹을만 합니다.")