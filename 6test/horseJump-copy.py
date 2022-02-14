def maxJump(n, m, r, c, b):
    maxLen = 0
    for ro, co in [ [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2] ]:
        if r + ro >= 0 and r + ro < m and c + co >= 0 and c + co < n and b[r + ro][c + co] == '0':
            b[r + ro][c + co] = '1'
            thisLen = 1 + maxJump(n, m, r+ro, c+co, b)
            # print(thisLen)
            if thisLen > maxLen:
                maxLen = thisLen
            b[r + ro][c + co] = '0'
    return maxLen
def main():
    n, m = map(int, input().split())
    b = [input().split() for i in range(m)]
    r, c = [int(v) for v in input().split()]
    print(maxJump(n, m, r, c, b))
if __name__ == "__main__":
    main()