class matrix():
    def __init__(self, r=0, c=0, d=[[]]):
        self.row = r
        self.col = c
        self.data = d

    def __add__(self, y):
        result = matrix()
        result.row = self.row
        result.col = self.col
        result.data = [[self.data[r][c]+y.data[r][c] for c in range()]]
        return result

x = matrix(3, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = matrix(3, 3, [[4, 5, 6], [1, 2, 3], [3, 4, 5]])
z = x + y
for r in range(z.row):
    print(*z.data[r])