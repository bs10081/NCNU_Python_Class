# 3 5
# 1 2 3 4 5
# 1 3 4 2 5
# 5 2 2 4 3

# 0000000
# 0123450
# 0134250
# 0522430 
# 0000000

# 12345 13425 52243

# 00000
# 01110
# 02220
# 03330
# 00000
#一維:上下差n，左右差1
#邊界問題解1：四個and-1，n+1 邊界 #邊界問題：在外面包一圈非合法值
#n: size of map
#data: map data

# board: map data(have ' ')
# n: map size
# p: need mark point
# d: up, down, left, right

def mark(board,n,p,d):
    color = board[p]
    # board[p] = 0
    for v in d:
        if board[p+v] == color:
            board[p+v] = 0
            board[p] = 0
    
            # mark(board, n, p+v, d)
    # print(board)

def drop(board,n,p,d):
    # board[p] = 0
    if board[p+d] == 0:
        temNum = board[p]
        board[p] = board[p+d]
        board[p+d] = temNum
    # if board[p+d+d] == 0:
    #     temNum = board[p]
    #     board[p] = board[p+d]
    #     board[p] = board[p+d+d]
    #     board[p+d+d] = temNum
    #     board[p+d] = temNum
        
        drop(board, n, p+d, d)

def format(board,n,m):
    for v in range(m+2**m):
        if board[v] == ' ':
            board.pop(v)
    return board

def findsame(n, m, data):
# create board with sentinal ' '
    board = [ ' ' for i in range((m+2**m))]
    # fill data into board
    for r in range(n):
        for c in range(m):
            board[(r+1)*(m+2)+c+1] = data[r*m+c] #[(r+1)*(n+2)+c+1] #n進位系統 #邊框變成n+2
    # print(board)
    # print("----------")
    # count = 0
    # for r in range(n):
    #     for c in range(n):
    #         if board[(r+1)*(n+2)+c+1] != ' ':
    # for i in range(m+2,(n+1)*(m+2)):
    #     if board[i] != ' ' and board[i] != 0:
    #         drop (board,n,i,[-(m+2)])
    
    for v in range(99999):
        for p in range(m+2,(n+1)*(m+2)):
            # for i in range(m+2,(n+1)*(m+2)):
            #     if board[i] != ' ' and board[i] != 0:
            #         drop (board,n,i,-(m+2))

            if board[p] != ' ' and board[p] != 0:
                mark (board,n,p,[m+2,-(m+2),1,-1])    # 這句可以改成八個方向

            if board[p] != ' ' and board[p] != 0:
                drop (board,n,p,(m+2))       
    # print(board)
    # board = format(board,n,m)
    return [i for i in board if i != ' ']
    
def main():
    data = list()
    n, m = map(int, input().split())
    for I in range(n):
        data += [v for v in input().split()]

    board = findsame(n, m, data)
    # print(board)
    # print("------")

    for i in range(0,int(n)):
        print(*(board[m*i:m*(i+1)]))
    print()

if __name__ == "__main__":
    main()