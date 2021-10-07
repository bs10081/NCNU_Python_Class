def main():
    v = int(input())
    n = int(input())
    if v > n:
        n,v = v,n
        
    while v <= n:
        if isPrime(v):
            print(v)
        v = v + 1



def isPrime(v):                                      
    div = 2 
    while div < v:
        if v % div == 0:
            return False
        div = div + 1
    return True

main()
