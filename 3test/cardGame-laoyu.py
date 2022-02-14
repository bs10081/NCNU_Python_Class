def perm(hand, last = -1):
    maxLen = 0
    for p in range(len(hand)):
        # 如果最後一張牌和手上的牌 同花色or同數字
        if last == -1 or hand[p]//13 == last//13 or hand[p]%13==last%13:
            # 把數字排列完，然後加入到緩存值
            temLen = 1 + perm(hand[:p] + hand[p+1:], hand[p])
            # 緩存值大於最大值，便覆蓋
            if temLen > maxLen:
                maxLen = temLen
    return maxLen

def main():
    n = int(input())
    print(perm([int(v) for v in input().split()]))

if __name__ == "__main__":
    main()