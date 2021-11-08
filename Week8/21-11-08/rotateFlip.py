

# def main():
#     R, C, K = map(int, input().split())
#     data = [list(map(int, input().split())) for r in range(R)]
#     op = list(map(int, input().split()))[::-1]
#     for i in range(K):
#         if op[i] == 0:

#         else:

# def main():
#     # R = line, C = integer, M = integer
#     R, C, M = map(int, input().split())
#     data = []
#     for row in range(R):
#         data.append(list(map(int, input().split())))


#     for option in input().split():
#         if option == "0":
#             R, C, data = C, R, [[data[R-1-c][R] for c in range(R)] for r in range(C)] 
#         else:
#             data = data[::-1]

#     for row in data:
#         print(*data)

def flipMatrix(matrix):
    return matrix[::-1]

def rotateMatrix(R, C, matrix):
    result = [[0 for i in range(R)] for i in range(C)]
    # put the C to R
    for r in range(R):
        for c in range(C):
            result[C-c-1][r] = matrix[r][c]

    return result 

def test():
    a = [[1,2],[3,4]]
    a = flipMatrix(a)
    print(a)

def main():
    # input data
    R, C, M = [int(i) for i in input().split(" ")]
    matrix = [[int(j) for j in input().split(" ")] for i in range(R)]
    operations = [int(i) for i in input().split(" ")]

    # set a list
    # if operation = 1 then flip, else then rotate
    for operation in operations[::-1]:
        if operation == 1:
            matrix = flipMatrix(matrix)
        elif operation == 0:
            matrix = rotateMatrix(len(matrix), len(matrix[0]), matrix)
        
    # print row and cols's lenght
    print(len(matrix), len(matrix[0]))

    # print matrix and format
    for r in matrix:
        # for c in r:
            # print(f"{c} ", end="")
        print(*r)
        # print()

if __name__ == "__main__":
    main()