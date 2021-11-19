def main():
    perm('ABCD', 3)

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)

# give a string S , eg "ABNCDEF", list all permutation of length n
# "ABCDE" 3
# ABC
# ACB
# BAC, BCA, CAB, CBA
# ABD, ABE, BCD, BCE, CDE

def perm(s, n):
    perm2(s, n, '')
# ABCD, 3, ''
# 1. 'BCD', '2', 'A'
    # 1.1 'CD', 1, 'AB'
        # 1.1.1 'D', 0, 'ABC'
        # 1.1.2 'C', 0, 'ABD'
    # 1.2 'BD', '1', 'AC'
    # 1.3 'BC', '1', 'AD'
# 2. 'ACD', '2', 'B'
# 3. 'ABD', '2', 'C'
# 4. 'ABC', '2', 'D'

# opitonal: 可選的資料
# n：要選出幾個
# chosen：前面同學已經幫我選好的

def perm2(optional, n, chosen):
    if n == 0:
        print(chosen)
        return
    for i in range(len(optional)):
        perm2(optional[0:i] + optional[i+1:], n-1, chosen + optional[i])
if __name__ == "__main__":
    main()
