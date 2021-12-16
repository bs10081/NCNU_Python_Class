#first lines: an int n
#then n lines each have n chars
#output: how many block in the map
#definition:相鄰的字元若一樣，則視為同一個block

# 1111AAABB
# 1AABB22BB
# 2AABCCCB2
# AAACCCB22
# ABBCCCC11
# CCCCCCCCC

# 00000000000
# 01111AAABB0
# 01AABB22BB0
# 02AABCCCB20
# 0AAACCCB220
# 0ABBCCCC110
# 0CCCCCCCCC0
# 00000000000

#一維:上下差n，左右差1
#邊界問題解1：四個and-1，n+1 邊界 #邊界問題：在外面包一圈非合法值
#n: size of map
#data: map data

def findSol(n, data):
    # create board with sentinal ' '
    board = [' ' for i in range((n+2)**2)]
    # fill data into board
    for r in range(n):
        for c in range(n):
            board[(r+1)*(n+2)+c+1] = data[r*n+c] #[(r+1)*(n+2)+c+1] #n進位系統 #邊框變成n+2
    count = 0
    # for r in range(n):
    #     for c in range(n):
    #         if board[(r+1)*(n+2)+c+1] != ' ':
    for p in range(n+2,(n+1)*(n+2)):
        if board[p] != ' ':
                mark (board,n,p,[n+2,-(n+2),1,-1])    # 這句可以改成八個方向
                count += 1
    return count

# board: map data(have ' ')
# n: map size
# p: need mark point
# d: up, down, left, right

def mark(board,n,p,d):
    color = board[p]
    board[p] = ' '
    for v in d:
        if board[p+v] == color:
            mark(board, n, p+v, d)

def main():
    data = list()
    n = int(input())
    for l in range(n):
        data += [v for v in input()]
    print(findSol(n, data))


main()