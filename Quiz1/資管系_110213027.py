import random


def interestCalculation(deposit):
    # 銀行本金額 0 ~ 15000 , 利率 1.88%
    # 銀行本金額 15000 ~ 30000 , 利率 2.88%
    # 銀行本金額 30000 以上 , 利率 3.88%
    # 計算利息
    if deposit <= 15000:
        interest = deposit * 0.0188
    elif deposit <= 30000:
        interest = deposit * 0.0288
    else:
        interest = deposit * 0.0388
    # 利息加上本金
    deposit += interest
    # 四捨五入
    deposit = round(deposit, 2)
    # 輸出利息
    return deposit


def Q1():
    # 買手機
    print("第一題程式區塊")
    # 設定手機價格
    iPhone = 56400
    # 初始化存款金額
    deposit = 0
    # 初始化存款月份
    month = 0
    # - - -

    # 同行輸入 空白鍵切割
    # 同行輸入 空白鍵切割
    # 同行輸入 空白鍵切割

    # 很重要所以說三次 QAQ

    # - - -
    # 輸入薪水及存款金額
    salary, saveMoney = input("請輸入月薪與存款: ").split()
    # 如果每月儲蓄金額大於薪水則要求重新輸入
    while int(saveMoney) > int(salary):
        print("重新輸入")
        salary, saveMoney = input("請輸入月薪與存款: ").split()
    # 將薪水與存款金額轉換成整數
    salary = int(salary)
    saveMoney = int(saveMoney)
    while deposit < iPhone:
        # 如果月薪大於手機價格則輸出"可以馬上購買"
        if int(salary) > iPhone:
            print("可以馬上購買")
            # 結束程式
            quit()
        # 計算利息
        interestCalculation(deposit)
        # 儲蓄金加上每月存款
        deposit += int(saveMoney)
        # 存款月份加一
        month += 1
    # 如果可以直接購買則不會執行到這裡
    print("存款月份: ", month)


def Q2():
    print("第二題程式區塊")
    List_N = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # 建立字典 A:1 B:2
    dirN = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
            "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    # 隨機從字典中提取一個字母, 作為答案
    answer = random.choice(List_N)
    # 輸入一個變數，讓使用者可以猜程式所隨機選擇之字母，在猜的過程 中提示使用者要往前猜還是往後猜，直到猜對為止
    # answer 轉換成數字
    answer = dirN[answer]
    while True:
        guess = input("輸入字母: ")
        # 將guess根據字典 N 轉換成數字
        guess = dirN[guess]
        # 判斷猜的數字是否大於答案
        if guess == answer:
            print("恭喜猜對")
            break
        elif guess > answer:
            print("請往前猜")
        elif guess < answer:
            print("請往後猜")


def Q3():
    print("第三題程式區塊")
    # 輸入一個變數, 代表有多少堆餅乾
    n = int(input("輸入現在桌上有多少堆餅乾 "))
    # 輸入 N 堆餅乾各有幾個
    list = []
    for i in range(n):
        # 輸入每堆餅乾的數量
        list.append(int(input("請輸入第" + str(i + 1) + "堆餅乾的數量 ")))
    # 平均餅乾到最大限度
    # 餅乾只能從高往低處理
    # 疊完之後多餘的餅乾會被吃掉
    # 計算移動了多少次餅乾
    count = 0
