def findSol(n, m, data, deadline, result, allAns):
    # 如果貨物搬完了，回傳這個可能性
    if n == 0:
        return
    minCost = -1
    for i in range(m):
        if data[i][0] <= deadline:
            temCost = findSol(n-1, m, data, deadline-data[i][0])
            if temCost != -1 and (minCost == -1 or minCost > data[i][1] + temCost):
                minCost = temCost + data[i][1]
def main():
    # input the worker and the worker profile
    n ,m = int(input()), int(input())
    # call findSol to do something
    minCost = findSol(n, m, [[int[v] for v in input().split()] for i in range(m)]),
    # 嘗試完所有的可能性之後，樹狀結構退回後，沒有任何的可能性，便輸出搬不完，否則便取最小值（錢）輸出
    print(minCost if minCost != -1 else "搬不完")

if __name__ == "__main__":
    main()