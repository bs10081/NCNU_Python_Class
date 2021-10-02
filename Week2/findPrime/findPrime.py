v = None

def main():
    printPrimes(isInput())

def isInput():
    global v
    v = int(input("Begin Number: "))
    n = int(input("End Number: "))
    return n
def printPrimes(n):     # Define a function to print primes.
    
    global v
    # print v from 1 to n.
    while v <= n:
        if isPrime(v):
            print(v)
        v = v + 1

def isPrime(v):     # Check number is prime.
    # Divide v by one until it can’t be divide.
    div = 2 
    while div < v:
        if v % div == 0:
            return False
        div = div + 1
    return True
main()
