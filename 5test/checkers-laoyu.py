def maxJump(n, r, c, b):
    maxLen = 0
    for ro, co in [ [1,0], [-1,0], [0, 1], [0, -1], [1, -1], [-1, -1], [1, 1], [-1, 1] ]:
        if r + 2 * ro >= 0 and r + 2 * ro < n and c + 2 * co >= 0 and c + 2 * co < n and \
        b[r + ro][c + co] == '1' and b[r + 2 * ro][c + 2 * co] == '0':
            b[r + ro][c + co] = '0'
            thisLen = 1 + maxJump(n, r + 2 * ro, c + 2 * co, b)
            if thisLen > maxLen:
                maxLen = thisLen
            b[r + ro][c + co] = '1'
    return maxLen
def main():
    n = int(input())
    r, c = [int(v) for v in input().split()]
    b = [input().split() for i in range(n)]
    b[r][c] = '0'
    print(maxJump(n, r, c, b))

main()