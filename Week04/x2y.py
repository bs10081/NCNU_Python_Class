def main():
    data = input()
    num = len(data)-1  

    if data != 0:
        for y in range(num, -1, -1):
            print(data[y], end="")
    else:
        print(data)
main()