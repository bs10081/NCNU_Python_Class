v=None
def main():
    printPrimes(isInput())
def isInput():
    global v
    v=int(input())#
    n=int(input())
    if n < v:
        n,v=v,n
    return n
def printPrimes(n):
    global v
    while v <= n:
        if isPrime(v):
            print(v)
        v = v+1
    
def isPrime(v):
    div=2
    while div < v:
        if v%div == 0:
            return False
        div=div+1
    return True
main()
