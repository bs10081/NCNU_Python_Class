#Recursion例子
#有一個序列，每個數都是前兩個數字的加總
def FR(n):
    if n <= 1:
        return n
    return FR(n-1)+FR(n-2)

#阿克曼函數
def AR (m,n):
    if m == 0:
        return n+1
    if n == 0:
        return AR(m-1,1)
    return AR(m-1,AR(m,n-1))

#河內塔問題
#印出順序
#move n disl from A to C
def move(n,A,B,C):
    if n == 0:
        return
    #move n-1 disk from A to B
    move(n-1,A,C,B)
    #move 1 disk from A to C
    print(A,'-->',C)
    #move n-1 disk from B to C
    move(n-1,B,A,C)