def main():
    # set data is list
    data = list()
    # put the number to the list
    data = data + list(map(int, input().split()))

    # Use findSecondMin to calculate data
    secNum = findSecondMin(data)
    print(secNum)


def findSecondMin(data):
    len(data)
    minNum = 922337203685477580 # 64bit Max number
    temNum = 0                  # Cache
    secNum = 0                  # SecondNumber

    for i in range(1, len(data)):
        # Get the absolute value of two numbers
        temNum = abs(data[i] - data[i-1])

        # Logic
        if temNum < minNum:
            secNum = minNum
            minNum = temNum
        elif temNum == minNum: # Exclude LaoYu's 1 1 2 logic
            secNum = temNum
        elif temNum > minNum and temNum < secNum:
            secNum = temNum

    return secNum

if __name__ == "__main__":  # check main is main
    main()