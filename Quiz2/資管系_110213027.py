import random


def interestCalculation(deposit):
    # 剩餘貸款金額 1 ~ 20000 , 利率 18.8%
    # 剩餘貸款金額 20001 ~ 50000 , 利率 28.8%
    # 剩餘貸款金額 50001 以上 , 利率 38.8%
    # 計算利息
    if deposit <= 20000:
        interest = deposit * 0.188
    elif deposit <= 50000:
        interest = deposit * 0.288
    else:
        interest = deposit * 0.388
    # 利息加上本金
    deposit += interest
    # 輸出利息
    return deposit


def Q1():
    print("第一題程式區塊")
    # 輸入欠的錢
    deposit = int(input("欠了多少錢:"))
    # 輸入還款金額
    pay = int(input("每個月可以還多少錢:"))
    # 計算還款期數
    month = 0
    while deposit > 0:
        deposit -= pay
        deposit = interestCalculation(deposit)
        month += 1
        # 如果一年還沒還完,就會被追殺,輸出"小心討債人"
        if month % 13 == 0:
            print("小心討債人")
            quit()
    # 輸出還款期數 format 需要 ** 月才可以還完
    print("需要 {} 個月才可以還完".format(month))


def Q2():
    print("第二題程式區塊")
    List_N = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "一", "二", "三", "四", "五", "六", "七", "八", "九 ", "十"]
    # 建立字典 1:1 2:2 3:3 ... 10:10 一:11 二:12 三:13 ... 十:20
    N = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
         "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
    ans = random.choice(List_N)
    # 輸入數字
    while True:
        guess = input("請輸入數字或中文數字(1~10):")
        # 數字與國字都代表1~10
        # 判斷輸入是否大於答案,若是則輸出 "請往前面的數字猜"
        if N[guess] > N[ans]:
            print("請往前面的數字猜")
        # 判斷輸入是否小於答案,若是則輸出 "請往後面的數字猜"
        elif N[guess] < N[ans]:
            print("請往後面的數字猜")
        # 如果猜到同一數值但是文字與數字不同時,則輸出 "差一點"
        elif N[guess] == N[ans] and guess != ans:
            print("差一點")
        # 猜對時,則輸出 "恭喜答對"
        else:
            print("恭喜答對")
            break


def Q3():
    print("第三題程式區塊")
    print("上次就不會了,這次肯定不會")
