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

def findSol(n, r, v, ur, dr):
    if n == r:
        return 1
        
    sols = 0

    for c in range(n):
        if v[c] and ur[r+c] and dr[r-c+n-1]:
            v[c], ur[r+c], dr[r-c+n-1] =False, False, False
            sols += findSol(n, r+1, v, ur, dr)
            v[c], ur[r+c], dr[r-c+n-1] = True, True, True
    return sols

def main():
    n = int(input())
    print(findSol(n,0,[True for i in range(n)],[True for i in range(2*n-1)],[True for i in range(2*n-1)]))

if __name__ == "__main__":
    main()