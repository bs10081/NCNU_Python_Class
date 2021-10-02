# 學號：110213027
# 姓名：簡齊君

def isInput():
    FirstSide = float(input("Please input the first side: "))
    SecondSide = float(input("Please input the second side: "))
    ThirdSide = float(input("Please input the third side: "))
    # Input three side.
    valueList = [FirstSide, SecondSide, ThirdSide]  # Put the value in the list.
    valueList.sort()

    return [int(i) for i in valueList]      # Convert floating point value into integer by using inline for loop.

def main():
    FirstSide, SecondSide, ThirdSide = isInput()

    print(f"{FirstSide} {SecondSide} {ThirdSide}")
    # Output Number (Min to Max)
    a = FirstSide ** 2 + SecondSide ** 2 
    b = ThirdSide ** 2
    # Set a, b, c variable
    if (FirstSide == SecondSide == ThirdSide):
        print("No")     # Equilateral triangle
    elif (FirstSide == SecondSide or SecondSide == ThirdSide):
        print("No")     # Isosceles triangle
    elif (a > b):       # a + b > c
        print("Acute")
    elif (a < b ):      # a + b < c
        print("Obtuse")
    elif (a  == b):     # a + b = c
        print("Right")
    else:
        print("No")

if __name__ == "__main__":     # Python main program by fucking checking this is the main module.
    main()
