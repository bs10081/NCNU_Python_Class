# eg
# 1237 ==> distance = 3
# 9736 ==> distance = 4
# 1111 ==> distance = 0

def main():
    d, k = map(int, input().split())    # give int d and k
    for temDis in range(10 ** (d-1), 10 ** d):  # output all number between 10..0 ~ 99..9 such that
        if distance(temDis, k):     # if True then print number
            print(temDis)

def distance(temDis, k):
    # Take the remainder of 10
    previous = temDis % 10
    # Divide by 10
    digit = temDis // 10
    # Set another variable to save the number
    temDigit = abs(digit%10 - previous)
    # Do again
    previous = digit % 10
    digit = digit // 10

    while digit != 0:
        # Set a another one to save number
        dis = abs(digit%10 - previous)
        # Do again
        previous = digit % 10
        digit = digit // 10
        if dis > temDigit:  # if first > last
            temDigit = dis  # Upside down
    if temDigit <= k:   # loargest adajacent digit  distance <= k
        return True

if __name__ == "__main__":  # check main is main then run main.
    main()