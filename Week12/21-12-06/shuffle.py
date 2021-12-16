# 學號：110213027
# 姓名：簡齊君

# 發橋牌
# 假設以int 0 ~ 51 表示52張牌
# 0 ~ 12 為spade A ~ 2, 13 ~ 25 為heart，26 ~ 38 diamond，39 ~ 51 club
# 請發 East, South, West, North 四家牌如下
# East
# S AKQ32
# H
# D JAT987
# C 32
# South
# S ...
# H ...
# 亂數發四家牌

import random
# return list of 4 lists
def shuffle():
    # create new cards
    card = [i for i in range(52)]
    # shuffle cards by swap 2 cards many times
    for i in range(1000):
        x, y = random.randint(0, 51), random.randint(0, 51)
        card[x], card[y] = card[y], card[x]
    return [sorted(card[:13]), sorted(card[13:26]), sorted(card[26:39]), sorted(card[39:])]

def showCards(cards):
    # for player h
    for h in range(4):
        # cards = hands[h]
        # print(cards)
        # cards = shuffle()
        print(['North', 'East', 'South', 'West'][h] + ':')
        # for color c
        for c in range(4):
            print(['S', 'H', 'D', 'C'][c], end=' ')
            # print v of color c
            print(sameSuit(c, cards[h]))
        # print()
def sameSuit(s, card):
    # print four hands cards
    name = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    result = ''
    # put the name to the index
    for c in card:
        if c // 13 == s:
            result += name[c%13]
    return result

def main():
    showCards(shuffle())

if __name__ == "__main__":
    main()
