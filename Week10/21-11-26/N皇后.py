#N皇后問題
#4 lines in a board
#for n queen
#n?vertical lines? 0~n-1
#n?horizontal lines? 0~n-1
#2n-1?up right lines? 0~2n-2
#2n-1?down right lines? 0~2n-2
#for a position(r,c) #座標
#belonfg to which lines?
#c vertical lines
#r horizontal lines
#r+c up right lines #組合概念
#r-c+n-1 down right lines #右下 #最大到最小之間 #n-1目的為正
#r 前面擺了幾個皇后 也代表現在要擺的是哪個row
#v直線，ur右斜/，dr左斜
def findSol(n,r,v,ur,dr):
    #已經擺完所有皇后了
    if n == r:
        return 1
    #計算次數
    sols = 0 
    for c in range(n):#放置皇后在[r][c] #n*n矩陣的column
        #擺上條件是其他地沒有皇后
        if v[c] and ur[r+c] and dr[r-c+n-1]:
            #上面條件是可以擺皇后的地方
            #如果有皇后，改成False，條件不成立就不會recurtion
            v[c],ur[r+c],dr[r-c+n-1] = False,False,False #放一個皇后上去
            sols += findSol(n,r+1,v,ur,dr) #計算次數
            #把值改回來
            v[c],ur[r+c],dr[r-c+n-1] = True,True,True #釋放出位置
    return sols

def main():
    #n*n棋盤
    n = int(input())
    #n是n*n的棋盤，0是row,[True for i in range(n)]是column
    #[True for i in range(2*n-1)]右斜/ [True for i in range(2*n-1)]左斜
    print(findSol(n,0,[True for i in range(n)],[True for i in range(2*n-1)],[True for i in range(2*n-1)]))
main()



