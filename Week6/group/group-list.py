def main():

    isFriends = list(map(int, input().split()))

    numberOfSmallGroups = findSol(isFriends)

    print("小團體數: {}".format(numberOfSmallGroups))

def findSol(isFriends):
    readList = 0
    isGroup, numberOfSmallGroups = calculateSmallGroups(isFriends, readList)

    print(isGroup)
    # first = True
    # for v in [1, 2, 5, 7] :
    #     if first :
    #         print(v, end='')
    #         first = False
    #     else :
    #         print(' ' + v, end='')
    #         print()


    return numberOfSmallGroups


def calculateSmallGroups(isFriends, readList):
    defaultFriends = isFriends[0]   # 4
    
    temFriends = isFriends[isFriends[0]]    # 4 -> 6
    isGroup = list()
    isGroup.append(isFriends[0])    # 4
    
    # print(temFriends)
    while defaultFriends != temFriends:
        
        isGroup.append(temFriends)
        temFriends = isFriends[temFriends]
    isGroup.insert(0, isGroup[-1])
    isGroup.pop(-1)

    readList += 1
    return(isGroup, readList)


if __name__ == "__main__":
    main()