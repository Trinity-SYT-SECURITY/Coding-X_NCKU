# 簡易讀入檔案範例
f = open("file1.txt", "r")  # 開啟檔案 file1.txt檔案，並開啟[讀入]模式
for line in f:  # 一次讀一行
    # print(line) #輸出所讀的一行的內容
    print(line, end="")  # 輸出所讀的一行的內容
f.close()  # 關閉檔案
print("file1.txt讀入檔案處理完成")  # 告訴使用者工作完成


# 使用with來open檔案讀取
with open("file1.txt", "r") as f:  # 開啟檔案 file1.txt檔案，並開啟[讀入]模式=>f
    for line in f:  # 一次讀一行
        print(line, end="")  # 輸出所讀的一行的內容
# 使用with，將不需使用close來關閉檔案，with結束時就關閉檔案
print("file1.txt讀入檔案處理完成")  # 告訴使用者工作完成
