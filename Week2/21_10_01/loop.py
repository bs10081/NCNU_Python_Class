def main():
    v = int(input("輸入的數字:"))
    printPrimes(v)

def printPrimes(n):
    # print v from 1 to n
    v = 2
    while v <= n:
        if isPrime(v):
            print(v)
        v = v + 1

def isPrime(v):
    # 除1 and v都不能整除v
    div = 2 
    while div < v:
        if v % div == 0:
            return False
        div = div + 1
    return True
main()
