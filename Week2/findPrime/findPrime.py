<<<<<<< HEAD
v = None                                                # v = None, Global function.
=======
v = None    # v = None, Global function.
>>>>>>> 547dbdc041905c7d27ad85023f86200ea64a21c0

def main():
    printPrimes(isInput())

def isInput():
    global v                                            # Use Global variavle "v"
    Begin = int(input())
    End = int(input())
    v = min(Begin, End)                                 # Get the min Number to fix Order problem.5
    n = max(Begin, End)                                 # Get the max Number to fix Order problem.
    return n
def printPrimes(n):                                     # Define a function to print primes.
    
    global v
                                                        # print v from 1 to n.
    while v <= n:
        if isPrime(v):
            print(v)
        v = v + 1

def isPrime(v):                                         # Check number is prime.
                                                        # Divide v by one until it can’t be divide.
    div = 2 
    while div < v:
        if v % div == 0:
            return False
        div = div + 1
    return True
main()
