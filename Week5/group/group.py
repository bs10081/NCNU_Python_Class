def findGroup (friends, self) :
    
    group, friends[self], self = [self], friends[self]

    while friends[self] != -1 :
        
        group, friends[self], self = group + [self], -1, friends[self]
    return group

def findSol (friends) :
    groups = 0
    for person in range(len(friends))

        if friends[person] != -1 :
            print(*findGroup(friends, person))
            groups += 1
    print("小團體數：" + str(groups))

def main() :
    findSol(list(map(int, input().split())))
main()