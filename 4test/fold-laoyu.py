def main():
    row, col = map(int, input().split())
    data = [[int(v) for v in input().split()] for r in range(row)]
    for op in input().split():
        if op == "0":  # up dow
            newData = [[0 for c in range(col)] for r in range((row+1)//2)]
            for r in range((row+1)//2):
                for c in range(col):
                    if r + 1 == (row+1)/2:
                        newData[r][c] = data[r][c]
                    else:
                        newData[r][c] = data[r][c] + data[row-r-1][c]
        else: # left right
            data, col = [[data[r][c]+ data[r][col-c-1] if c+1 != (col+1)/2 else data[r][c] for c in range((col+1)//2)] for r in range(row)], (col+1)//2
    for r in range(row):
        print(*data[r])

if __name__ == "__main__":
    main()