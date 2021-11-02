def add(A, B):
    # C = []
    # for r in range(len(A)):
    #     row = []
    #     for c in range(len(A[0])):
    #         row.append(A[r][c]+B[r][c])
    #     C.append(row)
    # return C
    return [[A[r][c] + B[r][c] for c in range(len(A[0]))] for r in range(len(A))]


def mul(A, B):
    return [[sum(A[r][k]*B[k][c] for c in range(len(A[0]))] for r in range(len(A))]
    # C = []
    # for r in range(len(A)):
    #     row = []
    #     for C in range(len(B[0])):
    #         total = 0
    #         for k in range(len(A[0])):
    #             total += A[r][k]*B[k][C]
    #         row.append(total)
    #     C.append(row)
    # return C

def main():
    print(mul([[1,2],[3,4]], [[5,6],[7,8]]))

main()