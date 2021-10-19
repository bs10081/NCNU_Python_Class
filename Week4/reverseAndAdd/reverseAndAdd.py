# def main():
#     # input the number
#     inputNum = input()
#     Num = len(inputNum)-1
#     if inputNum != 0:
#         for i in range(Num, -1, -1):
#             num = (inputNum[i],)
#     else:
#         inputNum = inputNum 

#     print(num)
# main()

def main():
    # input the number
    Number = int(input("Enter the integer number: "))
    # Set a Real Number.
    realNumber = Number
    # Initiate value to null

def addReverseNumber(revs_number, realNumber):
    reverseNum()
    addNumber = revs_number + realNumber
    print("Anser: {}".format(addNumber))

def reverseNum():
    revs_number = 0
    # reverse the integer number using while loop
    while Number > 0:
        # Logic
        remainder = Number % 10
        revs_number = (revs_number * 10) + remainder
        Number = Number // 10
    
    addReverseNumber(revs_number, realNumber)

if __name__ == "__main__":  # Check the main is fucking main.
    main()
