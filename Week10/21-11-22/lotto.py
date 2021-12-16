# lotto 包牌
# input: 2 lines
# first line: n m, n個號碼選出m個
# second line a list of int, 表示已經選好的數字
# output: 所有符合條件的數字組合
# eg:
# 49 6
# 1 11 3
def main():
    allNum, chosseNum = map(int, input().split())
    underNum = list(map(int, input().split()))
    # comb(setDiff([i + 1 for i in range(allNum)], underNum), chosseNum - len(underNum), underNum)
    a=[]
    for i in range(1,allNum+1):
        a+=[i]
    for i in underNum:
        a.remove(i)
        chosseNum-=1
    comb(a, chosseNum, underNum)

def setDiff(a, b):
    result = list()
    for v in a:
        if not v in b:
            result.append[v]
    return result

def comb(a, n, c):
    if n == 0:
        print(*c)
        return
    for p in range(len(a)):
        comb(a[p+1:], n-1, c + [a[p]])

if __name__ == "__main__":
    main()