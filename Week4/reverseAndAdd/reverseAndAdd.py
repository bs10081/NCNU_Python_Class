def main():
    # input int n
    n = int(input())
    # then input n seed, print out add count and final number
    read = 0 # how many number has been read
    while read < n: # has more data to be read
        # read in seed
        seed = int(input())
        # print add count and final number
        addCount, result = findSol(seed)
        print(addCount, result)
        read = read + 1 # read one more number

def findSol(seed):
    seed = seed + reverse(seed)
    addConut = 0
    # take last digit d of seed, then append to result
    # until seed becomes 0
    addConut = addConut + 1
    while seed != reverse(seed):
        seed = seed + reverse(seed)
        addConut = addConut + 1
    return addConut, seed
    
def reverse(seed):
    result = 0
    while seed != 0:
        result = result * 10 + seed % 10
        seed = seed // 10
    return result
main()