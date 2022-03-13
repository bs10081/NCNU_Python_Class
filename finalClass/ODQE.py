def main():
    a = float(input())
    b = float(input())
    c = float(input())

    print((-b + (b*b - 4*a*c)**0.5) / (a*2), (-b - (b*b - 4*a*c)**0.5) / (a*2))
if __name__ == "__main__":
    main()