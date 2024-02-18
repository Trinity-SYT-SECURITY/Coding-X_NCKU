"""
09-02 資料加總
請以一程式，讀取read.txt的內容(內容為數字，以空白分隔)並將這
些數字加總，再顯示檔案內容和加總的結果，檔案讀取完成後要關閉。
read.txt
11 22 33 22 33 44 33 44 55 44 55 66 55 66 77

例: =>660
"""

"""f = open("C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\read.txt", "r")
data = f.read()
print("read.txt", data)
f.close()

numlist = data.split(' ')
print("分割完成=>", numlist)
numsum = 0
for i in range(len(numlist)):
    numsum += eval(numlist[i])
    
print("doc read.txt sum of number :" ,numsum)
print("doc read.txt all digital average  :" ,(numsum/len(numlist)))
"""
# 讀取檔案，並資料加總
# 開啟檔案
# 開啟檔案並讀檔
import bs4  # BeautifulSoup
import re
import requests
from base64 import encode
f = open(
    "C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\read.txt", "r")
data = f.read()  # 將檔案讀取資料=>data
print("read.txt=>", data)  # 測試所讀出的資料
f.close()  # 關閉檔案
# 處理已讀出的資料data，將每筆整數資料加總
numsLst = data.split(' ')  # 利用空白來分割split字串成為數字串列=>numsLst
print("已分割的data=>", numsLst)
numsSum = 0  # 所有資料的總和
# for i in range(len(numsLst)): #i 為 numsLst 的索引值
# numsSum += eval(numsLst[i]) #以i為索引處理
for i in numsLst:  # i 為 numLst的元素
    numsSum += eval(i)  # i 為元素的加總
# 輸出結果
print("檔案read.txt所有數字加總:", numsSum)
print("檔案read.txt所有數字的平均值:", (numsSum/len(numsLst)))
"""
已分割的data=> ['11', '22', '33', '22', '33', '44', '33', '44', '55', '44', '55', '66', '55', '66', '77\n']
檔案read.txt所有數字加總: 660
檔案read.txt所有數字的平均值: 44.0
"""


