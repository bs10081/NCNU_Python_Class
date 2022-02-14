def throwCard(n, hands, throw=None, score=0, maxScore=0) :
    for i in range(n) :
        # 若花色或數字一樣，則可丟掉
        if throw == None or hands[i] // 13 == throw // 13 or hands[i] % 13 == throw % 13 :
            tmp = throwCard(n-1, hands[:i] + hands[i+1:], hands[i], score+1, maxScore)
            if tmp > maxScore :
                maxScore = tmp
    if maxScore < score :
        maxScore = score
    return maxScore
        
def main() :
    n = int(input())
    hands = list(map(int, input().split()))
    print(throwCard(n, hands))
main()