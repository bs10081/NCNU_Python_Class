def main():
    # set data is list
    data = list()
    # put the number to the list
    data = data + list(map(int, input().split()))

    secNum = findSecondMin(data)
    print(secNum)


def findSecondMin(data):
    len(data)
    # 
    minNum = 10000000000000
    temNum = 0
    secNum = 0
    # 
    for i in range(1, len(data)):
        temNum = abs(data[i] - data[i-1])
        
        if temNum < minNum:
            secNum = minNum
            minNum = temNum

        elif temNum > minNum and temNum < secNum:
            secNum = temNum
            
        
    return secNum

if __name__ == "__main__":
    main()