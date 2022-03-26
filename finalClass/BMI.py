# calculate BMI
def main():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    bmi = weight / (height ** 2)
    print("Your BMI is: ", bmi)
    if bmi < 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("You are normal")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")

if __name__ == "__main__":
    main()