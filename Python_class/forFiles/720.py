# 讀取csv並分割數字資料
f = open('C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\number.csv',
         'r', encoding='UTF-8')  # 開啟檔案
num_list = []  # 存放number.csv的數字的串列
# 開始讀檔
for line in f:  # 一次一行
    onerow = line.strip().split(',')  # 先將line中的前後空白去除.strip，以,分割=>串列onerow
    print(onerow)
    num_list.extend(int(x) for x in onerow)  # 每一行的數字(int(x))合併=>num_list
print(num_list)
f.close()
"""
['14', ' 52', '76 ', ' 43']
['32', ' 45', ' 99', ' 103']
[14, 52, 76, 43, 32, 45, 99, 103]
"""


# 讀取csv並分割數字資料
f = open('C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\number.csv',
         'r', encoding='UTF-8')  # 開啟檔案
num_list = []  # 存放number.csv的數字的串列
# 開始讀檔
for line in f:  # 一次一行
    onerow = line.strip().split(',')  # 先將line中的前後空白去除.strip，以,分割=>串列onerow
    # print(onerow) #顯示一行中以被分割split的字串數字的串列
    num_list.extend(int(x) for x in onerow)  # 每一行的數字(int(x))合併=>num_list
print(num_list)  # 所有數字資料的數字串列
f.close()
print("number.csv檔案中所有資料的加總:", sum(num_list))  # 輸出總和
print("number.csv檔案中所有資料的平均:", sum(num_list)/len(num_list))  # 輸出平均
"""
[14, 52, 76, 43, 32, 45, 99, 103]
number.csv檔案中所有資料的加總: 464
number.csv檔案中所有資料的平均: 58.0
"""
