# a = ["1", "2", "3"]
# print("\n".join(a))

# print("\n".join([ "*"*(i + 1) for i in range(int(input()))]))

print("\n".join([ " "*(10-i)+"*"+"**"*(i) for i in range(10)]+[" "*(i)+"*"+"**"*(10-i) for i in range(10)]+[(" "*10+"*")]))

# def main():
#     line = 1
#     while line <= n:
#         print(' ' * ( n - line ) + '*' * ( 2 * line - 1 ))
#         line = line + 1
#     line = n - 1
#     while line >= 1:
#         print(' ' * ( n - line ) + '*' * ( 2 * line - 1 ))
#         line = line - 1
# main()
