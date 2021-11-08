def main():
    n = int(input())
    for row in magic(n): # put the row(result) to the myFormat to do format
        print(*myFormat(row, n))

def magic(n):
    # set All the numbers to 0
    result = [[0 for rowZero in range(n)] for columnZero in range(n)]
    # turn to the default Coordinate
    row, column = 0, n//2
    # write default coordinate to 1
    result[row][column] = 1
    # set for loop start in 2, and end in 25(if n is 5)
    for v in range(2,n*n+1):
        # move the coordinate to the nextrow and nextcolumn
        nextr, nextc = (row-1)%n, (column+1)%n
        if result[nextr][nextc] != 0:
            # go down the row
            nextr, nextc = (row+1)%n, column
        # put the last value to first value
        row, column, result[nextr][nextc] = nextr, nextc, v
    return result

def myFormat(data, n): # n = 5 data = 17 24 1 8 15
    for v in data:  # v = 2 data = 17 24 1 8 15
        yield str(v).zfill(len(str(n*n))) # v = 01   25

if __name__ == "__main__":
    main()