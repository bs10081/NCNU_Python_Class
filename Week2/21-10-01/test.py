def myinput():
    a = float(input())
    b = float(input())
    c = float(input())
def findVal(x,y,z):
    s = (x+y+z)/2
    return (s*(s-x)*(s-y)*(s-z))**0.5

def main():
    x,y,z = myinput()
    print(findVal(x,y,z))

main()



