def isLeap(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)
def main():
    year = int(input("Enter the year: "))
    if isLeap(year):
        print("leap")
    else:
        print("not leap")
main()
