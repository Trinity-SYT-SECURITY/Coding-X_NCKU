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
