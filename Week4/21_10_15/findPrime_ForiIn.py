def main():
    n = int(input())
    for prime in primes(n):
        print(prime)

def primes(n):
    v = 2
    while v <= n:
        if isPrime(v):
            yield v
        v = v + 1

# def isPrime(v):
#     div = 2
#     while div*div <= v:
#         if v % div == 0:
#             return False
#         div += 1
#     return True

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