"""
6-08 最大最小值索引

請以一程式，讓使用者建立一個 3*3的矩陣，其內容為從鍵盤輸入的整數(不重複)，接著輸出矩陣最大值與最小值的索引。

例:>>>6,4,8,39,12,3,-3,49,33 =>index of the largest number = 49 is (2,1)
index of the smallest number -3 is:(2,0)

Ans:
"""
# 3*3矩陣的最大最小值索引
size = 3  # 矩陣大小
mat = []  # 矩陣串列
# 建立2維矩陣並輸入元素的數字
for i in range(size):
    mat.append([])  # 建立二維矩陣[[],[],[]]
    for j in range(size):  # 輸入數字
        # (i,j)=>(1,0)=>mat[[6,4,8],[39]]
        mat[i].append(eval(input('輸入不重複的整數:')))
# 開始找出矩陣中的最大數，最小數及其位置(在串列中的索引)
max_n = min_n = mat[0][0]  # 最大，最小值，預設為第一個元素[0][0]
max_index = min_index = [0, 0]  # 索引值List
for i in range(size):  # 第一維
    for j in range(size):  # 第二維
        if mat[i][j] > max_n:  # 找到較大數
            max_n = mat[i][j]  # 紀錄該元素
            max_index = [i, j]  # 紀錄索引
        elif mat[i][j] < min_n:  # 找到較小數
            min_n = mat[i][j]  # 紀錄該元素
            min_index = [i, j]  # 紀錄索引
# 輸出最後結果
print("index of the largest number = %d is (%d,%d)" %
      (max_n, max_index[0], max_index[1]))
print("index of the smallest number = %d is (%d,%d)" %
      (min_n, min_index[0], min_index[1]))
"""
輸入不重複的整數:10
輸入不重複的整數:44
輸入不重複的整數:98
輸入不重複的整數:32
輸入不重複的整數:97 
輸入不重複的整數:22
輸入不重複的整數:14 
輸入不重複的整數:66
輸入不重複的整數:32
index of the largest number = 98 is (0,2)
index of the smallest number = 10 is (0,0)
"""

print("~"*150)
"""
      06-04 眾數
請以一程式，讓使用者輸入十個整數做為樣本數，輸出眾數
(樣本中出現最多次的數字)及其出現的次數。
例:>>34，18，22，32，18，29，30，38，42，18。 =>18，3
"""
# 求數值串列中的眾數
size = 10  # 串列個數
sample = []  # 數值樣本的串列
count = [0]*size  # 複製[0]成為10個元素的串列=>count，每個sample中個別數值的次數的串列
for i in range(size):  # 輸入數值到串列sample
    num = eval(input())
    sample.append(num)  # 加入到串列sample
    count[sample.index(num)] += 1  # 將此輸入的數值次數+1==>>count
num_occu = max(count)  # 找出在count中最高的次數，眾數在sample中的次數
theNo = sample[count.index(num_occu)]  # 眾數
print("眾數為:", theNo)
print("出現的次數:", num_occu)
print(sample)  # 顯示sample的List內容
print(count)  # 顯示count的List內容
"""
1          
2
3
4
5
6
6
4
3
2
眾數為: 2
出現的次數: 2
[1, 2, 3, 4, 5, 6, 6, 4, 3, 2]
[1, 2, 2, 2, 1, 2, 0, 0, 0, 0]
"""
print("~"*150)

"""
07-01 串列數組轉換

請撰寫一程式，輸入數個整數並儲存至串列中，以輸入-9999為結束點
（串列中不包含-9999），再將此串列轉換成數組，
最後顯示該數組以及其長度（Length）、最大值（Max）、最小值（Min）、
總和（Sum）
"""
nums = eval(input("輸入一整數(-9999結束輸入):"))
numsLst = []  # 存放整數的串列
while nums != -9999:  # -9999結束輸入
    numsLst.append(nums)  # 加入List中
    nums = eval(input("輸入一整數(-9999結束輸入):"))
# 結束輸入=>建立List結束
numstup = tuple(numsLst)  # List轉換成Tuple=>numstup
# 所有tuple中的結論輸出
print("目前的數組:", numstup)
print("數組中長度(元素數):", len(numstup))
print("數組中最大數:", max(numstup))
print("數組中最小數:", min(numstup))
print("數組中總和:", sum(numstup))

"""
輸入一整數(-9999結束輸入):423
輸入一整數(-9999結束輸入):555
輸入一整數(-9999結束輸入):212
輸入一整數(-9999結束輸入):33
輸入一整數(-9999結束輸入):224
輸入一整數(-9999結束輸入):-432
輸入一整數(-9999結束輸入):55
輸入一整數(-9999結束輸入):33
輸入一整數(-9999結束輸入):9 
輸入一整數(-9999結束輸入):5 
輸入一整數(-9999結束輸入):0
輸入一整數(-9999結束輸入):-9999
目前的數組: (423, 555, 212, 33, 224, -432, 55, 33, 9, 5, 0)
數組中長度(元素數): 11
數組中最大數: 555
數組中最小數: -432
數組中總和: 1117
"""

