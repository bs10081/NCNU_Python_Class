def main():
    try:
        while True:
            start, end = map(int, input().split())
            if start > end:
                start,end = end,start
            findSol(start, end)
    except EOFError:
        pass
# find the maximun seqence length betwee(start, end)
def findSol(start, end):
    maxLen = seqLen(start)
    v = start + 1
    while v <= end:
        if seqLen(v) > maxLen:
            maxLen = seqLen(v)
        v = v + 1
    print(start, end, maxLen)
# calculate the seqence length of seed v
def seqLen(v):
    length = 1
    while v != 1:
        if v % 2 == 0:
            v = v // 2
        else:
            v = v*3 + 1
        length = length + 1
    return length
main()
