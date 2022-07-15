import math
import keyword  # 保留字

"""
range(1, 11)：產生從1到10的整數序列(未指定遞增值的情況下，其遞增值預設為1)。
利用range()來產生for-loop的控制變數
"""
n = 10
resu = 1
for i in range(1, n+1):
    resu += i
    print(resu, end=" ")  # 2 4 7 11 16 22 29 37 46 56

"""
2 4 7 11 16 22 29 37 46 56 
"""

# print()函式預設輸出後一定會做換行，如果不想換行，可以指定end=''
py = 1
# int py = 1
a = b = c = 30
print()
print("a=" + str(a) + " b=" + str(b) + " c="+str(c), end="")
print()
print(keyword.kwlist)  # 查詢保留字

"""
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

# 資料型態查詢
x = 1
print(type(x))  # <class 'int'>
x = 1.1
print(type(x))  # <class 'float'>
x = "1.1"
print(type(x))  # <class 'str'>
"""
<class 'int'>
<class 'float'>
<class 'str'>
"""


a = 30
b = 40
c = a > b
print(c)  # False
print(type(c))  # <class 'bool'>
"""
False
<class 'bool'>
"""


# 輸出
print("TQC + Python 3認證考試", '\n')  # TQC + Python 3認證考試
"""
TQC + Python 3認證考試
"""


# 格式化輸出
num = 100
print("%3.2f" % num, '\n')  # 100.00
"""
100.00
"""


print('%d' % 20, '\n')  # 格式化整數
print('%f' % 1.11, '\n')  # 預設保留6位小數
print('%.1f' % 1.11, '\n')  # 取1位小數
print('My name is %s' % 'tom', '\n')  # 格式化字串
"""
20
1.110000
1.1
My name is tom
"""
# 若{}內不指定索引值的話，預設依序從0開始，()會依照參數填入的順序


name = "tom"
age = 20
strr = "my name is {} and my age is {}".format(name, age)
print(strr)  # my name is tom and my age is 20
"""
my name is tom and my age is 20
"""

name = "tom"
age = 20
strr = "my name is {1} and my age is {0}".format(name, age)
print(strr)  # my name is 20 and my age is tom
"""
my name is 20 and my age is tom
"""

pi = 3.14  # 圓周率變數
print("圓周率 = %3.5f" % pi)  # 3.14000
print("圓周率 = %4.1f" % pi)  # 3.1
"""
圓周率 = 3.14000
圓周率 =  3.1
"""

num = 99  # 整數變數
print("%3d" % num)  # 正數，靠右對齊，左邊補空白
print("%-3d" % num)  # 負數，靠左對齊，右邊補空白
"""
 99
