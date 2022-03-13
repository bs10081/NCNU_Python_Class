# use Heron formula to calcuate area of a triangle
def main():
    # a, b, c: lengths of edges of a triangle
    a = float(input())
    b = float(input())
    c = float(input())
    
    s = (a+b+c)/2
    print((s*(s-a)*(s-b)*(s-c))**0.5)
main()
