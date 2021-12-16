#input: 2 lines
#1st line: int represents distance d #總里程數
#2nd line: a list of int represents each student's running distance #每人可跑的距離
#output: how many combinations that sum of a combination #有幾總組合可以讓 可跑距離 = 里程數

#組合
#總里數 = 可跑距離組合加總
#或 總里數-選到的那個人 == 0，則記數1
# for
# i
# 總里數-選到list裡被選到的人 原list-選到人

def findSol(Distance,Studens):
    #總里數-選到人里數 = 0，即記數
    if Distance <= 0: #<=讓它不要再找了
        return 1 if Distance == 0 else 0 
    #記數
    sols = 0
    for i in range(len(Studens)):
        sols += findSol(Distance-int(Studens[i]),Studens[i+1:]) #sols+= 新用法
    return sols

def main():
    print(findSol(int(input()),list(map(int,input().split()))))

main()