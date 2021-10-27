def main():
    # input Friends list
    Friends = list(map(int, input().split()))
    # print small group list
    groupNum = 0
    for i in range(len(Friends)):
        if Friends[i] != -1:
            findFriends(i, Friends)
            groupNum += 1

    print("小團體數: {}".format(groupNum))

def findFriends(me, Friends):
    # print frist friend in the group
    print(me, end="")
    firstFriends = me
    # When I have a friend, then pritn the friend.
    while Friends[me] != -1:

        # When my friend is alone, then STOP
        if  firstFriends == Friends[me] :
            Friends[me] = -1
        print(" " +str(Friends[me]), end="")
        temFriends = Friends[me]
        Friends[me] = -1
        me = temFriends
    print()
if __name__ == "__main__":
    main()