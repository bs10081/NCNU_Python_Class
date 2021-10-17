def main():
    # input the number
    number = int(input("Enter the integer number: "))
    # Initiate value to null
    revs_number = 0
    # reverse the integer number using while loop
    while number > 0:
        # Logic
        remainder = number % 10
        revs_number = (revs_number * 10) + remainder
        number = number // 10
    print("The reverse number is: {}".format(revs_number))  #Output formated reverse number

if __name__ == "__main__":
    main()