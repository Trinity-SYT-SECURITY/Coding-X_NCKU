# 簡易寫入檔案範例
content = "meow"
# 開啟檔案
# 開啟 file1.txt檔案，並開啟[寫入]模式
f = open("C:\\Users\\user\\Desktop\\coding-X\\Python_class\\forFiles\\file1.txt", "w")
f.write(content)  # 寫入content的內容到檔案中
f.close()  # 關閉檔案
print("file1.txt檔案處理完成")  # 告訴使用者工作完成
