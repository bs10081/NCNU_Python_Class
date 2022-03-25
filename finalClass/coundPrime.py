def main():
    x = int(input())
    y = int(input())
    if x > y:
        y,x = x,y
    maxLen = 0
    while x <= y:
        if isPrime(x):
            maxLen += 1
        x = x + 1
    print(maxLen)

def isPrime(v):                                      
    div = 2 
    while div*div < v:
        if v % div == 0:
            return False
        div = div + 1
    return True

if __name__ == "__main__":
    main()