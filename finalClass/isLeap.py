
def isLeap(y):
    return y%400 == 0 or (y%100 != 0 and y%4 == 0)
    
    # Base👇🏻, Advanced👆🏻

    # if y % 400 == 0:
    #     return True
    # elif y&100 == 0:
    #     return False
    # elif y&4 == 0:
    #     return True
    # else:
    #     return False

def main():
    y = int(input())
    if isLeap(y):
        print("leap")
    else:
        print("common")

if __name__ == "__main__":
    main()