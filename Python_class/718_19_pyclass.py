

import random
totali = 0  # 總和
for i in range(1, 11):
    print(i)  # 目前的i值
    totali += i  # totali = totali + i =>將i值加入到總和
print("上述總和:", totali)  # 輸出總和


# 03-04 迴圈倍數總和
numa = eval(input("請輸入一整數a(迴圈的終值):"))
totala = 0  # 總和
print("1到%d的5的倍數有" % (numa), end=":")  # 開頭的顯示
# for i in range(1, numa+1): #1,2,...numa
#  if i % 5 == 0: #當前i值可被5整除=5的倍數
for i in range(5, numa+1, 5):  # 5,10,...最後5的倍數
    print(i, end=" ")
    totala += i  # 加入到總和
print("的總和為:%d" % (totala))
"""
1到20的5的倍數有:5 10 15 20 的總和為:50
"""

# 巢狀迴圈
for i in range(2):
    for j in range(3):
        print(i*j)
"""
0
0
0
0
1
2
"""

for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j, end="\t")  # 輸出結果
    print()
"""
1 * 1 = 1       1 * 2 = 2       1 * 3 = 3       1 * 4 = 4       1 * 5 = 5    1 * 6 = 6        1 * 7 = 7       1 * 8 = 8       1 * 9 = 9
2 * 1 = 2       2 * 2 = 4       2 * 3 = 6       2 * 4 = 8       2 * 5 = 10   2 * 6 = 12       2 * 7 = 14      2 * 8 = 16      2 * 9 = 18
3 * 1 = 3       3 * 2 = 6       3 * 3 = 9       3 * 4 = 12      3 * 5 = 15   3 * 6 = 18       3 * 7 = 21      3 * 8 = 24      3 * 9 = 27
4 * 1 = 4       4 * 2 = 8       4 * 3 = 12      4 * 4 = 16      4 * 5 = 20   4 * 6 = 24       4 * 7 = 28      4 * 8 = 32      4 * 9 = 36
5 * 1 = 5       5 * 2 = 10      5 * 3 = 15      5 * 4 = 20      5 * 5 = 25   5 * 6 = 30       5 * 7 = 35      5 * 8 = 40      5 * 9 = 45
6 * 1 = 6       6 * 2 = 12      6 * 3 = 18      6 * 4 = 24      6 * 5 = 30   6 * 6 = 36       6 * 7 = 42      6 * 8 = 48      6 * 9 = 54
7 * 1 = 7       7 * 2 = 14      7 * 3 = 21      7 * 4 = 28      7 * 5 = 35   7 * 6 = 42       7 * 7 = 49      7 * 8 = 56      7 * 9 = 63
8 * 1 = 8       8 * 2 = 16      8 * 3 = 24      8 * 4 = 32      8 * 5 = 40   8 * 6 = 48       8 * 7 = 56      8 * 8 = 64      8 * 9 = 72
9 * 1 = 9       9 * 2 = 18      9 * 3 = 27      9 * 4 = 36      9 * 5 = 45   9 * 6 = 54       9 * 7 = 63      9 * 8 = 72      9 * 9 = 81
"""

# 繪製直角三角形
# *  i=1, j=1
# ** i=2, j=1,2
# *** i=3, j=1,2,3
# **** i=4, j=1,2,3,4
"""
*
**
***
"""

test = eval(input("想要多少 * :"))
for i in range(1, 1+test):
    for j in range(1, i+1):
        print("*", end="")
    print()
"""
想要多少 * :10
*
**
***
****
*****
******
*******
********
*********
**********
"""
# break命令例
for i in range(1, 11):  # [1, 2, 3,...,10]<=原本i 的過程
    if i == 6:
        break  # 只要迴圈i =6將中途結束=>1-5的輸出而已
    else:
        print(i)

"""
1
2
3
4
5
"""

# continue
for i in range(1, 11):  # [1, 2, 3,...,10]<=原本i 的過程
    if i == 6:
        continue  # 只要迴圈i =6將跳過，7後繼續=>1-5，7-10的輸出而已
    else:
        print(i)
"""
1
2
3
4
5
7
8
9
10
"""

# 列出1~50間的所有偶數整數，使用continue
for i in range(1, 51):
    if (i % 2 != 0):
        continue
    else:
        print(i, end=" ")
"""
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 
"""


# 以while來處理由使用者輸入的迴圈整數連加
numa = eval(input())  # 第一個整數
numb = eval(input())  # 最後一個整數
totali = 0  # 總和
i = numa  # 迴圈的初值
while i <= numb:  # 迴圈的終值，條件計數器<=b
    totali += i  # 迴圈區段
    i += 1  # i=i+1

# 輸出結果
print("%d +...+%d = %d" % (numa, numb, totali))
"""
10
100
10 +...+100 = 5005
"""

num = random.randint(1, 100)  # 產生1~100間的整數
if num % 2 == 0:
    print("num=", num, "是偶數")
else:
    print("num=", num, "是奇數")
"""
num= 15 是奇數
num= 31 是奇數
num= 18 是偶數
...
"""

