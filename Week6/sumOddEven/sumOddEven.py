def findSol(Number):
    # default oddNum and evenNum
    oddNum = 0
    evenNum = 0
    # Check is odd or even, and add
    for i in range(len(Number)):
        if Number[i] % 2 == 0:
            evenNum += Number[i]
        else:
            oddNum += Number[i]

    return oddNum, evenNum

def main():

    # oddNum, evenNum = findSol(list(map(int, input().split())))
    # print(oddNum, evenNum)

    print(*findSol(list(map(int, input().split()))))

if __name__ == "__main__":
    main()