print("~"*150)
"""
07-02 數組合併排序
請以一程式，輸入並建立兩個數組，各以-9999為結束點
(數組中不包含-9999)，將此兩數組合併並從小排序之，
顯示排序前的數組和排序後的串列
例:
>>>create tuple1:9, 0, -1, 3, 8, -9999
>>>create tuple2:28, 16, 39, 56, 78, 88, -9999
=>
Combined tuple before sorting: (9, 0, -1, 3, 8, 28, 16, 39, 56, 78, 88)
combined list after sorting: [-1, 0, 3, 8, 9, 16, 28, 39, 56, 78, 88]
"""

num1 = 0
num2 = 0
numsLst = []  # 存放整數的串列
numsLst2 = []  # 存放整數的串列
print("create tuple:")

while (num1 != -9999):  # -9999結束輸入

    num1 = eval(input("create tuple1(-9999結束輸入):"))
    if (num1 != -9999):  # 不另外加這條，會多出開始的num1=0
        numsLst.append(num1)  # 加入List中
numstup = tuple(numsLst)

print("~"*100)

while (num2 != -9999):

    num2 = eval(input("create tuple2(-9999結束輸入):"))
    if (num2 != -9999):
        numsLst2.append(num2)  # 加入List中

numstup2 = tuple(numsLst2)
# 結束輸入=>建立List結束
dictnum = numstup + numstup2  # 數組合併

print("Combined tuple before sorting:{}".format(dictnum))

numlist = sorted(dictnum)
print("combined list after sorting: {}".format(numlist))

print("~"*100+"另一個做法")
# 建立並產生兩組數組
tup1 = tup2 = ()
print("建立數組tup1:")
while True:
    numt = eval(input("請輸入一整數(-9999為結束):"))
    if numt == -9999:
        break  # 中斷迴圈
    tup1 += (numt,)  # tup1 = tup1 + (numt,), 新增numt(數組)到tup1
# print(tup1) #顯示已新增資料後的tup1數組
print("建立數組tup2:")
while True:
    numt = eval(input("請輸入一整數(-9999為結束):"))
    if numt == -9999:
        break  # 中斷迴圈
    tup2 += (numt,)  # tup2 = tup2 + (numt,), 新增numt(數組)到tup2
# 合併兩數組，並顯示
comb_tup = tup1 + tup2  # 合併數組
print("排序前的已合併的數組:", comb_tup)
# 數組=>串列List =>排序(小到大)，顯示已排序的串列
comb_lst = sorted(list(comb_tup))  # 已排序的串列
print("排序後的已合併的串列:", comb_lst)  # 輸出

"""
create tuple:
create tuple1(-9999結束輸入):3243
create tuple1(-9999結束輸入):44
create tuple1(-9999結束輸入):12   
create tuple1(-9999結束輸入):555
create tuple1(-9999結束輸入):-9999
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
create tuple2(-9999結束輸入):342
create tuple2(-9999結束輸入):-454
create tuple2(-9999結束輸入):-5566
create tuple2(-9999結束輸入):-42
create tuple2(-9999結束輸入):22
create tuple2(-9999結束輸入):-9999
Combined tuple before sorting:(3243, 44, 12, 555, 342, -454, -5566, -42, 22)
combined list after sorting: [-5566, -454, -42, 12, 22, 44, 342, 555, 3243]
"""

print("~"*150)
"""
07-09 詞典排序

請撰寫一程式，輸入一顏色詞典color_dict（以輸入鍵值”end”作為輸入結束點，詞典中將
不包含鍵值”end”），再根據key值的字母由小到大排序並輸出。
"""
color_dict = {}  # 顏色字典，空的字典
while True:  # 輸入顏色字典的元素，Key輸入"end"結束輸入
    ckey = input("請輸入顏色Key(end為結束):")
    if ckey == "end":  # 將結束輸入
        break  # 中斷 while
    cvalue = input("請輸入顏色Value:")
    color_dict[ckey] = cvalue  # 新增一筆顏色的元素[key:value]

# 結束color_dict輸入
cDict = sorted(color_dict)  # 將顏色字典的Key排序=>cDict[]
# 輸出整個已排序的顏色字典cDict
print("輸出已排序的顏色字典:")
for oneC in cDict:
    print("%s:%s" % (oneC, color_dict[oneC]))
