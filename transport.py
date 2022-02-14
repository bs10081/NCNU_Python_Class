# 學號 : 110213049
# 姓名 : 廖承偉

#計算搬運(要搬的個數,可以用的工人時間,可以用的工人時薪,工作總時間,已選時間,已選金錢,成功搬完的總金額列表)
def carry(n,time,money,deadline,nowt,nowm,totalm):
    #如果搬完了(n沒了)
    if n == 0:
        #如果這個總金額還沒出現過,加到總金額列裡
        if not sum(nowm) in totalm:
            totalm.append(sum(nowm))
        return
    for i in range(len(time)):
        #如果加上下一個時間不會超過deadline,就繼續排列
        if sum(nowt+[time[i]])<=deadline:
            #每搬完一次剩n-1個,選擇的時間變成c+[time[i]],現在金額變成nm+[money[i]]
            carry(n-1,time,money,deadline,nowt+[time[i]],nowm+[money[i]],totalm)
    #如果都沒有符合條件的結果,回傳搬不完,否則回傳總金額列裡的最小值
    if totalm ==[]:
        return '搬不完'
    else:
        return min(totalm)
def main():
    n = int(input())
    m = int(input())
    #將時間和金錢各創一個列表紀錄工人的資料
    time,money = list(),list()
    for i in range(m):
        t,m = map(int,input().split())
        time.append(t),money.append(m)
    print(carry(n,time,money,int(input()),[],[],[]))
main()