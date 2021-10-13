def main():
    try: 
        while True:
            begin, end = map(int, input().split())  #input 2 number in one line.
            if begin > end:
                end, begin = begin, end
            findSol(begin, end)     # use findSol to print anser.
    except EOFError:                # if error then pass. :)
        pass

def findSol(begin, end):
    maxLen = seqLen(begin)      # set a container for cycle.
    n = begin + 1
    while n <= end: 
        if seqLen(n) > maxLen:
            maxLen = seqLen(n)  # put seqLen(n) to maxLen.
        n = n + 1
    print(begin, end, maxLen) 


def seqLen(n):
    length = 1
    while n != 1:       # if n = 1 then STOP
        if n % 2 == 0:  # else n ←− n/2
            n = n // 2
        else:           # if n is odd then n ←− 3n + 1
            n = 3 * n + 1   
        length = length + 1
    return length

main()