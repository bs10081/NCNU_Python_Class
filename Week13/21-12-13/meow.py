def main():
    cats = ['鯊魚', 'hero', 'mia', '黑貓', 'miu', 'mogan', 'mori', 'melo', '小貓']
    today, nBeside= map(int, input().split())
    nBesideCatName = list(input().split())

    perm(cats, today, [], nBesideCatName)
# def findSol():
    # print("---------")
    # print(nBesideCatName)
    # print(cats[0], cats[1])
def perm(a, n, c, nBesideCatName):
    if n == 0:
        print(*c)
        return
    for p in range(len(a)):
        if len(c)==0 or not c[-1] in nBesideCatName or not a[p] in nBesideCatName:
            perm(a[:p] + a[p+1:], n-1, c + [a[p]], nBesideCatName)

if __name__ == "__main__":
    main()
