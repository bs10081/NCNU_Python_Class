# given x, y
# print the max cycle length ostarts from v, for v between x, y

def main():
    # input x, y
    x, y = int(input("intput x: ")), int(input("input y: "))
    # print x, y, and the max cycle length for x to y.
    print(x, y, findMax(x, y))


# find the max lenght start from x to y.
def findMax(x, y):
    if y > x:
        x, y = y, x
    # set maxLen to shortest possible length 1
    maxLen = cycleLen(x)
    v = x + 1
    # for v from x to y, do:
    while v <= y:
        # cal length of v, cycleLen(v)
        # if cycleLen(v) > maxLen, then:
        if cycleLen(v) > maxLen:
            # set maxLen to cycleLen(v)
            maxLen = cycleLen(v)
        v = v + 1
    # here we has processed all v between x, y
    # return maxLen
    return maxLen

def cycleLen(n):
    # set clen to 1
    clen = 1
    # while n is not 1, then:
    while n != 1:
        # increase clen
        clen += 1
        # gen next n, rule is
        # if n is even, then:
        if n % 2 == 0:
            # n = n // 2
            n = n // 2
        # else (must be odd) :
        else:
            # n = 3n + 1
            n = 3 * n + 1
    # here n has become 1, so clen is the cycle length
    # return cycle length
    return clen

if __name__ == "__main__":
    main()