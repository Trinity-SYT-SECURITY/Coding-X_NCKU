# 讀取台灣彩卷的大樂透號碼
import requests
import bs4  # BeautifulSoup

#url = "http://tqc.codejudger.com:3000/target/5203.html"
url = "https://www.taiwanlottery.com.tw/index_new.aspx"  # 開啟的網址
html = requests.get(url)  # 取得網頁
# 轉換成bs4格式
objSoup = bs4.BeautifulSoup(html.text, 'lxml')  # 網頁html=>bs4格式
dataTag = objSoup.select('.contents_box02')  # 取出contents_box02的區域的網頁
# 威力彩區
balls = dataTag[2].find_all(
    'div', {'class': 'ball_tx ball_yellow'})  # 取得大樂透的號碼=>balls[]
# 輸出結果
print('大樂透開獎  :')
print("開出順序: ", end='')
for i in range(6):
    print(balls[i].text, end=' ')

print("\n大小順序: ", end='')
for i in range(6, len(balls)):
    print(balls[i].text, end=' ')

redball = dataTag[2].find_all('div', {'class': 'ball_red'})  # 取得大樂透的特別號
print("\n特別號: ", redball[0].text)
# 威力彩區
balls = dataTag[0].find_all(
    'div', {'class': 'ball_tx ball_green'})  # 取得威力彩的號碼=>balls[]
# 輸出結果
print('威力彩開獎  :')
print("開出順序: ", end='')
for i in range(6):
    print(balls[i].text, end=' ')

print("\n大小順序: ", end='')
for i in range(6, len(balls)):
    print(balls[i].text, end=' ')

redball = dataTag[0].find_all('div', {'class': 'ball_red'})  # 取得大樂透的特別號
print("\n特別號: ", redball[0].text)
