#matrix add
from typing import TextIO


def add(A, B):
    C = []
    for r in range(len(A)):
        row = []
        for c in range(len(A[0])):
            row.append(A[r][c]+B[r][c])
        C.append(row)
    return C


def mul(A, B):
    C = []
    for r in range(len(A)):
        row = []
        for C in range(len(B[0])):
            total = 0
            for k in range(len(A[0])):
                total += A[r][k]*B[k][C]
            row.append(total)
        C.append(row)
    return C
def main():
    print(add([[1,2],[3,4]], [[5,6],[7,8]]))

main()