# 以random來擲骰子，直到點數出現4為止，顯示總共擲了多少次?
# 擲骰子
diceno = random.randint(1, 6)  # 產生骰子點數1-6
t = 1  # 擲骰子的次數
print("第%d次，目前點數:%d" % (t, diceno))
while diceno != 4:  # 當點數不是4時，將繼續擲下一次的骰子，只有4點才回停止
    # 再擲骰子
    diceno = random.randint(1, 6)  # 產生骰子點數1-6
    t += 1  # 次數+1
    print("第%d次，目前點數:%d" % (t, diceno))
print("共擲了%d次才出現4點:" % t)  # 當擲出4點時，顯示結果
"""
第1次，目前點數:3
第2次，目前點數:6
第3次，目前點數:3
第4次，目前點數:1
第5次，目前點數:6
第6次，目前點數:6
第7次，目前點數:5
第8次，目前點數:4
共擲了8次才出現4點:
"""


vnum = eval(input("請輸入欲反轉的一整數:"))
if vnum == 0:
    print(vnum)  # 直接輸出
else:  # 非0的整數，反轉
    while vnum != 0:  # 以迴圈的方式，將從最右位數取起，每一位數輸出反轉
        print(vnum % 10, end='')  # 整數除10的榆樹=>整數的個位數=>輸出
        vnum //= 10  # 整數除時的商=>去除到該整數的個位數 = vnum = vnum // 10
"""
請輸入欲反轉的一整數:1987
7891
"""

# 索引從0開始算起，位置從1開始算
lst = [2, 3, 5, 2, 33, 21, 99]  # 主List
print(lst[2:4])  # 索引2-3 位置:3-4=>[5,2]
print(lst[:3])  # 索引0-2 位置:1-3=>[2,3,5]
print(lst[5:])  # 索引5-6 位置:6-7=>[21,99]
print(lst[-4:-2])  # 索引-4(3)--3(4) 位置:4-5=>[2,33]
print(lst[1:5:2])  # 索引1,3=>[3,2]

"""
[5, 2]   
[2, 3, 5]
[21, 99] 
[2, 33]  
[3, 2]   
"""


# +, *, in/not in 運算
lst1 = [2, 3, 5, 9]
lst2 = [33, 99]

# =>像 lst1.extend(lst2)=>合併後=>lst1，此例，單純合併=>顯示=>沒有修改任何List
print(lst1 + lst2)  # =>[2, 3, 5, 9, 33, 99]
print(lst1 + lst2*2)  # =>[2, 3, 5, 9, 33, 99, 33, 99]

print(3 in lst1)  # 3是否有在lst1中，True
print(3 in lst2)  # 3是否有在lst2中，False

"""
[2, 3, 5, 9, 33, 99]
[2, 3, 5, 9, 33, 99, 33, 99]
True
False
"""
# 追蹤串列元素，List, range
print(range(0, 6))  # range(0,6)=>[0,1,2,3,4,5]<=無法直接print
lst = [2, 3, 5, 9, 33, 21, 99]  # lst串列
# 顯示串列內容
# print(lst)
for i in lst:
    print(i, end=" ")
print()
for i in range(0, len(lst), 3):  # range()=>[0,3,6]
    print(lst[i], end=" ")
"""
range(0, 6)
2 3 5 9 33 21 99
2 9 99
"""

# 串列解析(List Comprehesion)

lst = [x for x in range(5)]  # =>range(5)=>[0,1,2,3,4]=>x串列
print(lst)
print([a for a in lst if (a % 2) == 0])  # 產生偶數值的串列
print([a for a in lst if a % 2])  # 產生奇數的串列
"""
[0, 1, 2, 3, 4]
[0, 2, 4]
[1, 3]
"""

# 使用串列解析來處理質數
n = int(input('請輸入一非1的正整數(質數?):'))  # 詢問的整數
# n=5,range(2,n)=>[2,3,4]=>x=>放入x串列之前=>if(n%x)==0(若餘數為0)(若x串列中的元素有可整除n)=>lst串列
lst = [x for x in range(2, n) if (n % x) == 0]
if len(lst) == 0:  # lst無元素，沒有可將n整除的元素
    print(n, "是質數")
else:  # 有元素，有可將n整除的元素
    print(n, "不是質數")
"""
請輸入一非1的正整數(質數?):19
19 是質數

"""

# 求得一字串，得到該字串有A的字元有幾個(使用[x for x in list if 條件])
# 將字串"ABCDEACE"有A的字(if x == 'A')=>符合條件=>x元素=>放入lst串列
lst = [x for x in "ABCDEACE" if x == 'A']
print(lst)
print("此字串中有A的個數:", len(lst))  # 所產生的串列的長度

"""
['A', 'A']
此字串中有A的個數: 2
"""

tup = (1, 2, 3, 4, 5, 6)  # 建立數組(tuple)

lst = list(tup)  # 數組(tup)=>轉換成List=>lst=>[1,2,3,4,5,6]
print(lst.pop(3))  # 4 => lst=[1,2,3,5,6]

tup = tuple(lst)  # List轉成tuple=> tup=(1,2,3,5,6)
print(tup)
"""
4
(1, 2, 3, 5, 6)
"""
