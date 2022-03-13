# define main() function
def main():
    # input weight from standard input(), that is keyboard.
    weight = int(input("體重(Kg):"))
    height = int(input("身高(CM): "))
    # print out BMI value
    print(weight/(height/100)**2)

# call function main()
if __name__ == "__main__":
    main()
