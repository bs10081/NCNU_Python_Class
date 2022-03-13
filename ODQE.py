def main():
    # a, b, c: Is One-dimensional quadratic equation number.
    a = float(input())
    b = float(input())
    c = float(input())

    print((-b + (b*b - 4*a*c)**0.5)/(2*a))
    print((-b - (b*b - 4*a*c)**0.5)/(2*a))


if __name__ == "__main__":
    main()
