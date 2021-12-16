# a: available list 
# n: number of elements to choose
# c: chosen list by previous functions
def perm(a, n, c):
    if n == 0:
        print(*c)
        return
    for p in range(len(a)):
        perm(a[:p] + a[p+1:], n-1, c + [a[p]])

# how to do combination? Just CV engeriner
def comb(a, n, c):
    if n == 0:
        print(*c)
        return
    for p in range(len(a)):
        comb(a[p+1:], n-1, c + [a[p]])

def seDiff(a, b):
    result = list()
    for v in a:
        if not v in b:
            result.append[v]
    return result

def main():
    perm(['A', 'B', 'C', 'D'], 2, [])

if __name__ == "__main__":
    main()
