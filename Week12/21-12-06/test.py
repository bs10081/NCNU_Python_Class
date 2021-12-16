import random
def shuffle():
    # create new cards
    card = [i for i in range(52)]
    # shuffle cards by swap 2 cards many times
    for i in range(1000):
        x, y = random.randint(0, 51), random.randint(0, 51)
        card[x], card[y] = card[y], card[x]
    print([sorted(card[:13]), sorted(card[14:25]), sorted(card[26:38]), sorted(card[39:51])])

shuffle()