def main():
    # 求ax^2 + bx + c = 0
    a = float(input('a: ' ))
    b = float(input('b: ' ))
    c = float(input('c: ' ))
    print((-b+(b*b-4*a*c)**0.5)/(2*a))
    print((-b-(b*b-4*a*c)**0.5)/(2*a))

main()