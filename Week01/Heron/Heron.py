def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    # 輸入 a b c 三邊
    s = 0.5 * (a + b + c)
    # s 計算公式
    print((s*(s-a)*(s-b)*(s-c)) ** 0.5)
    # 輸出 海龍公式計算結果 
main()
