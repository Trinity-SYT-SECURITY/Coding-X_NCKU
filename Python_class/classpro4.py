
"""
07-04 集合條件判斷 請以一程式，輸入數個整數並儲存至集合，
以輸入-9999為結束點，最後顯示該集合的長度(Length)，最大數(Max)，最小數(Min)，總和(Sum)。 例:>>>0, 34, 7, -23, 29, -1, -9999
=>{0, 34, 7, -23, 29, -1}
Length 6 Max 34 Min -23 Sum 46
Ans:
"""


import random  # 亂數套件
import random
numset = set()

while True:
    intset = eval(input("輸入整數並儲存至集合:"))
    if intset == -9999:
        break
    numset.add(intset)

print("集合長度:", len(numset))
print("集合最大數:", max(numset))
print("集合最小數:", min(numset))
print("集合總和:", sum(numset))
"""
輸入整數並儲存至集合:44
輸入整數並儲存至集合:654
輸入整數並儲存至集合:22
輸入整數並儲存至集合:56
輸入整數並儲存至集合:-342
輸入整數並儲存至集合:66  
輸入整數並儲存至集合:-2
輸入整數並儲存至集合:-9999
集合長度: 7
集合最大數: 654
集合最小數: -342
集合總和: 498
"""

"""
練習__習題 請寫一程式，產生10個亂數置放於名為lst的
串列中，再將該串列轉為集合後，並印出串列及集合的元素。

=> [11,22,88,45,58,83,26,39,55,31]
"""

# 由亂數建立10個整數的List
lstr = []  # 建立空串列
for i in range(10):
    rndNum = random.randint(1, 100)  # 產生1-100之間的亂數整數
    lstr.append(rndNum)  # 加入串列
print("原串列:", lstr)  # 顯示串列

#setLstr = set(lstr)
setL = set([x for x in lstr])
print("集合:", setL)
"""
原串列: [100, 51, 12, 46, 47, 7, 51, 19, 67, 99]
集合: {67, 100, 99, 7, 12, 46, 47, 51, 19} 
"""


""" 
05-02 乘積
請以一程式，讓使用者輸入的兩個數字作為參數傳遞給一個名叫compute(x,y)
的函式，此函示將回傳x和y的乘積。
例:>>>56，>>>11，=>616
"""


def compute(x, y):  # 函式:計算兩數x,y的乘積
    r = x * y
    return r  # 回傳結果(乘積)


# main()主程式
numx = eval(input("請輸入一整數:"))
numy = eval(input("請輸入一整數:"))
print("%d * %d= %d" % (numx, numy, compute(numx, numy)))
"""
請輸入一整數:11
請輸入一整數:77 
11 * 77= 847
"""

# 不定數參數(*args)


def add_sum(*args):  # arg的不定數參數的數組，累加的函式
    total_sum = 0  # 累加的總和
    # 累加的迴圈
    for i in args:  # 迴圈中會一一將args中的個別參數=>i
        total_sum += i
    return total_sum  # 回傳累加的結果


# main()
print(add_sum(2, 3, 4))  # 3個參數的累加
print(add_sum(5, 5, 5, 5, 5))  # 5個參數的累加


"""
05-10 費氏數列
請以一程式，計算費氏數列(Fibonacci numbers)，使用者輸入一正整數num，並將它傳遞給名為compute()的函式，此函示將回傳 費氏數列前num個的數值。
提示:F0=0, F1=1, Fn=Fn-1+Fn-2
例:>>>10，=>
0 1 1 2 3 5 8 13 21 34
"""
# 費氏數列


def fibonacci(n):  # 費氏數列的函式: Fn = Fn-1+ Fn-2
    n1 = 0  # F0
    n2 = 1  # F1
    print('%d %d' % (n1, n2), end=' ')
    for i in range(3, n+1):  # 列出F3..Fn
        n3 = n2 + n1  # Fn = Fn-1+ Fn-2
        print("%d" % (n3), end=' ')
        n1 = n2  # Fi+1準備，前兩個整數
        n2 = n3


# main()
fnum = eval(input("請輸入將列出的費氏數列的個數(>2):"))
fibonacci(fnum)  # 使用函式，列出費氏數列

"""
請輸入將列出的費氏數列的個數(>2):10
0 1 1 2 3 5 8 13 21 34 
"""


"""
05-14
請以一程式，在main()函式輸入一整數n，將此整數傳給factor()函式，用以顯示1~n的階層(n!=?)(使用遞迴(Recusive))
例:>>>5，=>1!=1 2!=2 3!=6 4!=24 5!=120
"""
# n階層factorial()計算(使用遞迴)


def factor(n):
    # factor(1) =1, factor(2) = 2 *1 =2 * factor(1)， factor(3)=3 * factor(2),...factor(n)=n * factor(n-1)
    if n == 0 or n == 1:
        return 1
    else:
        retu = n*factor(n-1)
        print(n, "階乘=", retu)
        return retu


# main()
num = int(input("請輸入n階層的整數:(>1):"))
print("%d!= %d " % (num, factor(num)))


"""
請輸入n階層的整數:(>1):4
2 階乘= 2
3 階乘= 6
4 階乘= 24
4!= 24
"""
