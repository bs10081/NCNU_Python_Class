# 學號：110213027
# 姓名：簡齊君
def main():
    howManyNumber = int(input())
    Number = list(map(int, input().split()))
    typeGraph(howManyNumber, Number, max(Number))

def typeGraph(defaultSize, Number, maxNumber):

    for i in range(maxNumber+2, 0, -1):
        # row = [str(i).zfill(2)]
        print(str(i).zfill(2), end=" ")
        for v in range(defaultSize):
            if (Number[v]) >= i:
                #print(str(Number[v]).zfill(2), end=" ")
                print(str("## "), end="")
            else:
                print(str(".. "), end="")
        print()

    # print the x axis
    for column in range(len(Number)+1):
        print(str(column).zfill(2)+' ',end='')
    print()

if __name__ == "__main__":
    main()