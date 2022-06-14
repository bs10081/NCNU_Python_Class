# curPos: 目前位置
# path: 路徑
# end: 終點
# maxStep: 最大步數
# road: 路線

def findPath(curPos,path, end, maxStep, road):
    # 如果當前位置等於終點，則回傳路徑
    if(curPos == end):
        print(*path)
        # result = list(map(str,path))
        # print(" ".join(result))
        return 1

    # 計算當回合可以走的步數
    count = 0

    # 找出所有可以走的步數，1 到 max step 步
    for step in range(maxStep):
        nextPos = curPos + step + 1
        # 如果當前位置小於等於最大步數，並且可以走的話，則加入路徑
        if(nextPos <= end and road[curPos+step+1] == 0):
            # 呼叫函式，並且把當前位置傳入，加count計算
            count += findPath(nextPos, path+[nextPos], end, maxStep, road)
    
    return count

# end: 終點
# maxStep: 最大步數
# road: 地圖路徑， 1代表有水，0代表沒水

def main():
    end = int(input())
    maxStep = int(input())
    road = list(map(int, input().split()))
    # 初始化路徑 and 輸出結果
    print(findPath(0, [0], end, maxStep, road))


if __name__ == "__main__":
    main()