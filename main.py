# 顯示完整的地圖，debug用，避免像上次一樣。
def disp(cells):
    # 顯示 cells
    for i in cells:
        for j in i:
            print(j, end="")
        print("")
    print("")

def isEnd(cells):
    # 回傳一個結果，確認地圖中是否只有一個棋子，同理，可以通過更改數字來改更多的變化
    return sum([sum(i) for i in cells]) == 1

def checkSpace(pos, origin_pos, origin_cells, direction, size, record):
    # because which will overwrite the original map, so we need to copy a new map.
    cells = [[j for j in i] for i in origin_cells] 

    dire_row, dire_col = direction
    original_row, original_col = pos
    row, col = [original_row + dire_row, original_col + dire_col] # new space
    # 確定他不會撞牆
    if(row >= size or row < 0 or \
            col >= size or col < 0):
        return 0 # will not count in
    # 確定要跳過去的格子是空的
    if(cells[row][col] != 0): # is new new cell empty
        return 0
    # 更新地圖
    cells[original_row][original_col] = 0 # cell ate
    cells[origin_pos[0]][origin_pos[1]] = 0 # original pos
    # 將棋子移動到下一個位置。
    cells[row][col] = 1

    # 輸出log
    # print(record)

    # debug 用的地圖
    # disp(cells)

    record.append([row, col])

    return process(size, cells, row, col, record)
    # ...

def checkNearby(row, col, cells, direction, size, record):
    dire_row, dire_col = direction
    # 墊腳石座標(1;[1, 1]) = 原始座標(0[0, 0])加上direction的座標([1, 1])
    # row + dire_row ; col + dire_row
    # 0 * * 
    # * 1 * 
    # * * 2 
    new_row, new_col = [row + dire_row, col + dire_col]
    # 檢查是否有超出邊界，新的座標位置大於 size，或者是新的row小於0，或著是新的col大於size，亦或著新的col小於0。
    if(new_row >= size or new_row < 0 or \
            new_col >= size or new_col < 0):
        # 那麼便代表超出了座標，所以return 0 來表示這次的路徑不算。
        return 0 # will not count in
    # 如果不能吃掉的新的棋子的話（因為沒有棋子，所以不算數），就return 0
    if(cells[new_row][new_col] != 1): # ate cell
        return 0

    return checkSpace([new_row, new_col], [row, col], cells, direction, size, record)
    # .......
    # checkSpace(...)
    # return process(...)

def process(size, cells, row, col, record):
    # y, x
    # 八個方向的座標
    direction = [
        [1,0], # SOUTH
        [-1,0],# NORTH
        [0, 1], # EAST
        [0, -1], # WEST
        [1, -1], # SOUTH WEST
        [-1, -1], # NORTH WEST
        [1, 1], # SOUTH EAST
        [-1, 1] # NORTH EAST
    ]

    # 用來觀察程式的運作
    record = [i for i in record]

    # 設定次數為 0
    result = 0

    # 總結每一個樹狀節點有幾種可能性。
    for item in direction:
        result += checkNearby(row, col, cells, item, size, record)


    # 如果跑到底，沒有結果了
    if(result == 0):
        # 那麼便確定場上是否只有一個棋子
        if(isEnd(cells)):
            # 輸出log
            # print(record)
            return 1
        return 0
    # 處理完成，回傳給main
    return result

    # ....
    # for: 
    # checkNearby(...)


def main():
    # input part
    size = int(input())
    # 將輸入的資訊，轉換為二位的場地，丟到list裡面，順便讓每個數值變成int
    cells = [
                [int(j) for j in input().split()]  # size
                    for i in range(size)]
    # 輸入二位座標，放到list裡面
    row, col = [int(i) for i in input().split()]

    # 調用 process function，將結果輸出至 result
    result = process(size, cells, row, col, [[row, col]]) # [row, col] 是 record 的 log

    # output
    print(result)


if __name__ == "__main__":
    main()

