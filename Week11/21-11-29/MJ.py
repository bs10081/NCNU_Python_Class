# simplified MJ
# assume 萬 only
# input: 9 digits each between 0 ~ 4
# output: True if can Hu, Flase otherwise
# sample input:
# 311111123 = 3張1，2到7各1張，類推
# card: list of ints represents each card's number

def canHu(card, n, needMJ=True):
    if n == 0:
        return True
    result = False
    for c in range(9):
        if card[c] >= 3:
            card[c] -= 3
            if canHu(card, n-3, needMJ):
                result = True
            card[c] += 3
        if needMJ and card[c] >= 2:
            card[c] -2
            if canHu(card, n-2, False):
                result = True
            card[c] += 2
        if c < 7 and card[c+2] >= 1 == card[c+1] >= 1  == card[c+2] >= 1:
            card[c], card[c+1], card[c+2], = card[c] -1, card[c+1] -1,card[c+2] -2
            if canHu(card, n-3, needMJ):
                result = True
            card[c], card[c+1], card[c+2] = card[c] +1, card[c+1] +1, card[c+2] +1
        return result

def main():
    data = [int(v) for v in input()]
    sumData = sum(data)
    print(canHu(data, sumData))

if __name__ == "__main__":
    main()