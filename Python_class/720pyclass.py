import random as ra
import random as ra  # 匯入亂數函數
one_piece = {"AAA", "BBB", "CCC"}  # 主角的集合1
users = {"CCC", "DDD"}  # 主角的集合2
# 顯示集合的操作
print(one_piece)
print("交集:", one_piece & users)  # 交集
print("聯集:", one_piece | users)  # 聯集
print("差集1:", one_piece - users)  # 差集
print("差集2:", users - one_piece)  # 差集
print("對稱差集:", users ^ one_piece)  # 對稱差集

s = set("Hello")
print("s字串的集合:", s)  # s集合<=Hello中沒重複的字母置入
"""
{'AAA', 'CCC', 'BBB'}
交集: {'CCC'}
聯集: {'AAA', 'DDD', 'BBB', 'CCC'}
差集1: {'AAA', 'BBB'}
差集2: {'DDD'}
對稱差集: {'AAA', 'DDD', 'BBB'}   
s字串的集合: {'l', 'e', 'H', 'o'} 
"""


def out():  # out的函數宣告
    print("您好，今日好嗎?")


# main()主程式
out()  # 呼叫函式 out()

# 乘積的函式


def comppow(a, b):  # 函式:計算a的b次方
    return a**b  # 回傳結果(次方)


# 計算階層factorial 3!=3*2*1, 5!=5*4*3*2*1
def factorial(n):  # 階層函式
    r = 1
    for i in range(1, n+1):  # 1-n的累乘
        r = r * i
    return r  # 回傳結果


# main()主程式
numn = eval(input("請輸入一整數求得階層:"))
print("%d! = %d" % (numn, factorial(numn)))

# main()主程式
numa = eval(input("請輸入一整數:"))
numb = eval(input("請輸入一整數(次方):"))
print("%d 的 %d次方= %d" % (numa, numb, comppow(numa, numb)))


# 參數預設值例:
# 函式:計算面積
def get_area(width, height=12):  # 預設高height = 12
    return width*height


# main()
print(get_area(6))  # 使用預設高<=12
print(get_area(6, 10))  # 寬=6, 高=10
"""
72
60
"""


# 全域變數與區域變數#1
def scope():
    var1 = 1  # 區域變數
    print("在scope中", var1, var2)  # 1, 20


# main()
var1 = 10  # 區域變數
var2 = 20  # 全域變數
scope()
print("在主程式中:", var1, var2)  # 10, 20
"""
在scope中 1 20
在主程式中: 10 20
"""

# 全域變數與區域變數#2


def scope():
    global var1
    var1 = 1  # 全域變數
    var2 = 2  # 區域變數，無宣告global
    print("在scope中", var1, var2)  # 1, 2


# main()
var1 = 10  # 全域變數
var2 = 20  # 區域變數
scope()
print("在主程式中:", var1, var2)  # 1, 20
"""
在scope中 1 2
在主程式中: 1 20
"""

# 參數的傳遞，可否變更(pass by Assignment)#1 #參數:字串，不可變更


def change(inp_str):  # 函式，參數:字串
    print("收到: inp_str=", inp_str)  # 收到: inp_str=成大
    inp_str = "台中"
    print("修改: inp_str=", inp_str)  # 修改: inp_str=台中


# main()
init_str = "成大"  # 原資料
print("原始: init_str=", init_str)  # 原始: init_str=成大
change(init_str)  # 呼叫函式，帶入參數init_str:字串
print("更新後: init_str=", init_str)  # 更新後:init_str=成大

"""
原始: init_str= 成大
收到: inp_str= 成大
修改: inp_str= 台中
更新後: init_str= 成大
"""

# 參數的傳遞，可否變更(pass by Assignment)#2 #參數:串列，可變更


def change(inp_list):  # 函式，參數:串列
    print("收到: inp_list=", inp_list)  # 收到: inp_list=["AAA", "BBB"]
    inp_list.append("CCC")
    print("修改: inp_list=", inp_list)  # 修改: inp_str=["AAA", "BBB", "CCC"]


# main()
init_list = ["AAA", "BBB"]  # 原資料串列
print("原始: init_list=", init_list)  # 原始: init_list=["AAA", "BBB"]
change(init_list)  # 呼叫函式，帶入參數init_str:字串
print("更新後: init_list=", init_list)  # 更新後:init_str=["AAA", "BBB", "CCC"]
"""
原始: init_list= ['AAA', 'BBB']
收到: inp_list= ['AAA', 'BBB']
修改: inp_list= ['AAA', 'BBB', 'CCC']
更新後: init_list= ['AAA', 'BBB', 'CCC']
"""

# 驗證[偽]亂數
# 第一次給予Seed
ra.seed(10)
print("第一個亂數:", ra.random())
print("第二個亂數:", ra.random())
# 第一次給予同一個Seed
ra.seed(10)
print("第三個亂數:", ra.random())
print("第四個亂數:", ra.random())

ra.random  # 預設系統時間為Seed
print("第五個亂數:", ra.random())
print("第六個亂數:", ra.random())

# 隨機排列 串列
numlst = [x for x in range(7)]  # numlst 有 0-6 串列
print("尚未亂數的list:", numlst)
ra.shuffle(numlst)  # 使用亂數，將list次序弄亂
print("使用亂數的list:", numlst)
"""
第一個亂數: 0.5714025946899135
第二個亂數: 0.4288890546751146
第三個亂數: 0.5714025946899135
第四個亂數: 0.4288890546751146
第五個亂數: 0.5780913011344704
第六個亂數: 0.20609823213950174
尚未亂數的list: [0, 1, 2, 3, 4, 5, 6]
使用亂數的list: [4, 5, 0, 1, 2, 3, 6]
"""

# 亂數:取後不放回，ra.sample
lottery = [x for x in range(1, 49)]
win_num = ra.sample(lottery, 6)
print("此次樂透號碼:", win_num)

# 亂數:取後放回，ra.choice
#lottery = [x for x in range(1, 49)]
l2 = [y for y in range(10)]
numb = [ra.choice(l2) for i in range(6)]
print("此次樂透號碼(取後放回):", numb)
"""
此次樂透號碼: [29, 8, 20, 44, 13, 15]
此次樂透號碼(取後放回): [7, 0, 0, 4, 0, 3]
"""
