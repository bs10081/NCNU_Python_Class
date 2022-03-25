a = [1, 2, 3, 4]
sumNum = 0

for i in a:
    # In the for loop, "i" will sequentially read the values in list a.
    sumNum += i 
    # sumNum = sumNum + i, means, 0 + 1 > (0+1) + 2 > (1+2) + 3 > (3+3) + 4

print(sumNum)
