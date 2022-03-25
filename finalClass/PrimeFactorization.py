# 輸入一數 n ，將其質因數分解，由小到大換行輸出答案
def main():
    n = int(input())
    for i in range(2, n+1):
        while n % i == 0:
            print(i)
            n = n // i
    # 如果 n 本身為質數，其質因數分解的答案為 n 本身
    if n > 1:
        print(n)


if __name__ == '__main__':
    main()