def main():
    x, y = int(input()), int(input())
    # 讓x小於y
    if x > y:
        x,y = y,x
    count = 0
    while x <= y:
        if prime(x):
            count += 1
        x += 1
    print(count)

#植樹就是除了自己跟1之外都不能整除
def prime(v):
    div = 2
    while div*div < v:
        if v % div == 0:
            return False
        div = div + 1
    return True




main()