def main():
    perm('123456789',9,'')

def fitEq(Number):
    return int(Number[0:2]) * int(Number[2:3]) == int(Number[3:5]) and int(Number[3:5]) + int(Number[5:7]) == int(Number[7:9])   

def perm(optional, n, chosen):
    if n == 0:
        if fitEq(chosen):
            print(chosen)
        return
    for i in range(len(optional)):
        perm(optional[0:i] + optional[i+1:], n-1, chosen + optional[i])

if __name__ == "__main__":
    main()