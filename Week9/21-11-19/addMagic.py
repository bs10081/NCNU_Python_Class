# 1??2 ?442 7?44
# pos: the position I have to fill
# s: string of a, b, c
# la, lb, lc: length of a, b, c

def main():
    a, b, c = input().split()
    findSol(a + b + c, len(a), len(b), len(c), 0)

def findSol(s, la, lb, lc, pos):
    if len(s) == pos:
        if fitEq(s, la, lb, lc):
            print(s[0:la],s[la:la+lb],s[la+lb:])
        return
    if s[pos]=='?':
        # if is '?' then do it.
        for i in range(10):
            # if s = abcdf, i = 5, answer = abc5df 
            # s[0 to pos] + 'i' s[pos + 1 to end] 
            findSol(s[0:pos] + str(i) + s[pos+1:], la, lb, lc, pos + 1)
    else:
        # if is not '?', then pass.
        findSol(s, la, lb, lc, pos + 1)

def fitEq(s, la, lb, lc):
    # s[0 to la - 1] + s[la to la + lb] == s[la + lb to end]
    return int(s[0:la]) + int(s[la:la+lb]) == int(s[la+lb:])

if __name__ == "__main__":
    main()