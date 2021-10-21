def main():
    # input the number
    numArray = int(input("Enter the total number of the number array: "))
    # Set a variable to save the reversed times
    numArrayCount = 0
    while numArrayCount < numArray:
        # input the number
        Number = int(input("Enter the number: "))
        # put the anser to the variable.
        addCount, revs_number = AddReverseNum(Number)
        print(addCount, revs_number)
        numArrayCount += 1

def reverseNum(Number):
    revs_number = 0
    # reverse the integer number using while loop
    while Number != 0:
        # Logic
        remainder = Number % 10
        revs_number = (revs_number * 10) + remainder
        Number = Number // 10
    return revs_number

def AddReverseNum(Number):
    # Avoid palindrome from appearing at the beginning, so do a calculation first.
    Number = Number + reverseNum(Number)
    # Set variable to null
    addCount = 0
    # Add 1 once executed
    addCount += 1
    while Number != reverseNum(Number):
        Number = Number + reverseNum(Number)
        addCount += 1
    return addCount, Number

if __name__ == "__main__":  # Check the main is fucking main.
    main()
