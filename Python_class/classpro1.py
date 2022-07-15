"""
01-01 整數格式化輸出
請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔
一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠
齊，左右皆以直線 |（Vertical bar）作為邊界。
"""
import math

from sklearn import impute
print("01-01", '\n')
a = 10
b = 200
c = 30
d = 400

# 靠右
print("|%5d %5d|" % (a, b))
print("|%5d %5d|" % (c, d))

# 靠左
print("|%-5d %-5d|" % (a, b))
print("|%-5d %-5d|" % (c, d))

"""
|   10   200|
|   30   400|
|10    200  |
|30    400  |
"""
print("~"*150)
"""
請寫一程式，指定四個分別含有小數1到4位的浮點數，然後將這
四個浮點數以欄寬7，每列印兩個的方式，先列印向右靠齊，在
列印向左靠齊，左右皆以直線|作為邊界。*提示:輸出浮點數到小數後第二位。
"""
print("01-02", '\n')
a = 51.755
b = 4.322
c = 643.861
d = 9.2677

# 靠右
print("|%7.2f %7.2f|" % (a, b))
print("|%7.2f %7.2f|" % (c, d))

# 靠左
print("|%-7.2f %-7.2f|" % (a, b))
print("|%-7.2f %-7.2f|" % (c, d))
"""
|  51.76    4.32|
| 643.86    9.27|
|51.76   4.32   |
|643.86  9.27   |
"""

print("~"*150)

"""
請寫一程式，輸入一圓的半徑，並加以計算此圓的面積和周長，最後印出此圓的
半徑(Radius)，周長(Perimeter)和面積(Area)。
**提示:需import math，並使用math.pi，輸出浮點數到小數後第二位。
"""
print("01-03", '\n')
PI = math.pi  # 圓周率
radius = eval(input("請輸入一園的半徑: "))
# 計算周長根面積
print("半徑(Radius)= %.2f" % radius)
print("周長(Perimeter)= %.2f" % (2*PI*radius))  # 計算周長並輸出
# pow 是次方
print("面積(Area) = %.2f" % (PI * pow(radius, 2)))  # 計算園面積並輸出,pow(r,2) =r平方
"""
請輸入一園的半徑: 10
半徑(Radius)= 10.00
周長(Perimeter)= 62.83
面積(Area) = 314.16
"""

print("~"*150)
"""
請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數
"""
print("01-04", '\n')
sum1, sum2, sum3, sum4, sum5 = eval(input("輸入五個數字= "))

sumall = sum1+sum2+sum3+sum4+sum5
avgall = sumall/5  # 平均

print("你輸入的數值= {} {} {} {} {}".format(sum1, sum2, sum3, sum4, sum5))
print("你輸入的總和= %.1f" % sumall)
print("你輸入的平均= %.1f" % avgall)
"""
輸入五個數字= 20,30,60,50,40
你輸入的數值= 20 30 60 50 40
你輸入的總和= 200.0
你輸入的平均= 40.0
"""
print("~"*150)
"""
請寫一程式，請使用者輸入華氏溫度，然後輸出其對應的攝氏溫度。提示:攝氏=(華氏-32)5/9，輸出小數後2位

攝氏= 5/9 乘(華氏溫度- 32)
華氏= (攝氏乘9/5) + 32
"""
print("01-05", '\n')
user = eval(input("輸入想轉換成攝氏度的華氏溫度:"))
C = (user - 32) * 5/9  # 攝氏=(華氏-30)*5/9
print("攝氏 = %.2f 度C" % C)
"""
輸入華氏溫度:100
攝氏 = 37.78 度C
"""
print("~"*150)

"""
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）。
"""
print("02-01", '\n')
user = eval(input("輸入數字判斷偶數:"))
math = user % 2

if math == 0:
    print("{}是偶數".format(user))
else:
    print("{}不是偶數".format(user))
"""
輸入數字判斷偶數:120
120是偶數
輸入數字判斷偶數:83 
83不是偶數
"""

print("~"*150)
"""
請以選擇敘述寫一程式，讓使用者輸入一個正整數，
然後判斷它是3或5的倍數，若此數同時為3與5的倍數，
顯示[x is a muliple of 3 and 5.];如此此數值皆不
屬於3或5的倍數，顯示[x is not a multiple of 3 or 5.]，將使用者輸入的數值帶入x。
"""
print("02-02", '\n')
numx = eval(input("請輸入一正整數(判別3,5的倍數):"))  # x
# 判別倍數的過程，1.(3與5的倍數)，2.(3的倍數)，3.(5的倍數)
if (numx % 3 == 0) & (numx % 5 == 0):  # (3與5的倍數)
    print("%d is a multiple of 3 and 5." % numx)
elif (numx % 3 == 0):  # (3的倍數)
    print("%d is a multiple of 3." % numx)
elif (numx % 5 == 0):  # (5的倍數)
    print("%d is a multiple of 5." % numx)
else:  # 非 3 或 5 的倍數，以上皆非
    print("%d is not a multiple of 3 or 5." % numx)
"""
請輸入一正整數(判別3,5的倍數):35
35 is a multiple of 5.
"""
print("~"*150)
"""
請以選擇敘述寫一程式，讓使用者輸入兩個整數a, b，然後在
輸入一算術運算子(+、-、*、/、//、%)，輸出這兩個數以及其經過運算後的結果。
"""
print("02-03", '\n')

int1, int2 = int(input("輸入兩整數a,b:"))
cal = input("輸入算術運算子:")

if (cal == '+'):
    allca = int1+int2
    print("運算結果是{} ".format(allca))
elif (cal == '-'):
    allca = int1-int2
    print("運算結果是{} ".format(allca))
elif (cal == '*'):
    allca = int1*int2
    print("運算結果是{} ".format(allca))
elif (cal == '/'):
    allca = int1/int2
    print("運算結果是{} ".format(allca))
elif (cal == '//'):
    allca = int1//int2
    print("運算結果是{} ".format(allca))
elif (cal == '%'):
    allca = int1 % int2
    print("運算結果是{} ".format(allca))
else:
    print("運算子輸入錯誤請重新輸入")

"""
輸入兩整數a,b:10,20
輸入算術運算子:+
運算結果是30
"""
print("~"*150)
"""
請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣
優惠後的實付金額。購物金額折扣方案如下表所示，顯示購買金額，實付金額，+折扣方案：
8,000（含）以上     9.5折
18,000（含）以上    9折
28,000（含）以上    8折
38,000（含）以上    7折
"""
print("02-04", '\n')

userinp = eval(input("輸入購物金額:"))
if userinp < 8000:
    print("你輸入的購物金額是{},沒有折扣".format(userinp))

elif (userinp >= 8000) and (userinp < 18000):
    cost = userinp * 0.95
    print("你輸入的購物金額是{},折扣9.5後是{}".format(userinp, cost))

elif (userinp >= 18000) and (userinp < 28000):
    cost = userinp * 0.9
    print("你輸入的購物金額是{},折扣9折後是{}".format(userinp, cost))

elif (userinp >= 28000) and (userinp < 38000):
    cost = userinp * 0.8
    print("你輸入的購物金額是{},折扣8折後是{}".format(userinp, cost))

elif (userinp >= 38000):
    cost = userinp * 0.7
    print("你輸入的購物金額是{},折扣7折後是{}".format(userinp, cost))

"""
輸入購物金額:30000
你輸入的購物金額是30000,折扣8折後是24000.0
輸入購物金額:3000
你輸入的購物金額是3000,沒有折扣
"""
