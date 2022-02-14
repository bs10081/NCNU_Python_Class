def maxJump(n, m, r, c, b, all = []):
    maxLen = 0
    # 將八個方位抓出來
    road1 = [ [2, 1], [-2, 1], [-1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1], [1, 2] ]
    road2 = [ [1, 2], [2, 1], [-2, 1], [-1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1] ]
    road3 = [ [-2, -1], [1, 2], [2, 1], [-2, 1], [-1, 2], [1, -2], [2, -1], [-1, -2] ]
    road4 = [ [-1, -2], [-2, -1],  [1, 2], [2, 1], [-2, 1], [-1, 2], [1, -2], [2, -1] ]
    road5 = [ [2, -1], [-1, -2], [-2, -1],  [1, 2], [2, 1], [-2, 1], [-1, 2], [1, -2] ]
    road6 = [ [1, -2], [2, -1], [-1, -2], [-2, -1],  [1, 2], [2, 1], [-2, 1], [-1, 2] ]
    road7 = [ [-1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1],  [1, 2], [2, 1], [-2, 1] ]
    road8 = [ [-2, 1], [-1, 2], [1, -2], [2, -1], [-1, -2], [-2, -1],  [1, 2], [2, 1] ]
    for item in [road1,road2,road3,road4,road5,road6,road7,road8]:
        for ro, co in item:
            # 如果沒有超出邊界以及下一個點沒有馬
            if r + ro >= 0 and r + ro < m and c + co >= 0 and c + co < n and b[r + ro][c + co] == '0':
                # 記錄跳了一次，然後移動馬兒到新的位置
                b[r + ro][c + co] = '1'
                thisLen = 1 + maxJump(n, m, r+ro, c+co, b)
                if thisLen > maxLen:
                    maxLen = thisLen
    return maxLen

def main():
    n, m = map(int, input().split())
    b = [input().split() for i in range(m)]
    r, c = [int(v) for v in input().split()]
    print(maxJump(n, m, r, c, b))

if __name__ == "__main__":
    main()