import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/'
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all('div', class_='title')     # 取得 class 為 title 的 div 內容
count = 0;
for i in titles:
    if i.find('a') != None:                         # 判斷如果不為 None
        if i.find('a', attrs={'class": "btn wide'}) != None:
            link = i.find('a', attrs={'class": "btn wide'}).get_text()
            web2 = requests.get(link, cookies={'over18':'1'})
            soup2 = BeautifulSoup(web2.text, "html.parser")
            titles2 = soup2.find_all('div', class_='title') 
            for i2 in titles2:
                if i2.find('a') != None:  
                    print(i2.find('a').get_text())                 # 取得 div 裡 a 的內容，使用 get_text() 取得文字
                    print(url + i2.find('a')['href'], end='\n\n')  # 使用 ['href'] 取得 href 的屬性
        print(i.find('a').get_text())                 # 取得 div 裡 a 的內容，使用 get_text() 取得文字
        print(url + i.find('a')['href'], end='\n\n')  # 使用 ['href'] 取得 href 的屬性
        count = count + 1


print('共' + str(count) + '筆')
