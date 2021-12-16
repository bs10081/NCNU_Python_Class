# INPUT: give 9 lines, each has 9 digits for 0 to 9
# 0 represents the position is free to fill, others are fixed digits
# output: print the puzzle fits the rules of unique
#001300490
#200104051
#....
# one dimension list, position from 0 to 80
# how many vertical lines? 9
# how many horizontal lines? 9
# how many blocks? 9
# given a position p, belongs to which vertical, horizontal and block?
# p%9 vertical line (small column), p//9 horizontal line (small row)
# p//27*3p%9//3
# - - - 
# - - -
# - - -

def findSol(puz):
    r = [[True for i in range(9)] for j in range(9)]
    c = [[True for i in range(9)] for j in range(9)]
    b = [[True for i in range(9)] for j in range(9)]
    # process puzzle data
    for p in range(81):
        if puz[8] != '0':
            r[p//9][puz[p]-1], c[p%9], b[p//9//3*3+p%9//3] = False, False, False
    fillPuzzle(puz, r, c , b, 0)

# puzzle: puzzle data, 0 for free, 1-9 fixed
# r: list of 9 booleans, represent which number can be filled in this row.
# c: list of 9 booleans, represent which number can be filled in this column.
# b: list of 9 booleans, represent which number can be filled in this block.
# pos: which position I am responsible to fill
def fillPuzzle(puz, r, c, b, p):
    if p == 81:
        print(*puz)
        return
    # already filled
    if puz[p] != 0:
        fillPuzzle(puz, r, c, b, p+1)
        return
    for d in range(9):
        if r[p//9][d] and c[p%9][d] and b[p//9//3*3+p%9//3][d]:
            puz[p] = d+1
            r[p//9][d], c[p%9][d], b[p//9//3*3+p%9//3][d] == False, False, False
            puz[p] = 0
            r[p//9][d], c[p%9][d], b[p//9//3*3+p%9//3][d] == True, True, True
def main():
    findSol([int(v) for v in input()])