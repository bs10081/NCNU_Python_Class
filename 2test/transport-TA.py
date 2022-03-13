def findSol(n, m, data, deadline, result, allAns):
    # 如果時間不夠，那麼便終止這個可能性
    if deadline < 0:
        return
    # 如果貨物搬完了，回傳這個可能性
    if n == 0:
        allAns.append(sum(result))
        return
    for i in range(m):
        #n-1                  deadline - 當前worker的耗時；result + 當前worker搬運一次的價格
        findSol(n-1, m, data, deadline - data[i][0], result + [data[i][1]], allAns)
def main():
    # input worker
    n = int(input())
    # input worker types
    m = int(input())
    # set data is list
    data = []
    # input worker profile
    for i in range(m):
        data.append(list(map(int, input().split())))
    # input deadline
    deadline = int(input())
    # set allAns is list
    allAns = []
    # call findSol to 
    findSol(n, m, data, deadline, [], allAns)
    # 嘗試完所有的可能性之後，樹狀結構退回後，沒有任何的可能性，便輸出搬不完，否則便取最小值（錢）輸出
    if len(allAns) == 0:
        print('搬不完')
    else:
        print(min(allAns))

if __name__ == "__main__":
    main()