"""
09-04 資料計算
請以一程式，讀取read2.txt的內容(美一列的格式為名字及身高、體重，以空白分隔)並顯示所有人的平均身高，平均體重以及最高者，最重者。提示:輸出浮點數到小數點後第二位。
read2.txt
Ben 175 65
Cathy 155 55
Tony 172 75

例: =>
Ben 175 65
Cathy 155 55
Tony 172 75
Average height: 167.33
Average weight: 65.00
The tallest is Ben with 175.00cm
The heaviest is Tony with 75.00kg
"""
# 資料讀取與計算
# 建立三個List =>檔案中的姓名，身高，體重
name = []  # 姓名
height = []  # 身高
weight = []  # 體重
with open('C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\read2.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        tmp = line.strip('\n').split(' ')  # 一行分割=>tmp[]
        # tmp[]=>name, height, weight 一次讀一行
        name.append(tmp[0])  # 從第一行的第一個讀
        height.append(eval(tmp[1]))
        weight.append(eval(tmp[2]))
    print(name)
    print(height)
    print(weight)
print("平均身高:%.2f" % (sum(height)/len(height)))
print("平均身高:%.2f" % (sum(weight)/len(weight)))
max_h = max(height)
max_w = max(weight)
mh_name = name[height.index(max_h)]
mw_name = name[weight.index(max_w)]
print('最高的人是 %s 其身高為 %.2f 公分' % (mh_name, max_h))
print('最重的人是 %s 其體重為 %.2f 公斤' % (mw_name, max_w))
"""
['Ben', 'Cathy', 'Tony']
[175, 155, 172]
[65, 55, 75]
平均身高:167.33
平均身高:65.00
最高的人是 Ben 其身高為 175.00 公分
最重的人是 Tony 其體重為 75.00 公斤
"""


"""
09-06 字串資料取代
請以一程式，要求使用者輸入檔名data3.txt、字串s1及字串s2。
程式將檔案中的字串以s1以s2取代之。
data3.txt
watch shoes skirt
pen trunks pants
例: data3.txt
pen
sneakers
=>
=== Before the replacement

watch shoes skirt

pen trunks pants

=== After the replacement

watch shoes skirt

sneakers trunks pants
"""


# 檔案資料讀取與取代後寫入
f_name = input("請輸入將讀取的檔名:")  # 檔名:data3.txt
s_old = input("請輸入將被取代的原字串:")  # 舊字串<=將被取代的字串
s_new = input("請輸入將取代的新字串:")  # 新字串
# 開啟檔案->in_f，讀檔=>data
in_f = open(
    'C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\'+f_name, "r")
data = in_f.read()  # 將所有檔案中的資料讀取=>data
# 顯示未取代前的資料
print('==未取代前的資料:')
print(data)
in_f.close()  # 關閉檔案
# 將舊字串由新字串取代=>顯示取代後的資料
new_data = data.replace(s_old, s_new)  # 將舊字串由新字串取代=>new_data
print('==取代後的資料:')
print(new_data)
# 取代後的資料寫入到檔案中
out_f = open(
    'C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\'+f_name, "w")
out_f.write(new_data)  # 寫入到檔案中，從頭寫起(覆蓋)
out_f.close()  # 關閉檔案
"""
請輸入將讀取的檔名:data3.txt
請輸入將被取代的原字串:pen
請輸入將取代的新字串:meow
==未取代前的資料:
watch shoes skirt
pen trunks pants

==取代後的資料:
watch shoes skirt
meow trunks pants
"""

"""
09-10 學生基本資料
請以一程式，要求使用者輸入檔名read4.txt(以UTF-8編碼之二進為檔)、第一
列為欄位名稱，第二列為個人紀錄。請輸出檔案內容並顯示男生人數及女
生人數(性別欄位，0為女性，1為男性)。
read4.txt
學號 姓名 性別 科系
101 陳小華 0 餐旅管理
202 李小安 1 廣告
303 張小威 1 英文
404 羅小美 0 法文
505 陳小凱 1 日文
例:
=>
學號 姓名 性別 科系

101 陳小華 0 餐旅管理

202 李小安 1 廣告

303 張小威 1 英文

404 羅小美 0 法文

505 陳小凱 1 日文

Number of males:  3
Number of females:  2
"""

inp = input("輸入讀取檔名:")
# with open('C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\read2.txt', 'r', encoding='UTF-8') as f:
opendoc = open(
    'C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\'+inp, 'r', encoding='UTF-8-sig')
#data = opendoc.read()
# print(data)
males = 0
females = 0
with opendoc as f:

    for line in f:
        tmp = line.strip('\n').split(' ')  # 一行分割=>tmp[]
        # tmp[]=>name, height, weight 一次讀一行
#        height.append(eval(tmp[1]))

        if tmp[2] == '1':
            males += 1
        elif tmp[2] == '0':
            females += 1

print("男性人數:", males)
print("女性人數:", females)

"""
輸入讀取檔名:read4.txt
男性人數: 3
女性人數: 2
"""

"""
201 TQC+ 網頁資料擷取與分析 Python 3 _ 201 搜尋字詞

說明：

請撰寫一程式，爬取http://tqc.codejudger.com:3000/target/5201.html，
程式須回傳下列資訊： 讓使用者輸入欲搜尋的字詞，再輸出字詞的搜尋結果及字詞出現的次數。
範例輸入： 請輸入欲搜尋的字串 : TQC+

範例輸出：
TQC+ 搜尋成功
TQC+ 出現 23 次
"""

# 取得網頁=>doc
inp = input("請輸入欲搜尋字串:")
doc = requests.get("http://tqc.codejudger.com:3000/target/5201.html")
# print(doc.text)
coun = re.findall(inp, doc.text)
print(coun)

if len(coun) > 0:
    print(inp, "搜尋成功")
    print(inp, "出現", len(coun), "次")
else:
    print(inp, "搜尋失敗")


"""
請輸入欲搜尋字串:TQC+
['TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC', 'TQC']
TQC+ 搜尋成功
TQC+ 出現 23 次
"""

"""
203 TQC+ 網頁資料擷取與分析 Python 3 _ 203 台灣彩券 請撰寫一程式，爬取http://tqc.codejudger.com:3000/target/5203.html
，程式須回傳下列資訊：
大樂透的開出順序
大樂透的大小順序
大樂透的特別號

範例輸出：

大樂透開獎 :
開出順序 : 44 25 18 14 16 23
大小順序 : 14 16 18 23 25 44
特別號 : 41

"""

# 讀取台灣彩卷的大樂透號碼

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

""" 
大樂透開獎  :
開出順序: 41  40  09  29  16  23  
大小順序: 09  16  23  29  40  41  
特別號:  43 
威力彩開獎  :
開出順序: 17  10  33  15  07  30  
大小順序: 07  10  15  17  30  33  
特別號:  08 
"""
