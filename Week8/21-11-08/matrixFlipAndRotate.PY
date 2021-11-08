# matrix flip and rotate
# flip: rotate by vertical axis
# 1 2 3 4 rotate 1 5 1
# 5 6 7 8 ==>    3 6 2
# 1 3 5 7        5 7 3
#                7 8 4
data = [[1, 2, 3 , 4], [5, 6, 7, 8],[1, 3, 5, 7]]
r, c, rows, cols = 3, 4, 3, 4

print(*[[data[rows-1-c][r] for c in range(rows)] for r in range(cols)])
                # -2    3       4           3        3             4