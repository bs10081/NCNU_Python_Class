# 0 = Fold up matrix
# 1 = Fold in half

def main():
    # input data
    row, column = [int(i) for i in input().split()]
    matrix = [[int(j) for j in input().split()] for i in range(row)]
    operations = [int(i) for i in input().split()]
    # print(row,column,matrix,operations)
    # [ [1, 1, 1], 
    #   [1, 1, 1], 
    #   [1, 1, 1],
    #   [1 ,1 ,1] ]
    foldLeftSeed = 0
    foldUpSeed = 0
    for operation in operations:
        if operation == 1:
            matrix = foldLeft(row, column, matrix)
            foldLeftSeed += 1
        elif operation == 0:
            matrix = foldUp(row, column, matrix)
            foldUpSeed += 1

    # print matrix and format
    for r in matrix:
        # for c in r:
            # print(f"{c} ", end="")
        print(*r)
        # print()
    # print(foldUpSeed, foldLeftSeed, foldUpSeed + foldLeftSeed)

# define一個 fold up的 function
def foldUp(row, column, matrix):
    result = matrix
    if len(matrix) % 2 == 0:
        # 上下反轉
        temMatrix = matrix[::-1]
        # 將下半部分疊加到上半部分
        for r in range(len(matrix)//2):
            for c in range(len(matrix[0])):
                result[r][c] += temMatrix[r][c]
        # print(result)
        # 刪除後半
        for i in range(len(matrix)//2):
            del result[-1]
        # print(result)
    else:
        # 中間那一行不動，將中間行往下的數值疊加到中間行往上
        temMatrix = matrix[::-1]
        for r in range(len(matrix)//2):
            for c in range(len(matrix[0])):
                result[r][c] += temMatrix[-1-r][c]
        # print(result)
        # 刪除中間行以下的數列
        for i in range(len(matrix)//2):
            del result[-1]
        # print(result)
    return result

# define 一個左右折疊
def foldLeft(row, column, matrix):
    result = matrix
    
    if len(matrix[0]) % 2 == 0:
        temMatrix = matrix[::-1]
        for c in range(len(matrix[0])//2):
            for r in range(len(matrix)):
                result[r][c] += temMatrix[r][c]
        # print(result)
        # del column
        for i in range(len(matrix[0])//2):
            for r in range(len(matrix)):
                del result[r][-1]
        # print(result)
    else:
        temMatrix = matrix[::-1]
        for c in range(len(matrix[0])//2):
            for r in range(len(matrix)):
                result[r][c] += temMatrix[r][-1-c]
        # print(result)
        # del column
        for i in range(len(matrix[0])//2):
            for r in range(len(matrix)):
                del result[r][-1]
        # print(result)
    return result

if __name__ == "__main__":
    main()