99
"""


name = "John"
score = 99
print("{} 的成績是: {}".format(name, score))    # John 的成績是: 99
"""
John 的成績是: 99
"""


score = int(input("請輸入你的數學成績:"))  # 輸入成績 => score=>字串 =>轉換int
score = eval(input("請輸入你的數學成績:"))  # 輸入成績 => score=>字串 =>轉換eval數值
print("您的數學成績", score)
print("您的成績+10=", (score + 10))
"""
請輸入你的數學成績:80
您的數學成績 80
您的成績+10= 90
"""

str1 = "67"
num = 23 + int(str1)
print("23 + 67 = " + str(num))
"""
23 + 67 = 90
"""

# 運算式
PI = math.pi  # 圓周率
radius = eval(input("請輸入一園的半徑: "))
# 計算周長根面積
print("半徑(Radius)= %.2f" % radius)
print("周長(Perimeter)= %.2f" % (2*PI*radius))  # 計算周長並輸出
# pow 是次方
# print("面積(Area) = %.2f" % (PI * pow(radius, 2)))  # 計算園面積並輸出,pow(r,2) =r平方
print("面積(Area) = %.2f" % (PI * (radius ** 2)))  # 計算園面積並輸出,pow(r,2) =r平方
"""
請輸入一園的半徑: 10
半徑(Radius)= 10.00
周長(Perimeter)= 62.83
面積(Area) = 314.16
"""

# Pythonic
c, d = eval(input("輸入兩數做交換:"))

c, d = d, c

print("交換後{} {}".format(c, d))
"""
輸入兩數做交換:4,3
交換後3 4
"""

# 交換a, b兩變數
a = 3
b = 5
print("交換前 a=%3d b=%3d" % (a, b))
"""
交換前 a=  3 b=  5
交換後 a=  5 b=  3
"""


# 開始交換
"""
#傳統交換法
temp = a  #a=>temp
a =b    # b=>a
b = temp  # temp=>b =>a<=>b
"""
# pythonic 寫法
a, b = b, a
print("交換後 a=%3d b=%3d" % (a, b))  # 輸出結果
"""
交換後 a=  5 b=  3
"""


# 假設 a = 3, b = 1
a = 3

b = 1

# 請寫程式輸出下列判別式的真(True)、假(False)值
print("(1<=b) and (b<=a) and (a<10)=>", ((1 <= b) and (b <= a) and (a < 10)))

"""
(1<=b) and (b<=a) and (a<10)=> True
"""

#(((1<=1) and (1<=3)) and (3<10))
# (True and True) and True => True
# Pythonic 寫法
# 1<=b<=a<=10 => 1<=1<=3<=10 =>True
print("1<=b<=a<=10 =>", (1 <= b <= a <= 10))
"""
(1<=b) and (b<=a) and (a<10)=> True
1<=b<=a<=10 => True
"""

score = eval(input("輸入成績查詢是否及格:"))
if (0 <= score < 60):  # 不及格操作
    print("你的成績 {} 不及格".format(score))  # 符合條件
else:
    print("你的成績 {} 及格".format(score))
"""
輸入成績查詢是否及格:100
你的成績 100 及格
輸入成績查詢是否及格:22
你的成績 22 不及格
"""

# 百分比成機轉等地
score = eval(input("輸入成績:"))
level = None
if (90 <= score):
    level = "優等"
elif (80 <= score < 90):
    level = "甲等"
elif (70 <= score < 80):
    level = "乙等"
elif (60 <= score < 70):
    level = "丙等"
elif (50 <= score < 60):
    level = "不及格"

# 輸出成績等地
print("%d 的等第是 %s" % (score, level))
"""
輸入成績:90
90 的等第是 優等
"""

# 巢狀
# 輸入成績
score = eval(input("請輸入您的成績(0-100):"))
level = "輸入(0-100之間)"  # 等第
if (0 <= score <= 100):  # 輸入成績在0-100合法中
    if (90 <= score):
        level = "優等"
    elif (80 <= score < 90):
        level = "甲等"
    elif (70 <= score < 80):
        level = "乙等"
    elif (60 <= score < 70):
        level = "丙等"
    elif (score < 60):
        level = "不及格"
else:
    level = "輸入錯誤，成績須在0-100之間!!"
# 輸出成績的等第
print("%d 的等第 %s" % (score, level))
"""
請輸入您的成績(0-100):80
80 的等第 甲等
"""


# 運算式
# 運算式<-Pythonic寫法
numx = input("請輸入一整數(運算元1):")
numy = input("請輸入一整數(運算元2):")
oper = input("請輸入一運算子(+-*/..):")
print(numx + oper + numy + "=", eval(numx + oper + numy))
"""
請輸入一整數(運算元1):1
請輸入一整數(運算元2):2
請輸入一運算子(+-*/..):+
1+2= 3
"""

# 串列
score = [66, 22, 98]
print(score)
print(score[1])

list2 = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF"]  # 字串List
# 輸出元素
print(list2)  # 輸出整個List
print("list2[1]=", list2[1])  # List的第二個元素[1]
# print("list2[6]=", list2[6]) #List的第?個元素[6]<-ERROR
print("list2[-1]=", list2[-1])  # List2的倒數第一個元素[-1]
print("list2[-6]=", list2[-6])  # List2的倒數第六個元素[-6]
# print("list2[-7]=",list2[-7]) #ERROR
"""
[66, 22, 98]
22
['AAA', 'BBB', 'CCC', 'DDD', 'EEE', 'FFF']
list2[1]= BBB
list2[-1]= FFF
list2[-6]= AAA
"""

numx = input("請輸入一整數(運算元1):")
numy = input("請輸入一整數(運算元2):")
oper = input("請輸入一運算子(+-*/..):")
print(numx + oper + numy + "=", eval(numx + oper + numy))
"""
請輸入一整數(運算元1):10
請輸入一整數(運算元2):20
請輸入一運算子(+-*/..):+
10+20= 30
"""

print(range(5))  # 錯誤，只顯示函式範圍
list0 = range(5)
print(range(5))

# for迴圈
for i in range(10):
    print(i, end=" 的2次方 ")  # range(10)元素輸出
    print(i**2)  # i的2次方
"""
0 的2次方 0
1 的2次方 1
2 的2次方 4
3 的2次方 9
4 的2次方 16
5 的2次方 25
6 的2次方 36
7 的2次方 49
8 的2次方 64
9 的2次方 81
"""

# 1-10的列表並加總
total = 0  # 總合
for i in range(1, 11):
    print(i)
    total += i
print("上述總合:", total)

"""
1
2
3
4
5
6
7
8
9
10
上述總合: 55
"""
