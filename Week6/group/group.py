def main():
    # input Friends list
    Friends = list(map(int, input().split()))
    # print small group list
    groupNum = 0
    for i in range(len(Friends)):
        if Friends[i] != -1:
            findFriends(i, Friends)
            groupNum += 1
    

    # = calculateSmallGroups(Friends)
    print("小團體數: {}".format(groupNum))

# def calculateSmallGroups(Friends):
#         # print(Friends[0])
#     for i in range(len(Friends)):
#         print(Friends[i]) # 4
#         # while 

#         print(temFriends)

def findFriends(me, Friends):
    # 印出團體的第一個人
    print(me, end="")
    fristFriends = me
    # 當我還有朋友，就印出我的朋友
    while Friends[me] != -1:

        # 當我的朋友是團體的第一個人時，就停止print
        if  fristFriends == Friends[me] :
            Friends[me] = -1    
            break
        print(" " +str(Friends[me]), end="")
        temFriends = Friends[me]
        Friends[me] = -1
        me = temFriends
    print()
if __name__ == "__main__":
    main()