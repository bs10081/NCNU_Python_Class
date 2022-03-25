# calculate BMI
def main():
    # input height, weight
    height, weight = float(input("input height: ")), float(input("input weight: "))
    # calculate BMI
    BMI = weight / (height * height)
    # print BMI
    print(BMI)
    if BMI < 18.5:
        print("underweight")
    elif BMI < 25:
        print("normal")
    elif BMI < 30:
        print("overweight")
    else:
        print("obese")

if __name__ == "__main__":
    main()