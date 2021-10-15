# round v under digit d
def round(v, d):
    return int(v * 10 ** d + 0.5) / 10 ** d

def mymap(constr, obj):
    for v in obj:
        yield constr(v)
def main():
    # s = 'abcdef'
    # pos = 0
    # while pos < len(s):
    #     print(s[pos])
    #     pos = pos + 1

    # for char in 'abcdef':
    #     print(char)
    x, y = mymap(int, input().split())
    print(x,y)

def primes(n):
    v = 2
    while v <= n:
        if isPrime(v):
            yield v
        v += 1

def isPrime(v):
    if v % 2 == 0:
        return False
    div = 3
    while div*div <= v:
        if v % div == 0:
            return False
        div += 1
    return True

main()