# h: height
# w: width

def findSol(data, h, w):
    while True: # keep cancel and drop
        # cancel 
        for r in range(h):
            for c in range(w):
                if data[r][c] != '0' and (r + 1 < h and data[r+1][c] == data[r][c] or r-1 >= 0 and data[r-1][c] == data[r][c] or c + 1 < w and data[r][c+1] == data[r][c] or c - 1 >= 0 and data[r][c-1] == data[r][c]):
                    mark (data, h, w, r, c)

        # drop
        result = drop(data, h, w)
        if result == data:
            break
        data = result
    # print result 
    for r in range(h):
        print(*data[r])
def mark(data, h, w, r, c):
    color = data[r][c]
    data[r][c] = '0'
    roff, coff = [1, -1, 0, 0], [0, 0, 1, -1]
    for d in range(4):
        if r + roff[d] >= 0 and r + roff[d] < h and r - roff[d] >= 0 and r - roff[d] < h and c + coff[d] < w and data[r + roff[d]][c + coff[d]] == color:
            mark(data, h, w, r - roff[d], c + coff[d])

def drop(data, h, w):
    result = [['0' for j in range(w)] for i in range(h)]
    for c in range(w): # for each colum
        dest = h - 1 # copy position
        for r in range(h - 1, -1, -1): # r is source position
            if data[r][c] != '0':
                result[dest][c], dest = data[r][c], dest-1
    return result

def main():
    h, w = map(int, input().split())
    findSol([[v for v in input().split()] for i in range(h)], h, w)

if __name__ == "__main__":
    main()