"""
請輸入顏色Key(end為結束):yellow
請輸入顏色Value:100
請輸入顏色Key(end為結束):red
請輸入顏色Value:8787
請輸入顏色Key(end為結束):blue
請輸入顏色Value:2222
請輸入顏色Key(end為結束):end
輸出已排序的顏色字典:
blue:2222
red:8787
yellow:100
"""
print("~"*150)
"""
07-08 詞典合併
請以一程式，輸入兩個字典(以輸入"end"作為輸入結束點)，將此兩個字典合併，
並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。 例:

Create dict1:Key: a，Value: apple，Key: b，Value: banana，Key: d，Value: durian，Key: end
Create dict2:Key: c，Value: cat，Key: e，Value: elephant，Key: end
=> a: apple
b: banana
c: cat
d: durian
e: elephant
Ans:
"""
#輸入兩個字典dict1, dict2
print("建立字典1:")
dict1 = {}
while True:
    dkey = input("請輸入Key(end為結束):")
    if dkey == "end":  # 將結束輸入
        break  # 中斷 while
    dvalue = input("請輸入Value:")
    dict1[dkey] = dvalue  # 新增一筆元素[key:value]

print("建立字典2:")
dict2 = {}
while True:
    dkey = input("請輸入Key(end為結束):")
    if dkey == "end":  # 將結束輸入
        break  # 中斷 while
    dvalue = input("請輸入Value:")
    dict2[dkey] = dvalue  # 新增一筆元素[key:value]
# 合併兩個字典，將key做排序，輸出整體的已合併，已排序的字典
merge_dict = dict1.copy()  # 複製字典dict1=>merge_dict
merge_dict.update(dict2)  # 以更新方式update，來合併dict1,dict2=>merge_dict
mSortedDict = sorted(merge_dict)  # 將merge_dict的key做排序=>mSortedDict[]
print("輸出已排序的合併兩字典:")
for oneD in mSortedDict:
    print("%s:%s" % (oneD, merge_dict[oneD]))

"""
建立字典1:
請輸入Key(end為結束):kali
請輸入Value:988
請輸入Key(end為結束):mscos
請輸入Value:99
請輸入Key(end為結束):win
請輸入Value:12 
請輸入Key(end為結束):ubuntu
請輸入Value:100
請輸入Key(end為結束):end
建立字典2:
請輸入Key(end為結束):centos
請輸入Value:345
請輸入Key(end為結束):end   
輸出已排序的合併兩字典:
centos:345
kali:988
mscos:99
ubuntu:100
win:12
"""

print("~"*150)
""" 
07-10 詞典搜尋
請以一程式，為一字典輸入資料(以輸入"end"作為輸入結束點)，
再輸入一鍵值並檢視此鍵值是否存在於該字典中。 例:

Key: 123-4567-89，Value: Jennifer，Key: 987-6543-21，
Value: Tommy，Key: 2468246-82，Value: Kay，Key: end

Search key: 2468246-82 =>True
"""

dict1 = {}
while True:
    dkey = input("請輸入Key(end為結束):")
    if dkey == "end":  # 將結束輸入
        break  # 中斷 while
    dvalue = input("請輸入Value:")
    dict1[dkey] = dvalue  # 新增一筆元素[key:value]
merge_dict = dict1.copy()
mSortedDict = sorted(merge_dict)  # 將merge_dict的key做排序=>mSortedDict[]

inp = input("Search key:")
if inp in merge_dict:
    print("%s:%s" % (inp, merge_dict[inp]))
    print("true")
else:
    print("not")

"""
請輸入Key(end為結束):123-4567-89 
請輸入Value:Jennifer    
請輸入Key(end為結束):987-6543-21
請輸入Value:Tommy
請輸入Key(end為結束):2468246-82
請輸入Value:Kay
請輸入Key(end為結束):end 
Search key:987-6543-21
987-6543-21:Tommy
true
"""

# 詞典搜尋
# 輸入字典mydict
print("建立字典:")
mydict = {}
while True:
    dkey = input("請輸入Key(end為結束):")
    if dkey == "end":  # 將結束輸入
        break  # 中斷 while
    dvalue = input("請輸入Value:")
    mydict[dkey] = dvalue  # 新增一筆元素[key:value]

# 輸入搜尋key，搜尋
searchKey = input("請輸入欲搜尋的key:")
print("您所蒐尋的key:%s:%s" % (searchKey, (searchKey in mydict)))
"""
建立字典:
請輸入Key(end為結束):meow
請輸入Value:999
請輸入Key(end為結束):meme
請輸入Value:888
請輸入Key(end為結束):heloo
請輸入Value:877
請輸入Key(end為結束):end
請輸入欲搜尋的key:meme
您所蒐尋的key:meme:True
"""
